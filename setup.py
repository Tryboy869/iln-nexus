#!/usr/bin/env python3
"""
Setup configuration for iln-core v2.0.0
🌌 ILN - Informatique Language Nexus
GITHUB RELEASES OPTIMIZED - No PyPI complexities
"""

from setuptools import setup, find_packages
from pathlib import Path
import re

def get_version():
    """Read version from iln.py"""
    try:
        iln_file = Path(__file__).parent / "iln.py"
        if iln_file.exists():
            content = iln_file.read_text(encoding='utf-8')
            match = re.search(r'^__version__ = ["\']([^"\']*)["\']', content, re.M)
            if match:
                return match.group(1)
    except Exception:
        pass
    return "2.0.0"  # Fallback

def get_long_description():
    """Read README.md if available"""
    try:
        readme_file = Path(__file__).parent / "README.md"
        if readme_file.exists():
            return readme_file.read_text(encoding="utf-8")
    except Exception:
        pass
    
    return """
🌌 ILN v2.0.0 - Revolutionary Language Unification System

New in v2.0:
- Level 3 Champion Cascade Strategy (Pro Feature)
- 7 Strategic Engines (Python, NodeJS, Go, Rust, Java, C++, TypeScript)
- 12 Critical Essences including ml!, stream!, secure!, mobile!, api!
- Modular Architecture for Future Extensions

Community Edition includes Levels 1-2 (Open Source)
Pro Features (Levels 3-4) available at: nexusstudio100@gmail.com

Install from GitHub: pip install git+https://github.com/Tryboy869/iln-nexus.git@v2.0.0
"""

def get_requirements():
    """Read requirements.txt if available"""
    try:
        req_file = Path(__file__).parent / "requirements.txt"
        if req_file.exists():
            return [
                line.strip() 
                for line in req_file.read_text().splitlines() 
                if line.strip() and not line.startswith("#")
            ]
    except Exception:
        pass
    
    return ["requests>=2.28.0"]  # Minimal fallback

setup(
    # Basic package info
    name="iln-core",
    version=get_version(),
    author="Anzize Daouda",
    author_email="nexusstudio100@gmail.com",
    
    # Package description
    description="🌌 ILN v2.0 - Revolutionary Language Unification System. GitHub Releases.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    
    # GitHub-focused URLs
    url="https://github.com/Tryboy869/iln-nexus",
    download_url="https://github.com/Tryboy869/iln-nexus/releases",
    project_urls={
        "Homepage": "https://github.com/Tryboy869/iln-nexus",
        "Source Code": "https://github.com/Tryboy869/iln-nexus",
        "Bug Tracker": "https://github.com/Tryboy869/iln-nexus/issues",
        "Releases": "https://github.com/Tryboy869/iln-nexus/releases",
        "Documentation": "https://github.com/Tryboy869/iln-nexus/blob/main/README.md",
        
        # Live demos
        "AI Web Navigator Main": "https://ai-web-navigator-j5kp.onrender.com/?#demo",
        "AI Web Navigator Demo": "https://ai-web-navigator-demo-8hxj.onrender.com/",
        "WebPilot API Demo": "https://webpilot-api.onrender.com/",
        
        # Contact & Pro
        "Get Pro": "mailto:nexusstudio100@gmail.com?subject=ILN%20Pro%20Access",
        "Contact": "mailto:nexusstudio100@gmail.com"
    },
    
    # Package structure - GitHub install optimized
    py_modules=["iln"],  # Single module for easy GitHub install
    include_package_data=True,
    zip_safe=False,
    
    # Python version requirements
    python_requires=">=3.8",
    
    # Dependencies - minimal for GitHub installs
    install_requires=get_requirements(),
    
    # Entry points
    entry_points={
        "console_scripts": [
            "iln=iln:main",
            "iln-demo=iln:main",
        ],
    },
    
    # GitHub-friendly classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Operating System :: OS Independent",
    ],
    
    # Keywords for GitHub discovery
    keywords=[
        "iln", "language-unification", "multi-language", "github-package",
        "python", "javascript", "go", "rust", "java", "cpp", "typescript",
        "essence-absorption", "champion-cascade", "programming-revolution"
    ],
    
    # License
    license="MIT",
    
    # GitHub releases metadata
    platforms=["any"],
    
    # Simplified package data for GitHub
    package_data={
        "": ["*.md", "*.txt", "*.in", "LICENSE*"]
    },
)

# GitHub-focused post-install message
if __name__ == "__main__":
    print("""
🌌 ILN v2.0.0 - GitHub Release Package

✅ Installation from GitHub:
  pip install git+https://github.com/Tryboy869/iln-nexus.git@v2.0.0

🚀 Quick Test:
  python -c "from iln import ILN; ILN().demo()"

📧 Pro Features:
  nexusstudio100@gmail.com
""")