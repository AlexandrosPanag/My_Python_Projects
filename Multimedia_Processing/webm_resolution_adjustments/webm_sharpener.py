# Code written by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# 12/01/2026
# LICENSE: CC 4.0 BY-NC-SA

#!/usr/bin/env python3
"""
WebM Subtle Sharpener
Applies a very gentle unsharp mask to reduce pixelation without changing resolution.
"""

import subprocess
import sys
import os

def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      stdout=subprocess.DEVNULL, 
                      stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def get_video_info(input_file):
    """Get the original video dimensions."""
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'csv=p=0',
        input_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        width, height = map(int, result.stdout.strip().split(','))
        return width, height
    except subprocess.CalledProcessError:
        print(f"Error: Could not read video information from {input_file}")
        sys.exit(1)

def sharpen_video(input_file, output_file='output.webm'):
    """
    Apply subtle sharpening to a WebM video without changing resolution.
    
    Args:
        input_file: Path to input WebM file
        output_file: Path to output WebM file (default: output.webm)
    """
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    if not check_ffmpeg():
        print("Error: ffmpeg is not installed or not in PATH")
        print("Please install ffmpeg to use this script")
        sys.exit(1)
    
    # Get dimensions to display
    width, height = get_video_info(input_file)
    
    print(f"Resolution: {width}x{height} (unchanged)")
    print(f"Processing '{input_file}'...")
    
    # FFmpeg filter:
    # unsharp with very gentle settings to reduce pixelation
    # - luma_msize: 5x5 matrix (gentle blur radius)
    # - luma_amount: 0.4 (subtle sharpening, just enough to crisp edges)
    # - chroma left at 0.0 (no color sharpening to avoid artifacts)
    filter_complex = "unsharp=5:5:0.4:5:5:0.0"
    
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', filter_complex,
        '-c:v', 'libvpx-vp9',  # VP9 codec for WebM
        '-crf', '23',          # Quality level (lower = better, 15-35 range)
        '-b:v', '0',           # Variable bitrate
        '-c:a', 'copy',        # Copy audio without re-encoding
        '-y',                  # Overwrite output file
        output_file
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"\n✓ Success! Output saved to '{output_file}'")
        
        # Show file sizes
        input_size = os.path.getsize(input_file) / (1024 * 1024)
        output_size = os.path.getsize(output_file) / (1024 * 1024)
        print(f"  Input size: {input_size:.2f} MB")
        print(f"  Output size: {output_size:.2f} MB")
        
    except subprocess.CalledProcessError:
        print("\nError: ffmpeg processing failed")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python webm_sharpen.py input.webm [output.webm]")
        print("\nExample:")
        print("  python webm_sharpen.py input.webm")
        print("  python webm_sharpen.py input.webm sharpened.webm")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.webm'
    
    sharpen_video(input_file, output_file)