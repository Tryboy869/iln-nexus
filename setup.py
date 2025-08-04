#!/usr/bin/env python3
"""
Setup configuration for iln-core v2.0.0 - ROBUST VERSION
"""

from setuptools import setup, find_packages
from pathlib import Path

# ROBUST version reading - multiple fallbacks
def get_version():
    try:
        # Try reading from iln.py directly
        main_file = Path(__file__).parent / "iln.py"
        if main_file.exists():
            content = main_file.read_text()
            import re
            match = re.search(r'__version__ = ["\']([^"\']*)["\']', content)
            if match:
                return match.group(1)
    except:
        pass
    
    # Fallback to fixed version
    return "2.0.0"

# ROBUST description - with fallback
def get_long_description():
    try:
        readme_file = Path(__file__).parent / "README.md"
        if readme_file.exists():
            return readme_file.read_text(encoding="utf-8")
    except:
        pass
    
    # Fallback description
    return """
🌌 ILN v2.0.0 - Revolutionary Language Unification System

Stop learning 10+ programming languages. Master ONE language that absorbs the essence of ALL others.

New in v2.0:
- 7 Strategic Engines (Python, NodeJS, Go, Rust, Java, C++, TypeScript)
- 12 Critical Essences (ml!, stream!, secure!, mobile!, api!)
- Level 3 Champion Cascade Strategy
- Enhanced Performance Monitoring

Visit: https://github.com/Tryboy869/iln-nexus
"""

# ROBUST requirements - minimal dependencies
def get_requirements():
    try:
        requirements_file = Path(__file__).parent / "requirements.txt"
        if requirements_file.exists():
            return [
                line.strip() 
                for line in requirements_file.read_text().splitlines() 
                if line.strip() and not line.startswith("#")
            ]
    except:
        pass
    
    # Fallback minimal requirements
    return ["requests>=2.28.0"]

setup(
    # Basic info - FIXED VALUES (no functions that can fail)
    name="iln-core",
    version="2.0.0",  # HARD-CODED to avoid failures
    author="Anzize Daouda",
    author_email="nexusstudio100@gmail.com",
    
    description="🌌 ILN v2.0 - Revolutionary Language Unification System",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    
    url="https://github.com/Tryboy869/iln-nexus",
    
    # Package structure - ROBUST
    packages=find_packages() if find_packages() else [],
    py_modules=["iln"] if not find_packages() else [],
    
    python_requires=">=3.8",
    
    # Dependencies - MINIMAL to avoid failures  
    install_requires=get_requirements(),
    
    # Entry points - SIMPLE
    entry_points={
        "console_scripts": [
            "iln=iln:main",
        ],
    },
    
    # Classifiers - ESSENTIAL ONLY
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
    ],
    
    keywords="iln language-unification multi-language programming",
    license="MIT",
    
    # REMOVE ALL COMPLEX FEATURES that might fail
    # No custom commands, no complex package_data, etc.
)
```

## SOLUTION 2 - DIAGNOSTIC SCRIPT

Avant de modifier, ajoute ce script de diagnostic :

```python
# diagnostic_setup.py - Run this first
import sys
from pathlib import Path

def diagnose_setup():
    print("🔍 Diagnosing setup.py issues...")
    
    # Check file structure
    files = ["iln.py", "README.md", "requirements.txt", "setup.py"]
    for file in files:
        path = Path(file)
        status = "✅ EXISTS" if path.exists() else "❌ MISSING"
        print(f"  {file}: {status}")
    
    # Check iln.py for version
    try:
        if Path("iln.py").exists():
            content = Path("iln.py").read_text()
            if "__version__" in content:
                print("✅ __version__ found in iln.py")
            else:
                print("❌ __version__ NOT found in iln.py")
    except Exception as e:
        print(f"❌ Error reading iln.py: {e}")
    
    # Check imports
    try:
        from setuptools import setup, find_packages
        print("✅ setuptools imports OK")
    except Exception as e:
        print(f"❌ setuptools import error: {e}")

if __name__ == "__main__":
    diagnose_setup()