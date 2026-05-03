# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-04-20

### Phase 1: Core Language Implementation

This release establishes the foundational compiler infrastructure for NOS (Node Orchestration System), a declarative DSL for ROS2 robotics development.

### Added

- **ANTLR4 Grammar** (`nos/grammar/`)
  - Complete lexer and parser for NOS syntax
  - Support for `.nos`, `.node`, and `.interface` file extensions
  - Auto-generated parser files from grammar definitions

- **AST Construction** (`nos/ast/`)
  - Typed AST node hierarchy with 40+ node types
  - Source location tracking for accurate error reporting
  - Visitor pattern implementation for AST traversal
  - ASTBuilder for converting ANTLR4 parse trees to typed AST

- **Semantic Analysis** (`nos/semantic/`)
  - Symbol table with scoped symbol resolution
  - Multi-pass semantic analyzer (symbol building, reference resolution)
  - Type checking for ROS2 message types
  - Constraint validation (range, one_of, etc.)
  - Comprehensive diagnostic reporting with error codes

- **Python Code Generation** (`nos/codegen/`)
  - PythonGenerator: Generates ROS2 Python nodes from AST
  - LaunchTranspiler: Converts NOS launch to ROS2 Python launch
  - Support for lifecycle-managed nodes
  - QoS profile generation
  - Automatic parameter declaration with validation

- **Runtime Library** (`nos/runtime/`)
  - NOSNode: Enhanced base class for ROS2 nodes
  - NOSLifecycleNode: Lifecycle-managed node base class
  - Decorators for declarative parameter/subscription/service definitions
  - QoS utility functions (reliable, best_effort, sensor, parameter profiles)

- **Compilation Pipeline** (`nos/compiler/`)
  - End-to-end compiler pipeline (parse -> analyze -> generate)
  - CLI entry point with argparse interface
  - Support for file and string-based compilation
  - Batch compilation for multiple files
  - Dry-run mode for validation without generation

- **Security Validation** (`nos/security/`)
  - PythonCodeSanitizer with defense-in-depth validation
  - AST allowlist-based validation
  - Dangerous builtin detection (eval, exec, compile, etc.)
  - Import restriction to safe modules only
  - Pattern-based detection of obfuscation attempts
  - Comprehensive audit logging

- **Test Suite** (`tests/`)
  - Unit tests for AST nodes and builder
  - Semantic analysis tests
  - Code generation tests
  - Security validation tests
  - Integration tests for full compilation pipeline

### Known Limitations

- C++ code generator is planned but not yet implemented
- IDE/language server support not yet available
- Visual diagram generation not yet implemented
- Some advanced constraint types not yet enforced at runtime
- No incremental compilation support
- Limited error recovery in parser (fails on first syntax error)

### Security

- Implemented security validation for all embedded Python code
- Blocked dangerous builtins (eval, exec, __import__, etc.)
- Restricted imports to safe module allowlist
- Added detection for code obfuscation attempts
- All callback code is wrapped in try/except for runtime safety

[0.1.0]: https://github.com/your-org/nos/releases/tag/v0.1.0
