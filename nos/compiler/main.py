"""CLI entry point for NOS compiler.

Provides command-line interface for compiling NOS files.
"""

import argparse
import sys
from pathlib import Path

from .pipeline import CompilerPipeline, CompilationResult


def create_parser() -> argparse.ArgumentParser:
    """Create argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog='nos',
        description='NOS compiler for ROS2'
    )

    parser.add_argument(
        'files',
        nargs='+',
        help='NOS source files (.nos, .node, .interface)'
    )

    parser.add_argument(
        '-o', '--output',
        default='./generated',
        help='Output directory for generated files (default: ./generated)'
    )

    parser.add_argument(
        '-t', '--target',
        choices=['python', 'cpp'],
        default='python',
        help='Target language (default: python)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Parse and analyze but do not generate output'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )

    return parser


def format_result(result: CompilationResult, file_path: str) -> str:
    """Format compilation result for display."""
    lines = []

    if result.success:
        lines.append(f"âœ“ {file_path}")
        if result.files:
            lines.append(f"  Generated {len(result.files)} file(s):")
            for f in result.files:
                lines.append(f"    - {f}")
    else:
        lines.append(f"âœ— {file_path}")

    if result.warnings:
        lines.append(f"  Warnings ({len(result.warnings)}):")
        for w in result.warnings:
            lines.append(f"    ! {w}")

    if result.errors:
        lines.append(f"  Errors ({len(result.errors)}):")
        for e in result.errors:
            lines.append(f"    âœ— {e}")

    return "\n".join(lines)


def main(args: list = None) -> int:
    """Main entry point for the CLI.

    Args:
        args: Command line arguments (defaults to sys.argv)

    Returns:
        Exit code (0 for success, 1 for failure)
    """
    parser = create_parser()
    parsed = parser.parse_args(args)

    # Validate input files
    invalid_files = []
    for f in parsed.files:
        path = Path(f)
        if not path.exists():
            invalid_files.append(f"File not found: {f}")
        elif not path.suffix in ['.nos', '.node', '.interface']:
            invalid_files.append(f"Invalid file type: {f}")

    if invalid_files:
        for error in invalid_files:
            print(f"Error: {error}", file=sys.stderr)
        return 1

    # Configure pipeline
    options = {
        'target': parsed.target,
        'verbose': parsed.verbose
    }

    pipeline = CompilerPipeline(options)

    # Compile files
    success_count = 0
    failure_count = 0

    for file_path in parsed.files:
        result = pipeline.compile_file(file_path)

        if parsed.verbose or not result.success:
            print(format_result(result, file_path))
            print()

        if result.success:
            success_count += 1
            if not parsed.dry_run:
                pipeline.write_outputs(result, parsed.output)
        else:
            failure_count += 1

    # Summary
    if parsed.verbose:
        print(f"\nSummary: {success_count} succeeded, {failure_count} failed")

    return 0 if failure_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
