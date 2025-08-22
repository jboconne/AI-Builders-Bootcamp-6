#!/usr/bin/env python3
"""
Dependency Installation Script for File Text Extractor
This script helps install dependencies step by step to avoid build issues.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors gracefully"""
    print(f"\n{'='*60}")
    print(f"Installing: {description}")
    print(f"Command: {command}")
    print('='*60)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Success!")
        if result.stdout:
            print("Output:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed with error code {e.returncode}")
        if e.stdout:
            print("Stdout:", e.stdout)
        if e.stderr:
            print("Stderr:", e.stderr)
        return False

def main():
    print("File Text Extractor - Dependency Installation")
    print("This script will install dependencies step by step to avoid build issues.")
    
    # Check if pip is available
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("❌ pip is not available. Please install pip first.")
        return
    
    # List of packages to install (in order of dependency)
    packages = [
        ("numpy==1.24.3", "NumPy - Numerical computing library"),
        ("Pillow==10.0.1", "Pillow - Image processing library"),
        ("PyPDF2==3.0.1", "PyPDF2 - PDF processing library"),
        ("pdfplumber==0.9.0", "pdfplumber - PDF text extraction (alternative to PyMuPDF)"),
        ("opencv-python==4.8.1.78", "OpenCV - Computer vision library"),
        ("pytesseract==0.3.10", "pytesseract - OCR library"),
        ("pydub==0.25.1", "pydub - Audio processing library"),
        ("SpeechRecognition==3.10.0", "SpeechRecognition - Speech recognition library"),
        ("pyaudio==0.2.11", "pyaudio - Audio I/O library")
    ]
    
    failed_packages = []
    
    for package, description in packages:
        success = run_command(f"{sys.executable} -m pip install {package}", description)
        if not success:
            failed_packages.append(package)
            print(f"⚠️  Failed to install {package}. Continuing with other packages...")
    
    print(f"\n{'='*60}")
    print("Installation Summary")
    print('='*60)
    
    if failed_packages:
        print(f"❌ Failed packages ({len(failed_packages)}):")
        for package in failed_packages:
            print(f"  - {package}")
        print("\n💡 Suggestions:")
        print("  - Try installing failed packages individually")
        print("  - Some packages may require additional system dependencies")
        print("  - For pyaudio, you might need to install portaudio first")
    else:
        print("✅ All packages installed successfully!")
    
    print(f"\n📋 Total packages: {len(packages)}")
    print(f"✅ Successful: {len(packages) - len(failed_packages)}")
    print(f"❌ Failed: {len(failed_packages)}")

if __name__ == "__main__":
    main()
