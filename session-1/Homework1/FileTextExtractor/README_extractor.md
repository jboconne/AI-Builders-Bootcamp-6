# File Text Extractor

A Python program that extracts text from various file formats without using AI/LLM automation. The program automatically detects file types and extracts text using appropriate libraries for each format.

## Supported File Types

- **Audio Files**: WAV, MP3, MPEG
- **Text Files**: TXT (with multiple encoding support)
- **PDF Files**: PDF documents
- **Video Files**: MP4, AVI, MOV (using OCR on frames)

## Features

- Automatic file type detection based on extension and MIME type
- Speech recognition for audio files
- OCR (Optical Character Recognition) for video frames
- PDF text extraction
- Plain text file reading with encoding detection
- Results display and optional file output
- Error handling for unsupported or corrupted files

## Installation

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Tesseract OCR** installed for video text extraction

### Install Tesseract OCR

**Windows:**
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install and add to PATH

**macOS:**
```bash
brew install tesseract
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install tesseract-ocr
```

### Install Python Dependencies

**Option 1: Use the installation script (Recommended for Windows)**
```bash
python install_dependencies.py
```

**Option 2: Install from requirements file**
```bash
pip install -r requirements_extractor_alternative.txt
```

**Option 3: Install individually**
```bash
pip install SpeechRecognition pydub PyPDF2 pdfplumber opencv-python pytesseract Pillow pyaudio numpy
```

**Note for Windows Users:**
- If you encounter build errors with PyMuPDF, use the alternative requirements file
- The alternative version uses `pdfplumber` instead of `PyMuPDF` for better Windows compatibility
- Some packages may require additional system dependencies (see Troubleshooting section)

## Usage

### Basic Usage

1. Run the program:
```bash
python file_text_extractor.py
```

2. Enter the folder path containing your files when prompted
3. Wait for processing to complete
4. View results in the console
5. Optionally save results to a file

### Program Structure

The program consists of a `FileTextExtractor` class with methods for:

- `detect_file_type()`: Automatically determines file type
- `extract_text_from_audio()`: Speech recognition for audio files
- `extract_text_from_text_file()`: Plain text extraction
- `extract_text_from_pdf()`: PDF text extraction
- `extract_text_from_video()`: OCR on video frames
- `process_folder()`: Batch processing of multiple files
- `display_results()`: Formatted output display

### Example Output

```
================================================================================
FILE TEXT EXTRACTION RESULTS
================================================================================

File 1: sample_audio.wav
Type: AUDIO
----------------------------------------
Extracted Text:
This is the transcribed text from the audio file.
================================================================================

File 2: document.pdf
Type: PDF
----------------------------------------
Extracted Text:
This is the text content extracted from the PDF document...
================================================================================
```

## How It Works

### Audio Files
- Converts non-WAV formats to WAV using pydub
- Uses Google's Speech Recognition API (requires internet)
- Handles various audio formats and quality levels

### Text Files
- Attempts UTF-8 encoding first
- Falls back to Latin-1 encoding if needed
- Handles various text encodings gracefully

### PDF Files
- Uses pdfplumber for robust text extraction (Windows-friendly alternative to PyMuPDF)
- Processes all pages in the document
- Maintains text formatting where possible
- Falls back to PyPDF2 for basic PDF support if needed

### Video Files
- Extracts frames at regular intervals (every 30th frame)
- Converts frames to images for OCR processing
- Uses Tesseract OCR to extract text from frames
- Combines text from multiple frames

## Error Handling

The program includes comprehensive error handling for:
- Unsupported file types
- Corrupted or unreadable files
- Network issues (for speech recognition)
- Missing dependencies
- File permission issues

## Limitations

- **Audio**: Requires internet connection for Google Speech Recognition
- **Video**: OCR accuracy depends on video quality and text clarity
- **Large Files**: Processing time increases with file size
- **Language**: Speech recognition works best with English

## Troubleshooting

### Common Installation Issues

1. **PyMuPDF Build Errors (Windows)**
   - **Problem**: `metadata-generation-failed` or Visual Studio build errors
   - **Solution**: Use `requirements_extractor_alternative.txt` instead, which uses `pdfplumber`
   - **Alternative**: Run `python install_dependencies.py` for step-by-step installation

2. **Tesseract not found**
   - **Problem**: `pytesseract.pytesseract.TesseractNotFoundError`
   - **Solution**: Install Tesseract OCR and ensure it's in your system PATH
   - **Windows**: Download from https://github.com/UB-Mannheim/tesseract/wiki
   - **Linux**: `sudo apt-get install tesseract-ocr`

3. **Audio conversion errors**
   - **Problem**: `pydub.exceptions.CouldntDecodeError`
   - **Solution**: Install ffmpeg (required by pydub for audio conversion)
   - **Windows**: Download from https://ffmpeg.org/download.html
   - **Linux**: `sudo apt-get install ffmpeg`

4. **Permission errors**
   - **Problem**: `PermissionError: [Errno 13] Permission denied`
   - **Solution**: Ensure read access to target folder and files

5. **Memory issues with large files**
   - **Problem**: `MemoryError` or slow processing
   - **Solution**: Process files individually or increase system RAM

### Dependency-Specific Issues

- **pyaudio**: May require additional system libraries on Linux
- **opencv-python**: Large download, consider `opencv-python-headless` for servers
- **pdfplumber**: More Windows-friendly alternative to PyMuPDF
- **PyPDF2**: Basic PDF support, may not handle complex layouts

### Windows-Specific Solutions

1. **Use the installation script**: `python install_dependencies.py`
2. **Install pre-compiled wheels**: Avoid packages that require building from source
3. **Use alternative requirements**: `pip install -r requirements_extractor_alternative.txt`
4. **Install Visual Studio Build Tools**: Only if you need to build packages from source

### Testing Your Installation

After installation, test with:
```python
import pdfplumber
import cv2
import pytesseract
import speech_recognition
import pydub

print("All dependencies imported successfully!")
```

## Customization

You can modify the program to:
- Add support for additional file types
- Change the frame sampling rate for videos
- Implement different speech recognition engines
- Add batch processing options
- Customize output formats

## License

This program is provided as-is for educational and personal use.
