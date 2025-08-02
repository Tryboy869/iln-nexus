#!/usr/bin/env python3
"""
Setup configuration for iln-core
🌌 ILN - Informatique Language Nexus
Complete PyPI package configuration
"""

from setuptools import setup, find_packages
from pathlib import Path
import re

# Read version from main module
def get_version():
    version_file = Path(__file__).parent / "iln" / "__init__.py"
    if version_file.exists():
        version_content = version_file.read_text()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_content, re.M)
        if version_match:
            return version_match.group(1)
    return "1.0.0"

# Read README for long description
def get_long_description():
    readme_file = Path(__file__).parent / "README.md"
    if readme_file.exists():
        return readme_file.read_text(encoding="utf-8")
    return "ILN - Informatique Language Nexus: Revolutionary Language Unification System"

# Read requirements
def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        return [
            line.strip() 
            for line in requirements_file.read_text().splitlines() 
            if line.strip() and not line.startswith("#")
        ]
    return ["requests>=2.25.0"]

setup(
    # Basic package info
    name="iln-core",
    version=get_version(),
    author="Anzize Daouda",
    author_email="nexusstudio100@gmail.com",
    maintainer="Anzize Daouda",
    maintainer_email="nexusstudio100@gmail.com",
    
    # Package description
    description="🌌 ILN - Revolutionary Language Unification System. One Language, All Paradigms.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    
    # URLs and links
    url="https://github.com/iln-nexus/core",
    project_urls={
        "Homepage": "https://iln-nexus.com",
        "Documentation": "https://docs.iln-nexus.com",
        "Source Code": "https://github.com/iln-nexus/core",
        "Bug Tracker": "https://github.com/iln-nexus/core/issues",
        "Changelog": "https://github.com/iln-nexus/core/blob/main/CHANGELOG.md",
        "Funding": "https://github.com/sponsors/AnzizeDaouda",
        "Live Demos": "https://ai-web-navigator-demo-8hxj.onrender.com/",
        "WebPilot Demo": "https://ai-web-navigator-j5kp.onrender.com/",
        "Upgrade to Pro": "https://iln-nexus.com/pro",
        "Contact": "mailto:nexusstudio100@gmail.com",
        "Discord": "https://discord.gg/iln-nexus",
        "Twitter": "https://twitter.com/ILN_Nexus"
    },
    
    # Package structure
    packages=find_packages(),
    py_modules=["iln"] if not find_packages() else [],
    include_package_data=True,
    zip_safe=False,
    
    # Python version requirements
    python_requires=">=3.8",
    
    # Dependencies
    install_requires=get_requirements(),
    
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "isort>=5.10.0",
            "pre-commit>=2.20.0"
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0"
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.8.0"
        ],
        "pro": [
            "requests>=2.28.0",
            "aiohttp>=3.8.0",
            "websockets>=10.0"
        ]
    },
    
    # Entry points for CLI
    entry_points={
        "console_scripts": [
            "iln=iln:main",
            "iln-core=iln:main",
            "iln-demo=iln:demo_cli",
        ],
    },
    
    # Package classification
    classifiers=[
        # Development Status
        "Development Status :: 4 - Beta",
        
        # Intended Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        
        # Topic
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators", 
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "Topic :: System :: Distributed Computing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Programming Language
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10", 
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        
        # Operating System
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        
        # Environment
        "Environment :: Console",
        "Environment :: Web Environment",
        "Environment :: No Input/Output (Daemon)",
        
        # Natural Language
        "Natural Language :: English",
        "Natural Language :: French"
    ],
    
    # Keywords for discoverability
    keywords=[
        # Core concepts
        "iln", "language-unification", "essence-absorption", "multi-language",
        "programming-languages", "polyglot", "cross-language", "paradigm-fusion",
        
        # Specific languages
        "python", "javascript", "go", "rust", "nodejs", "c++", "java", "kotlin",
        
        # Programming concepts  
        "concurrency", "async", "memory-safety", "reactive-programming",
        "functional-programming", "object-oriented", "event-driven",
        
        # Architecture
        "microservices", "distributed-systems", "cloud-native", "api-integration",
        "multi-engine", "orchestration", "coordination",
        
        # Developer tools
        "developer-tools", "productivity", "automation", "code-generation",
        "framework", "library", "sdk", "cli-tools",
        
        # Domains
        "web-development", "mobile-development", "ai", "machine-learning",
        "data-science", "backend", "frontend", "full-stack",
        
        # Business
        "enterprise", "saas", "api", "professional", "commercial"
    ],
    
    # Package metadata
    platforms=["any"],
    license="MIT",
    
    # Custom setup configuration
    setup_requires=[
        "wheel>=0.37.0",
        "setuptools>=60.0.0"
    ],
    
    # Test configuration
    tests_require=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0"
    ],
    test_suite="tests",
    
    # Additional files to include
    package_data={
        "": [
            "*.md", 
            "*.txt", 
            "*.yml", 
            "*.yaml", 
            "*.json",
            "LICENSE*",
            "CHANGELOG*",
            "CONTRIBUTING*"
        ],
    },
    
    # Exclude development files from distribution
    exclude_package_data={
        "": [
            "tests/*",
            "docs/*", 
            ".git*",
            "*.pyc",
            "__pycache__/*"
        ]
    }
)

# Custom commands for development
try:
    from setuptools import Command
    
    class DemoCommand(Command):
        """Custom command to run ILN demo"""
        description = "Run ILN interactive demo"
        user_options = []
        
        def initialize_options(self):
            pass
            
        def finalize_options(self):
            pass
            
        def run(self):
            from iln import ILN
            iln = ILN()
            iln.demo()
    
    class InfoCommand(Command):
        """Custom command to show ILN info"""
        description = "Show ILN system information"
        user_options = []
        
        def initialize_options(self):
            pass
            
        def finalize_options(self):
            pass
            
        def run(self):
            from iln import ILN
            import json
            iln = ILN()
            info = iln.get_info()
            print(json.dumps(info, indent=2))
    
    # Add custom commands
    setup.cmdclass = {
        'demo': DemoCommand,
        'info': InfoCommand
    }
    
except ImportError:
    # If setuptools doesn't support custom commands, skip them
    pass
