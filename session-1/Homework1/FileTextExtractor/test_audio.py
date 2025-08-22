#!/usr/bin/env python3
"""
Test script for audio extraction functionality
"""

from file_text_extractor import FileTextExtractor

def test_audio():
    print("Testing audio extraction...")
    
    extractor = FileTextExtractor()
    
    # Test the problematic WAV file
    audio_file = './data/ACORD1_ACORD101_CPP-456789123_04072025.wav'
    
    print(f"Processing: {audio_file}")
    result = extractor.extract_text_from_audio(audio_file)
    
    print("\nResult:")
    print("=" * 50)
    print(result)
    print("=" * 50)

if __name__ == "__main__":
    test_audio()
