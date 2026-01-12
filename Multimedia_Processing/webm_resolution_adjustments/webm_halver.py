# Code written by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# 12/01/2026
# LICENSE: CC 4.0 BY-NC-SA

#!/usr/bin/env python3
"""
WebM Resolution Halver with Subtle Sharpening
Halves the resolution of a WebM video and applies a gentle unsharp mask.
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

def halve_resolution(input_file, output_file='output.webm'):
    """
    Halve the resolution of a WebM video with subtle sharpening.
    
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
    
    # Get original dimensions
    orig_width, orig_height = get_video_info(input_file)
    new_width = orig_width // 2
    new_height = orig_height // 2
    
    print(f"Original resolution: {orig_width}x{orig_height}")
    print(f"New resolution: {new_width}x{new_height}")
    print(f"Processing '{input_file}'...")
    
    # FFmpeg filter chain:
    # 1. scale: Lanczos scaling (high quality) to halve resolution
    # 2. unsharp: Very subtle sharpening (luma only)
    #    - luma_msize_x/y: 5x5 matrix (small)
    #    - luma_amount: 0.3 (very subtle, range is -2 to 5)
    filter_complex = (
        f"scale={new_width}:{new_height}:flags=lanczos,"
        f"unsharp=5:5:0.3:5:5:0.0"
    )
    
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', filter_complex,
        '-c:v', 'libvpx-vp9',  # VP9 codec for WebM
        '-crf', '23',          # Quality level (lower = better, 15-35 range)
        '-b:v', '0',           # Variable bitrate
        '-c:a', 'libopus',     # Opus audio codec
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
        print("Usage: python webm_halver.py input.webm [output.webm]")
        print("\nExample:")
        print("  python webm_halver.py input.webm")
        print("  python webm_halver.py input.webm output.webm")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.webm'
    
    halve_resolution(input_file, output_file)