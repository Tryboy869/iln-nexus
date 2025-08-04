#!/usr/bin/env python3
"""
Setup configuration for iln-core v2.0.0
🌌 ILN - Informatique Language Nexus
Enhanced PyPI package configuration with Level 3 + Strategic Engines
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
    
    # Fallback to reading from main iln.py file
    main_file = Path(__file__).parent / "iln.py"
    if main_file.exists():
        main_content = main_file.read_text()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", main_content, re.M)
        if version_match:
            return version_match.group(1)
    
    return "2.0.0"

# Read README for long description
def get_long_description():
    readme_file = Path(__file__).parent / "README.md"
    if readme_file.exists():
        return readme_file.read_text(encoding="utf-8")
    return """
🌌 ILN v2.0.0 - Revolutionary Language Unification System

**New in v2.0:**
- Level 3 Champion Cascade Strategy (Pro Feature)
- 7 Strategic Engines (Python, NodeJS, Go, Rust, Java, C++, TypeScript)
- 12 Critical Essences including ml!, stream!, secure!, mobile!, api!
- Modular Architecture for Future Extensions
- Enhanced Performance Monitoring & Benchmarking

Community Edition includes Levels 1-2 (Open Source)
Pro Features (Levels 3-4) available at: https://iln-nexus.com/pro

Stop learning 10+ programming languages. Master ONE language that absorbs the essence of ALL others.

Visit: https://github.com/Tryboy869/iln-nexus
"""

# Read requirements
def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"
    if requirements_file.exists():
        return [
            line.strip() 
            for line in requirements_file.read_text().splitlines() 
            if line.strip() and not line.startswith("#")
        ]
    return [
        "requests>=2.28.0",
        "typing-extensions>=4.0.0"
    ]

setup(
    # Basic package info - UPDATED for v2.0
    name="iln-core",
    version="2.0.0",  # Force v2.0.0
    author="Anzize Daouda",
    author_email="nexusstudio100@gmail.com",
    maintainer="Anzize Daouda", 
    maintainer_email="nexusstudio100@gmail.com",
    
    # Enhanced package description for v2.0
    description="🌌 ILN v2.0 - Revolutionary Language Unification System. 7 Engines, Level 3 Champions, One Language All Paradigms.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    
    # Updated URLs for v2.0
    url="https://github.com/Tryboy869/iln-nexus",
    project_urls={
        "Homepage": "https://github.com/Tryboy869/iln-nexus",
        "Documentation": "https://docs.iln-nexus.com",
        "Source Code": "https://github.com/Tryboy869/iln-nexus",
        "Bug Tracker": "https://github.com/Tryboy869/iln-nexus/issues",
        "Releases": "https://github.com/Tryboy869/iln-nexus/releases",
        "Changelog": "https://github.com/Tryboy869/iln-nexus/blob/main/CHANGELOG.md",
        "Level 1-2 Documentation": "https://github.com/Tryboy869/iln-nexus/blob/main/LEVEL-1.md",
        "Level 3 Documentation": "https://github.com/Tryboy869/iln-nexus/blob/main/LEVEL-3.md",
        "Manifesto": "https://github.com/Tryboy869/iln-nexus/blob/main/MANIFESTE.in",
        
        # Live demos updated
        "AI Web Navigator Demo": "https://ai-web-navigator-ddz5.onrender.com/",
        "WebPilot API Demo": "https://webpilot-api.onrender.com/",
        "WebPilot API Demo": "https://webpilot-api.onrender.com/",
        "Fusion EL4X Demo": "https://fusion-el4x.onrender.com/",
        "NSS Nexus Studio": "https://nss-nexus-studio-server.onrender.com/",
        "Nexus Memory Demo": "https://nexus-contextual-memory.onrender.com/",
        
        # Business & Support
        "Upgrade to Pro": "https://iln-nexus.com/pro",
        "Contact": "mailto:nexusstudio100@gmail.com",
        "Support": "mailto:nexusstudio100@gmail.com",
        "Enterprise": "mailto:nexusstudio100@gmail.com?subject=ILN%20Enterprise"
    },
    
    # Package structure
    packages=find_packages() if find_packages() else [],
    py_modules=["iln"] if not find_packages() else [],
    include_package_data=True,
    zip_safe=False,
    
    # Python version requirements - Updated for v2.0 features
    python_requires=">=3.8",
    
    # Dependencies - Enhanced for v2.0
    install_requires=[
        "requests>=2.28.0",
        "typing-extensions>=4.0.0;python_version<'3.11'"
    ],
    
    # Enhanced optional dependencies for v2.0
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-benchmark>=4.0.0",  # NEW: for benchmarking
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
            "isort>=5.10.0",
            "pre-commit>=2.20.0",
            "tox>=4.0.0"  # NEW: for multi-environment testing
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
            "sphinx-autodoc-typehints>=1.19.0"  # NEW: better type hints in docs
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.8.0",
            "pytest-benchmark>=4.0.0",  # NEW: performance testing
            "pytest-xdist>=3.0.0"  # NEW: parallel testing
        ],
        "pro": [
            "requests>=2.28.0",
            "aiohttp>=3.8.0",
            "websockets>=10.0",
            "pydantic>=1.10.0"  # NEW: for enhanced data validation
        ],
        "engines": [  # NEW: Optional engine-specific dependencies
            "numpy>=1.21.0",  # For ML essences
            "asyncio-mqtt>=0.13.0", # For stream essences  
            "cryptography>=38.0.0",  # For secure essences
            "fastapi>=0.85.0",  # For API essences
            "uvicorn>=0.18.0"  # For mobile/web essences
        ],
        "all": [  # NEW: Install everything
            "pytest>=7.0.0", "pytest-cov>=4.0.0", "pytest-benchmark>=4.0.0",
            "black>=22.0.0", "mypy>=1.0.0", "sphinx>=5.0.0",
            "aiohttp>=3.8.0", "numpy>=1.21.0", "fastapi>=0.85.0"
        ]
    },
    
    # Enhanced entry points for v2.0
    entry_points={
        "console_scripts": [
            "iln=iln:main",
            "iln-core=iln:main",
            "iln-demo=iln:demo_cli",
            "iln-benchmark=iln:benchmark_cli",  # NEW: dedicated benchmark CLI
            "iln-info=iln:info_cli",  # NEW: dedicated info CLI
        ],
    },
    
    # Enhanced package classification for v2.0
    classifiers=[
        # Development Status - Updated to Beta for v2.0
        "Development Status :: 4 - Beta",
        
        # Intended Audience - Expanded
        "Intended Audience :: Developers",
        "Intended Audience :: Education", 
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",  # NEW
        "Intended Audience :: End Users/Desktop",  # NEW
        
        # Topic - Enhanced categories
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers", 
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Build Tools",  # NEW
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Systems Administration",  # NEW
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Database :: Database Engines/Servers",  # NEW
        "Topic :: Communications :: Chat",  # NEW
        "Topic :: Multimedia :: Graphics",  # NEW
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Programming Language - Updated Python versions
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",  # NEW: Future support
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        
        # Multi-language support indicators
        "Programming Language :: JavaScript",  # NEW
        "Programming Language :: Java",  # NEW  
        "Programming Language :: C++",  # NEW
        "Programming Language :: Rust",  # NEW
        "Programming Language :: Go",  # NEW
        
        # Operating System
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",  # NEW: More specific
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",  # NEW
        "Operating System :: Microsoft :: Windows :: Windows 11",  # NEW
        "Operating System :: MacOS",
        
        # Environment - Enhanced
        "Environment :: Console",
        "Environment :: Web Environment", 
        "Environment :: No Input/Output (Daemon)",
        "Environment :: GPU",  # NEW: For ML workloads
        "Environment :: Other Environment",  # NEW
        
        # Natural Language
        "Natural Language :: English",
        "Natural Language :: French",
        
        # Framework
        "Framework :: AsyncIO",  # NEW
        "Framework :: FastAPI",  # NEW
        
        # Typing
        "Typing :: Typed"  # NEW: Indicates type hints support
    ],
    
    # Enhanced keywords for v2.0 discoverability
    keywords=[
        # Core concepts v2.0
        "iln", "iln-v2", "language-unification", "essence-absorption", 
        "multi-language", "champion-cascade", "level-3-architecture",
        "strategic-engines", "modular-programming", "paradigm-fusion",
        
        # New v2.0 features
        "champion-selection", "engine-registry", "essence-processor",
        "performance-benchmarking", "modular-architecture", 
        "intelligent-orchestration", "contextual-optimization",
        
        # Programming languages supported
        "python", "javascript", "typescript", "go", "golang", "rust", 
        "nodejs", "node", "c++", "cpp", "java", "kotlin", "swift",
        
        # New essences v2.0
        "machine-learning", "ml", "data-streaming", "security", 
        "mobile-development", "api-development", "real-time",
        "encryption", "authentication", "cross-platform",
        
        # Programming paradigms
        "concurrency", "async", "await", "memory-safety", "ownership",
        "reactive-programming", "functional-programming", 
        "event-driven", "concurrent-programming", "parallel-processing",
        
        # Architecture patterns
        "microservices", "distributed-systems", "cloud-native", 
        "serverless", "api-integration", "multi-engine", 
        "orchestration", "coordination", "service-mesh",
        
        # Developer experience
        "developer-tools", "productivity", "automation", "code-generation",
        "framework", "library", "sdk", "cli-tools", "devops",
        "continuous-integration", "performance-optimization",
        
        # Application domains
        "web-development", "mobile-development", "ios", "android",
        "ai", "artificial-intelligence", "machine-learning", "ml",
        "data-science", "data-engineering", "backend", "frontend", 
        "full-stack", "game-development", "embedded-systems",
        
        # Business & Enterprise
        "enterprise", "saas", "b2b", "api", "professional", 
        "commercial", "scalable", "high-performance", "production-ready",
        "enterprise-grade", "mission-critical",
        
        # Technology trends
        "cloud-computing", "edge-computing", "iot", "blockchain",
        "quantum-computing", "containers", "kubernetes", "docker",
        "serverless-functions", "microservices-architecture"
    ],
    
    # Package metadata
    platforms=["any"],
    license="MIT",
    
    # Enhanced setup requirements for v2.0
    setup_requires=[
        "wheel>=0.38.0",  # Updated
        "setuptools>=65.0.0"  # Updated for better support
    ],
    
    # Enhanced test configuration
    tests_require=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "pytest-benchmark>=4.0.0",  # NEW
        "pytest-asyncio>=0.21.0"  # NEW
    ],
    test_suite="tests",
    
    # Additional files to include - CORRECTED (no CHANGELOG, no Level 3 docs)
    package_data={
        "": [
            "*.md", "*.txt", "*.yml", "*.yaml", "*.json", "*.toml",
            "LICENSE*", "CONTRIBUTING*", "MANIFESTE*",
            "LEVEL-1.md", "LEVEL-2.md",  # Only public levels
            "*.in"  # Manifesto files
        ],
    },
    
    # Exclude development files from distribution
    exclude_package_data={
        "": [
            "tests/*", "test_*", "*_test.py",
            "docs/*", ".git*", "*.pyc", "__pycache__/*",
            ".pytest_cache/*", ".coverage", "htmlcov/*",
            ".tox/*", ".mypy_cache/*", ".ruff_cache/*",
            "*.log", "*.tmp",
            "LEVEL-3.md", "LEVEL-4.md", "CHANGELOG*"  # Exclude pro features & non-existent files
        ]
    },
    
    # NEW: Project configuration metadata
    project_metadata={
        "version_scheme": "release-branch-semver",
        "release_branch": "main",
        "supported_python_versions": ["3.8", "3.9", "3.10", "3.11", "3.12"],
        "supported_platforms": ["linux", "macos", "windows"],
        "maturity": "beta",
        "stability": "stable"
    }
)

# Enhanced custom commands for v2.0
try:
    from setuptools import Command
    import sys
    
    class DemoCommand(Command):
        """Enhanced command to run ILN v2.0 demo"""
        description = "Run ILN v2.0 interactive demo with new features"
        user_options = [
            ('level=', 'l', 'Demo level to run (1, 2, 3, or all)'),
            ('engine=', 'e', 'Specific engine to demo'),
            ('verbose', 'v', 'Verbose output')
        ]
        
        def initialize_options(self):
            self.level = 'all'
            self.engine = 'auto'
            self.verbose = False
            
        def finalize_options(self):
            if self.level not in ['1', '2', '3', 'all']:
                raise ValueError("Level must be 1, 2, 3, or 'all'")
            
        def run(self):
            try:
                from iln import ILN
                print(f"🌌 Running ILN v2.0 Demo (Level: {self.level}, Engine: {self.engine})")
                iln = ILN()
                
                if self.level == 'all':
                    iln.demo()
                else:
                    # Custom demo for specific level
                    level_int = int(self.level)
                    test_code = "ml!('demo', test) && stream!('data', process)"
                    result = iln.execute(test_code, level=level_int, engine=self.engine)
                    print(f"✅ Level {level_int} Demo Result:", result.metadata)
                    
            except ImportError:
                print("❌ ILN not properly installed. Run: pip install -e .")
                sys.exit(1)
    
    class InfoCommand(Command):
        """Enhanced command to show ILN v2.0 system information"""
        description = "Show ILN v2.0 system information and capabilities"
        user_options = [
            ('format=', 'f', 'Output format (json, yaml, table)'),
            ('engines', None, 'Show available engines'),
            ('essences', None, 'Show supported essences')
        ]
        
        def initialize_options(self):
            self.format = 'json'
            self.engines = False
            self.essences = False
            
        def finalize_options(self):
            if self.format not in ['json', 'yaml', 'table']:
                raise ValueError("Format must be json, yaml, or table")
            
        def run(self):
            try:
                from iln import ILN
                import json
                
                iln = ILN()
                info = iln.get_info()
                
                if self.format == 'json':
                    print(json.dumps(info, indent=2))
                elif self.format == 'table':
                    print("🌌 ILN v2.0 System Information")
                    print(f"Version: {info['version']}")
                    print(f"Engines: {len(info['engines'])}")
                    print(f"Essences: {len(info['supported_essences'])}")
                    print(f"Levels: {info['levels_available']}")
                
                if self.engines:
                    print("\n🔧 Available Engines:")
                    for engine in info['engines']:
                        print(f"  • {engine}")
                        
                if self.essences:
                    print("\n🌟 Supported Essences:")
                    for essence in info['supported_essences']:
                        print(f"  • {essence}")
                        
            except ImportError:
                print("❌ ILN not properly installed. Run: pip install -e .")
                sys.exit(1)
    
    class BenchmarkCommand(Command):
        """NEW: Command to run ILN v2.0 performance benchmarks"""
        description = "Run ILN v2.0 performance benchmarks"
        user_options = [
            ('level=', 'l', 'Benchmark specific level (1, 2, 3, or all)'),
            ('engine=', 'e', 'Benchmark specific engine'),
            ('output=', 'o', 'Output file for results')
        ]
        
        def initialize_options(self):
            self.level = 'all'
            self.engine = 'auto'
            self.output = None
            
        def finalize_options(self):
            pass
            
        def run(self):
            try:
                from iln import ILN
                import json
                
                print("🚀 Running ILN v2.0 Performance Benchmarks...")
                iln = ILN()
                results = iln.benchmark()
                
                if self.output:
                    with open(self.output, 'w') as f:
                        json.dump(results, f, indent=2)
                    print(f"📊 Results saved to: {self.output}")
                else:
                    print(json.dumps(results, indent=2))
                    
            except ImportError:
                print("❌ ILN not properly installed. Run: pip install -e .")
                sys.exit(1)
    
    # Add enhanced custom commands
    setup.cmdclass = {
        'demo': DemoCommand,
        'info': InfoCommand,
        'benchmark': BenchmarkCommand  # NEW
    }
    
except ImportError:
    # If setuptools doesn't support custom commands, skip them
    print("⚠️  Advanced setup commands not available (setuptools version issue)")
    pass

# NEW: Post-installation success message
def post_install_message():
    print("""
🌌 ILN v2.0.0 Installation Complete!

✅ New Features Available:
  • Level 3 Champion Cascade Strategy
  • 7 Strategic Engines (Python, NodeJS, Go, Rust, Java, C++, TypeScript)
  • 12 Critical Essences (ml!, stream!, secure!, mobile!, api!)
  • Enhanced Performance Monitoring

🚀 Quick Start:
  iln --demo                    # Run interactive demo
  iln --list-engines           # Show available engines
  iln --benchmark              # Performance 
