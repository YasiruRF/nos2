# NOS Foundation

## Core Goal
NOS is a high-level, declarative domain-specific language (DSL) designed for ROS2 robotics development. Its primary mission is to:
- **Reduce ROS2 boilerplate** by 70-80% through declarative syntax.
- **Ensure Type-Safety** via a strongly-typed AST and semantic analysis.
- **Maintain Compatibility** with existing ROS2 tooling (colcon, rclpy, rclcpp).
- **Automate Infrastructure**: Automatically handle node initialization, topic management, and lifecycle states.

## Project Structure
- `nos/grammar/`: ANTLR4 grammar definitions (`.g4`) and generated Python parser files.
- `nos/ast/`: Abstract Syntax Tree definition (`nodes.py`) and conversion logic (`builder.py`).
- `nos/semantic/`: Symbol tables and semantic validation rules.
- `nos/codegen/`: Target code generation (currently Python-focused, C++ planned).
- `nos/runtime/`: Base classes and decorators providing the execution bridge to ROS2.
- `nos/compiler/`: Orchestration of the parsing, analysis, and generation pipeline.
- `nos/security/`: Logic for code sanitization and safety validation.

## Development Mandates
- **Parser Integrity**: Never manually edit files in `nos/grammar/`. Always regenerate from `.g4` sources.
- **Validation-First**: All language features must be empirically verified with both the AST builder and generated output.
- **Idiomatic ROS2**: Generated code must follow established ROS2 best practices (e.g., using `rclpy` lifecycle nodes for managed components).
