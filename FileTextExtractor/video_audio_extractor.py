#!/usr/bin/env python3
"""
Video Audio Extractor - Extract text from videos using audio instead of OCR
This bypasses the need for Tesseract installation
"""

import os
from pydub import AudioSegment
import tempfile
from file_text_extractor import FileTextExtractor

def extract_audio_from_video(video_path, output_dir="./extracted_audio"):
    """
    Extract audio from video files and save as WAV
    """
    print(f"🎬 Extracting audio from: {os.path.basename(video_path)}")
    print("=" * 60)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Load video and extract audio
        video = AudioSegment.from_file(video_path)
        
        # Get audio properties
        duration = len(video) / 1000
        channels = video.channels
        sample_rate = video.frame_rate
        
        print(f"Audio duration: {duration:.1f} seconds")
        print(f"Audio channels: {channels}")
        print(f"Sample rate: {sample_rate} Hz")
        
        # Create output filename
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        audio_file = os.path.join(output_dir, f"{base_name}_audio.wav")
        
        # Export audio as WAV
        print("Exporting audio...")
        video.export(
            audio_file,
            format='wav',
            parameters=[
                '-ar', '16000',      # 16kHz sample rate
                '-ac', '1',          # Mono channel
                '-f', 'wav',         # WAV format
                '-acodec', 'pcm_s16le'  # PCM 16-bit
            ]
        )
        
        print(f"✅ Audio extracted to: {audio_file}")
        return audio_file
        
    except Exception as e:
        print(f"❌ Error extracting audio: {e}")
        return None

def process_video_with_audio_extraction(video_path):
    """
    Process video by extracting audio and using speech recognition
    """
    print("🎥 Video Audio Text Extractor")
    print("=" * 60)
    
    # Step 1: Extract audio
    print("📂 Step 1: Extracting audio from video...")
    audio_file = extract_audio_from_video(video_path)
    
    if not audio_file:
        return "Failed to extract audio from video"
    
    # Step 2: Check if audio is too long
    print(f"\n🔍 Step 2: Analyzing audio length...")
    try:
        audio = AudioSegment.from_file(audio_file)
        duration_seconds = len(audio) / 1000
        
        if duration_seconds > 300:  # 5 minutes
            print(f"⚠️  Audio is {duration_seconds:.1f} seconds long (exceeds 5-minute limit)")
            print("Splitting audio into segments...")
            
            # Use the audio splitter we created earlier
            from audio_splitter import split_audio_file
            segments = split_audio_file(audio_file, "./video_audio_segments")
            
            if segments:
                print(f"✅ Created {len(segments)} audio segments")
                
                # Process each segment
                print(f"\n📝 Step 3: Processing audio segments...")
                extractor = FileTextExtractor()
                all_results = []
                
                for i, segment_path in enumerate(segments, 1):
                    print(f"\n--- Processing Segment {i}/{len(segments)} ---")
                    result = extractor.extract_text_from_audio(segment_path)
                    all_results.append({
                        'segment': i,
                        'text': result
                    })
                    print(f"Result: {result[:100]}..." if len(result) > 100 else f"Result: {result}")
                
                # Combine results
                combined_text = f"VIDEO AUDIO TEXT EXTRACTION RESULTS\n"
                combined_text += f"Original video: {os.path.basename(video_path)}\n"
                combined_text += f"Audio segments: {len(segments)}\n"
                combined_text += "=" * 60 + "\n\n"
                
                for result in all_results:
                    combined_text += f"SEGMENT {result['segment']}\n"
                    combined_text += "-" * 40 + "\n"
                    combined_text += f"{result['text']}\n\n"
                
                # Save results
                output_file = f"video_audio_results_{os.path.splitext(os.path.basename(video_path))[0]}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(combined_text)
                
                print(f"\n✅ Combined results saved to: {output_file}")
                return combined_text
                
        else:
            # Process single audio file
            print(f"✅ Audio is {duration_seconds:.1f} seconds (within limits)")
            print(f"\n📝 Step 3: Processing audio with speech recognition...")
            
            extractor = FileTextExtractor()
            result = extractor.extract_text_from_audio(audio_file)
            
            # Save result
            output_file = f"video_audio_result_{os.path.splitext(os.path.basename(video_path))[0]}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"VIDEO AUDIO TEXT EXTRACTION RESULT\n")
                f.write(f"Original video: {os.path.basename(video_path)}\n")
                f.write("=" * 50 + "\n\n")
                f.write(result)
            
            print(f"✅ Result saved to: {output_file}")
            return result
            
    except Exception as e:
        return f"Error processing video audio: {str(e)}"

def main():
    """Main function to process videos"""
    print("🎥 Video Audio Text Extractor")
    print("Extracts text from videos using audio instead of OCR")
    print("=" * 60)
    
    # Find video files
    video_files = []
    for root, dirs, files in os.walk('./data'):
        for file in files:
            if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                video_files.append(os.path.join(root, file))
    
    if not video_files:
        print("❌ No video files found in data directory")
        return
    
    print(f"Found {len(video_files)} video file(s):")
    for i, video_file in enumerate(video_files, 1):
        print(f"  {i}. {os.path.basename(video_file)}")
    
    # Process first video file
    if video_files:
        print(f"\n🎬 Processing: {os.path.basename(video_files[0])}")
        result = process_video_with_audio_extraction(video_files[0])
        
        print(f"\n📊 FINAL RESULT:")
        print("=" * 60)
        print(result)

if __name__ == "__main__":
    main()
