"""End-to-end compilation pipeline for FlowLang.

Orchestrates the complete compilation process from source file
to generated code.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path
import sys

# ANTLR4 imports
from antlr4 import CommonTokenStream, InputStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener

# Import generated ANTLR4 classes
from ..grammar.FlowLangLexer import FlowLangLexer
from ..grammar.FlowLangParser import FlowLangParser

from ..ast import nodes
from ..ast.builder import ASTBuilder
from ..semantic import SemanticAnalyzer, AnalysisResult
from ..codegen import PythonGenerator, LaunchTranspiler, GenerationOutput


class FlowLangSyntaxError(Exception):
    """Syntax error in FlowLang source."""
    pass


class FlowLangErrorListener(ErrorListener):
    """Custom error listener for ANTLR4 syntax errors."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Syntax error at {line}:{column} - {msg}"
        self.errors.append(error_msg)


@dataclass
class CompilationResult:
    """Result of a compilation.

    Attributes:
        success: True if compilation succeeded
        files: Generated files (path -> content)
        errors: Compilation errors
        warnings: Compilation warnings
        ast: The parsed and validated AST
    """
    success: bool = False
    files: Dict[str, str] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    ast: Optional[nodes.ASTNode] = None


class CompilerPipeline:
    """End-to-end FlowLang compilation pipeline.

    Orchestrates:
    1. Source file parsing (using ANTLR4)
    2. AST construction
    3. Semantic analysis
    4. Code generation

    Usage:
        >>> pipeline = CompilerPipeline()
        >>> result = pipeline.compile_file("input.flow")
        >>> if result.success:
        ...     pipeline.write_outputs(result, "output_dir/")
        ...     print(f"Generated {len(result.files)} files")
        ... else:
        ...     for error in result.errors:
        ...         print(f"Error: {error}")

    Attributes:
        options: Compilation options dict
        verbose: Whether to print debug information
        target: Target language ('python' or 'cpp')
    """

    def __init__(self, options: Optional[Dict[str, Any]] = None):
        """Initialize the compiler pipeline.

        Args:
            options: Compilation options including:
                - target: 'python' or 'cpp' (default: 'python')
                - verbose: Print debug info
                - output_dir: Default output directory
        """
        self.options = options or {}
        self.verbose = self.options.get('verbose', False)
        self.target = self.options.get('target', 'python')

    def compile_file(self, file_path: str) -> CompilationResult:
        """Compile a single FlowLang source file.

        Args:
            file_path: Path to .flow, .node, or .interface file

        Returns:
            CompilationResult with generated files or errors

        Example:
            >>> pipeline = CompilerPipeline({'verbose': True})
            >>> result = pipeline.compile_file('my_node.node')
            >>> print(f"Success: {result.success}")
            >>> print(f"Files generated: {list(result.files.keys())}")
        """
        result = CompilationResult()

        try:
            # Step 1: Parse source file
            if self.verbose:
                print(f"Parsing: {file_path}")

            ast = self._parse_file(file_path)
            if ast is None:
                result.errors.append(f"Failed to parse: {file_path}")
                return result

            result.ast = ast

            # Step 2: Semantic analysis
            if self.verbose:
                print(f"Analyzing: {file_path}")

            analysis = self._analyze(ast)
            result.errors.extend([str(e) for e in analysis.errors])
            result.warnings.extend([str(w) for w in analysis.warnings])

            if not analysis.is_valid:
                return result

            # Step 3: Code generation
            if self.verbose:
                print(f"Generating: {file_path}")

            generated = self._generate(ast, analysis.symbol_table)
            result.files = generated.files

            result.success = True
            return result

        except Exception as e:
            result.errors.append(f"Compilation error: {str(e)}")
            if self.verbose:
                import traceback
                result.errors.append(traceback.format_exc())
            return result

    def compile_string(self, source: str, file_name: str = "<string>") -> CompilationResult:
        """Compile FlowLang source from a string.

        Args:
            source: FlowLang source code
            file_name: Name for error reporting

        Returns:
            CompilationResult with generated files or errors
        """
        result = CompilationResult()

        try:
            # Parse
            ast = self._parse_string(source, file_name)
            if ast is None:
                result.errors.append(f"Failed to parse: {file_name}")
                return result

            result.ast = ast

            # Analyze
            analysis = self._analyze(ast)
            result.errors.extend([str(e) for e in analysis.errors])
            result.warnings.extend([str(w) for w in analysis.warnings])

            if not analysis.is_valid:
                return result

            # Generate
            generated = self._generate(ast, analysis.symbol_table)
            result.files = generated.files

            result.success = True
            return result

        except Exception as e:
            result.errors.append(f"Compilation error: {str(e)}")
            return result

    def _parse_file(self, file_path: str) -> Optional[nodes.ASTNode]:
        """Parse a source file into AST using ANTLR4.

        Args:
            file_path: Path to .flow, .node, or .interface file

        Returns:
            Root AST node or None if parsing fails
        """
        path = Path(file_path)
        if not path.exists():
            return None

        try:
            source = path.read_text(encoding='utf-8')
            return self._parse_string(source, str(path))
        except Exception as e:
            if self.verbose:
                print(f"Error reading file {file_path}: {e}")
            return None

    def _parse_string(self, source: str, file_name: str) -> Optional[nodes.ASTNode]:
        """Parse source string into AST using ANTLR4.

        Args:
            source: FlowLang source code
            file_name: Name for error reporting

        Returns:
            Root AST node or None if parsing fails
        """
        try:
            # Create input stream from source
            input_stream = InputStream(source)

            # Create lexer with custom error listener
            lexer = FlowLangLexer(input_stream)
            error_listener = FlowLangErrorListener()
            lexer.removeErrorListeners()
            lexer.addErrorListener(error_listener)

            # Create token stream
            tokens = CommonTokenStream(lexer)

            # Create parser with custom error listener
            parser = FlowLangParser(tokens)
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            # Parse starting from the 'flowFile' rule
            parse_tree = parser.flowFile()

            # Check for syntax errors
            if error_listener.errors:
                if self.verbose:
                    for error in error_listener.errors:
                        print(f"  {error}")
                return None

            # Convert parse tree to AST using ASTBuilder
            builder = ASTBuilder(file_name)
            ast = builder.visit(parse_tree)

            return ast

        except Exception as e:
            if self.verbose:
                print(f"Parse error in {file_name}: {e}")
                import traceback
                traceback.print_exc()
            return None

    def _analyze(self, ast: nodes.ASTNode) -> AnalysisResult:
        """Run semantic analysis on AST."""
        analyzer = SemanticAnalyzer()
        return analyzer.analyze(ast)

    def _generate(self, ast: nodes.ASTNode, symbol_table: Any) -> GenerationOutput:
        """Generate target code from AST."""
        output = GenerationOutput()

        if self.target == 'python':
            # Generate Python nodes
            node_gen = PythonGenerator(self.options)
            node_output = node_gen.generate(ast, symbol_table)
            output.files.update(node_output.files)

            # Generate launch files
            launch_gen = LaunchTranspiler(self.options)
            launch_output = launch_gen.generate(ast, symbol_table)
            output.files.update(launch_output.files)

        elif self.target == 'cpp':
            # TODO: Implement C++ generator
            pass

        return output

    def write_outputs(self, result: CompilationResult, output_dir: str) -> bool:
        """Write generated files to output directory.

        Args:
            result: Compilation result with files
            output_dir: Target directory path

        Returns:
            True if all files written successfully
        """
        if not result.success:
            return False

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        try:
            for file_path, content in result.files.items():
                full_path = output_path / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content, encoding='utf-8')
                if self.verbose:
                    print(f"  Wrote: {full_path}")
            return True
        except Exception as e:
            result.errors.append(f"Failed to write output: {str(e)}")
            return False

    def compile_multiple(self, file_paths: List[str]) -> Dict[str, CompilationResult]:
        """Compile multiple files and return results.

        Args:
            file_paths: List of source file paths

        Returns:
            Dictionary mapping file paths to compilation results
        """
        results = {}
        for path in file_paths:
            results[path] = self.compile_file(path)
        return results
