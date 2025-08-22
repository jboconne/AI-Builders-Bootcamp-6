#!/usr/bin/env python3
"""
Audio file diagnostics to understand format and content
"""

import os
from pydub import AudioSegment
import wave

def analyze_audio_file(file_path):
    """Analyze audio file properties"""
    print(f"Analyzing: {file_path}")
    print("=" * 60)
    
    if not os.path.exists(file_path):
        print("❌ File does not exist")
        return
    
    # Get file info
    file_size = os.path.getsize(file_path)
    print(f"File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    
    try:
        # Try to load with pydub
        audio = AudioSegment.from_file(file_path)
        print(f"✅ Pydub loaded successfully")
        print(f"Duration: {len(audio)} ms ({len(audio)/1000:.1f} seconds)")
        print(f"Channels: {audio.channels}")
        print(f"Sample width: {audio.sample_width} bytes")
        print(f"Frame rate: {audio.frame_rate} Hz")
        print(f"Max amplitude: {audio.max}")
        print(f"Average amplitude: {audio.dBFS} dBFS")
        
        # Check if audio has content
        if audio.max == 0:
            print("⚠️  WARNING: Audio appears to be silent (max amplitude = 0)")
        elif audio.dBFS < -50:
            print("⚠️  WARNING: Audio is very quiet (dBFS < -50)")
        
    except Exception as e:
        print(f"❌ Pydub failed: {e}")
    
    try:
        # Try to open as WAV file
        with wave.open(file_path, 'rb') as wav_file:
            print(f"✅ WAV file opened successfully")
            print(f"WAV channels: {wav_file.getnchannels()}")
            print(f"WAV sample width: {wav_file.getsampwidth()} bytes")
            print(f"WAV frame rate: {wav_file.getframerate()} Hz")
            print(f"WAV frames: {wav_file.getnframes()}")
            print(f"WAV parameters: {wav_file.getparams()}")
            
    except Exception as e:
        print(f"❌ WAV file failed: {e}")
    
    print("=" * 60)

if __name__ == "__main__":
    audio_file = './data/ACORD1_ACORD101_CPP-456789123_04072025.wav'
    analyze_audio_file(audio_file)
