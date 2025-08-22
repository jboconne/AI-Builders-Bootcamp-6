#!/usr/bin/env python3
"""
Video file diagnostics to identify codec and processing issues
"""

import os
import cv2
from pydub import AudioSegment

def analyze_video_file(file_path):
    """Analyze video file properties and identify potential issues"""
    print(f"🎬 Analyzing video: {file_path}")
    print("=" * 60)
    
    if not os.path.exists(file_path):
        print("❌ File does not exist")
        return
    
    # Get file info
    file_size = os.path.getsize(file_path)
    file_ext = os.path.splitext(file_path)[1].lower()
    
    print(f"File size: {file_size / (1024*1024):.1f} MB")
    print(f"Format: {file_ext}")
    
    # Try OpenCV
    print("\n📹 OpenCV Analysis:")
    try:
        cap = cv2.VideoCapture(file_path)
        
        if cap.isOpened():
            print("✅ OpenCV can open the video")
            
            # Get video properties
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            duration = total_frames / fps if fps > 0 else 0
            
            print(f"  - Total frames: {total_frames}")
            print(f"  - FPS: {fps:.1f}")
            print(f"  - Resolution: {width}x{height}")
            print(f"  - Duration: {duration:.1f} seconds")
            
            # Try to read first frame
            ret, frame = cap.read()
            if ret:
                print("✅ First frame read successfully")
                print(f"  - Frame shape: {frame.shape}")
            else:
                print("❌ Could not read first frame")
            
            cap.release()
            
        else:
            print("❌ OpenCV cannot open the video")
            print("  This usually indicates a codec issue")
            
    except Exception as e:
        print(f"❌ OpenCV error: {e}")
    
    # Try pydub for audio analysis
    print("\n🎵 Audio Analysis:")
    try:
        audio = AudioSegment.from_file(file_path)
        print("✅ Pydub can read audio from video")
        print(f"  - Audio duration: {len(audio) / 1000:.1f} seconds")
        print(f"  - Audio channels: {audio.channels}")
        print(f"  - Audio sample rate: {audio.frame_rate} Hz")
    except Exception as e:
        print(f"❌ Pydub audio error: {e}")
    
    # Codec suggestions
    print("\n💡 Codec Solutions:")
    if file_ext == '.mp4':
        print("  - MP4 files often need H.264 codec support")
        print("  - Try installing additional codecs:")
        print("    * K-Lite Codec Pack (Windows)")
        print("    * LAV Filters")
        print("    * FFmpeg")
    elif file_ext == '.avi':
        print("  - AVI files may need DivX, XviD, or other codecs")
    elif file_ext == '.mov':
        print("  - MOV files need QuickTime codecs")
    
    print("\n🛠️  Alternative Solutions:")
    print("  1. Convert video to a different format (e.g., MP4 with H.264)")
    print("  2. Install additional video codecs")
    print("  3. Use FFmpeg to extract frames manually")
    print("  4. Try different video processing libraries")

def test_video_processing(file_path):
    """Test if video can be processed for text extraction"""
    print(f"\n🧪 Testing video processing for text extraction...")
    print("=" * 60)
    
    try:
        from file_text_extractor import FileTextExtractor
        extractor = FileTextExtractor()
        
        print("Testing video text extraction...")
        result = extractor.extract_text_from_video(file_path)
        
        print("\nResult:")
        print("-" * 40)
        print(result)
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    # Test with available video files
    video_files = [
        './data/TestimonialShort.mp4',
        './data/video/Testimonial.mp4'
    ]
    
    for video_file in video_files:
        if os.path.exists(video_file):
            analyze_video_file(video_file)
            test_video_processing(video_file)
            break
    else:
        print("No video files found in data directory")
        print("Available files:")
        for root, dirs, files in os.walk('./data'):
            for file in files:
                if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                    print(f"  - {os.path.join(root, file)}")
