"""FlowLang - A declarative DSL for ROS2 robotics.

FlowLang Phase 1 (Core Language) provides:
- ANTLR4 grammar definitions for .flow, .node, and .interface files
- AST representation and semantic analysis
- Python code generator for ROS2 nodes
- Launch file transpiler
"""

__version__ = "0.1.0"
__all__ = ["compiler", "ast", "semantic", "codegen"]
