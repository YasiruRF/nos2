"""Setup script for FlowLang package."""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="flowlang",
    version="0.1.0",
    description="A declarative DSL for ROS2 robotics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="FlowLang Team",
    license="Apache-2.0",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.13.0",
        "jinja2>=3.0.0",
        "rclpy>=3.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
            "flake8>=4.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "flowlang=flowlang.compiler.main:main",
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
    ],
)
