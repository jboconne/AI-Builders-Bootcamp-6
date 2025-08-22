#!/usr/bin/env python3
"""
Comprehensive long audio processor for file text extraction
"""

import os
from file_text_extractor import FileTextExtractor
from audio_splitter import split_audio_file

def process_long_audio_complete(input_file, output_dir="./audio_segments"):
    """
    Complete solution for processing long audio files:
    1. Split into segments
    2. Process each segment
    3. Combine results
    """
    print("🎵 Long Audio File Processor")
    print("=" * 60)
    
    # Step 1: Split the audio file
    print("📂 Step 1: Splitting audio file into segments...")
    segments = split_audio_file(input_file, output_dir)
    
    if not segments:
        print("❌ Failed to split audio file")
        return None
    
    # Step 2: Process each segment
    print(f"\n🔍 Step 2: Processing {len(segments)} segments...")
    extractor = FileTextExtractor()
    all_results = []
    
    for i, segment_path in enumerate(segments, 1):
        print(f"\n--- Processing Segment {i}/{len(segments)} ---")
        print(f"File: {os.path.basename(segment_path)}")
        
        try:
            result = extractor.extract_text_from_audio(segment_path)
            all_results.append({
                'segment': i,
                'file': os.path.basename(segment_path),
                'text': result
            })
            
            # Show preview of result
            if len(result) > 100:
                preview = result[:100] + "..."
            else:
                preview = result
            print(f"Result: {preview}")
            
        except Exception as e:
            error_msg = f"Error processing segment {i}: {str(e)}"
            print(f"❌ {error_msg}")
            all_results.append({
                'segment': i,
                'file': os.path.basename(segment_path),
                'text': error_msg
            })
    
    # Step 3: Combine and save results
    print(f"\n📝 Step 3: Combining results...")
    
    # Create combined text
    combined_text = f"LONG AUDIO FILE PROCESSING RESULTS\n"
    combined_text += f"Original file: {os.path.basename(input_file)}\n"
    combined_text += f"Total segments: {len(segments)}\n"
    combined_text += "=" * 60 + "\n\n"
    
    for result in all_results:
        combined_text += f"SEGMENT {result['segment']}\n"
        combined_text += f"File: {result['file']}\n"
        combined_text += "-" * 40 + "\n"
        combined_text += f"{result['text']}\n\n"
    
    # Save combined results
    output_file = f"combined_audio_results_{os.path.splitext(os.path.basename(input_file))[0]}.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_text)
    
    print(f"✅ Combined results saved to: {output_file}")
    
    # Summary
    print(f"\n📊 PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Original file: {os.path.basename(input_file)}")
    print(f"Segments created: {len(segments)}")
    print(f"Segments processed: {len(all_results)}")
    print(f"Results saved to: {output_file}")
    
    # Show sample of combined text
    print(f"\n📖 Sample of combined text:")
    print("-" * 40)
    if combined_text:
        lines = combined_text.split('\n')[:10]
        for line in lines:
            print(line)
        if len(combined_text.split('\n')) > 10:
            print("...")
    
    return all_results

if __name__ == "__main__":
    # Process the long audio file
    input_audio = './data/ACORD1_ACORD101_CPP-456789123_04072025.wav'
    results = process_long_audio_complete(input_audio)
    
    if results:
        print(f"\n🎉 Audio processing completed successfully!")
        print(f"Check the output file for complete results.")
    else:
        print(f"\n❌ Audio processing failed.")
