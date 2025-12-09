# Alexandros Panagiotakopoulos
# Date: 08-12-2025
# LICENSE: CC4-BY-NC-SA 4.0


#winget install ffmpeg
# example usage:
#python video_resizer.py input.webm output.webm 1.42 0.3

#!/usr/bin/env python3
"""
Video Resizer and Zoom Tool
Resizes videos to 464x864 with a zoom effect and outputs in WebM format.
Requires: ffmpeg installed on system (no Python packages needed!)
"""

import subprocess
import sys
import json
from pathlib import Path


def get_video_info(input_path: str) -> dict:
    """Get video information using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_streams',
        input_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        # Find video stream
        for stream in data['streams']:
            if stream['codec_type'] == 'video':
                return {
                    'width': int(stream['width']),
                    'height': int(stream['height'])
                }
        
        raise ValueError("No video stream found")
        
    except subprocess.CalledProcessError as e:
        print(f"Error probing video: {e.stderr}", file=sys.stderr)
        raise
    except json.JSONDecodeError:
        print("Error parsing video information", file=sys.stderr)
        raise


def resize_and_zoom_video(input_path: str, output_path: str, zoom_factor: float = 1.5, y_offset: float = 0.0, scale: float = 1.0):
    """
    Resize and zoom a video to 464x864 in WebM format.
    
    Args:
        input_path: Path to input video file
        output_path: Path to output WebM file
        zoom_factor: Zoom multiplier (1.5 = 50% zoom in, default)
        y_offset: Vertical offset ratio (-1.0 to 1.0, 0 = center, negative = up, positive = down)
        scale: Final output scale (0.5 = 50% smaller, 0.8 = 20% smaller, default = 1.0)
    """
    target_width = 464
    target_height = 864
    
    try:
        # Get input video information
        video_info = get_video_info(input_path)
        input_width = video_info['width']
        input_height = video_info['height']
        
        print(f"Input: {input_width}x{input_height}")
        print(f"Output: {target_width}x{target_height}")
        print(f"Zoom factor: {zoom_factor}x")
        if scale != 1.0:
            print(f"Final scale: {scale * 100:.0f}%")
        
        # Calculate dimensions for zoom
        zoom_width = int(target_width * zoom_factor)
        zoom_height = int(target_height * zoom_factor)
        
        # Calculate crop offsets
        # Center horizontally
        crop_x = (zoom_width - target_width) // 2
        
        # Apply vertical offset
        max_y_offset = (zoom_height - target_height) // 2
        crop_y = max_y_offset + int(max_y_offset * y_offset)
        
        # Clamp crop_y to valid range
        crop_y = max(0, min(crop_y, zoom_height - target_height))
        
        # Apply final scale if specified
        if scale != 1.0:
            final_width = int(target_width * scale)
            final_height = int(target_height * scale)
            vf = f"scale={zoom_width}:{zoom_height},crop={target_width}:{target_height}:{crop_x}:{crop_y},scale={final_width}:{final_height}"
        else:
            vf = f"scale={zoom_width}:{zoom_height},crop={target_width}:{target_height}:{crop_x}:{crop_y}"
        
        # Build ffmpeg command
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', vf,
            '-c:v', 'libvpx-vp9',      # VP9 codec for WebM
            '-crf', '30',               # Quality (lower = better, 23-32 recommended)
            '-b:v', '1M',               # Video bitrate
            '-c:a', 'libopus',          # Opus audio codec
            '-b:a', '128k',             # Audio bitrate
            '-y',                       # Overwrite output file
            output_path
        ]
        
        print("\nProcessing video...")
        print(f"Running: {' '.join(cmd)}\n")
        
        # Run ffmpeg
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"FFmpeg error:\n{result.stderr}", file=sys.stderr)
            sys.exit(1)
        
        print(f"✓ Successfully created: {output_path}")
        
    except FileNotFoundError:
        print("\nError: ffmpeg not found. Please install ffmpeg:", file=sys.stderr)
        print("  Windows: Download from https://ffmpeg.org/download.html", file=sys.stderr)
        print("  Or use: winget install ffmpeg", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function with command-line interface."""
    if len(sys.argv) < 2:
        print("Usage: python video_resizer.py <input_video.webm> [output_video.webm] [zoom_factor] [y_offset] [--scale factor]")
        print("\nExample:")
        print("  python video_resizer.py input.webm")
        print("  python video_resizer.py input.webm output.webm 1.8")
        print("  python video_resizer.py input.webm output.webm 1.8 -0.2")
        print("  python video_resizer.py input.webm output.webm 1.42 0.1 --scale 0.8")
        print("\nDefault zoom factor: 1.5 (50% zoom in)")
        print("y_offset: -1.0 (top) to 1.0 (bottom), 0 = center, default = 0")
        print("--scale: Final output scale (0.5-1.0, default = 1.0)")
        print("  0.5 = 50% smaller (232x432)")
        print("  0.8 = 20% smaller (371x691)")
        print("\nTry zoom 1.5-2.0 for tight character framing!")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Validate input is WebM
    if not input_path.lower().endswith('.webm'):
        print("Error: Input file must be in WebM format (.webm)", file=sys.stderr)
        sys.exit(1)
    
    # Generate output filename if not provided
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        input_stem = Path(input_path).stem
        output_path = f"{input_stem}_resized.webm"
    
    # Get zoom factor if provided
    zoom_factor = float(sys.argv[3]) if len(sys.argv) >= 4 else 1.5
    
    # Get y_offset if provided
    y_offset = float(sys.argv[4]) if len(sys.argv) >= 5 else 0.0
    
    # Get scale if provided
    scale = 1.0
    if len(sys.argv) >= 6:
        if sys.argv[5] == '--scale' and len(sys.argv) >= 7:
            scale = float(sys.argv[6])
        elif sys.argv[5].startswith('--scale='):
            scale = float(sys.argv[5].split('=')[1])
    
    # Validate zoom factor
    if zoom_factor < 1.0:
        print("Error: Zoom factor must be >= 1.0", file=sys.stderr)
        sys.exit(1)
    
    # Validate y_offset
    if y_offset < -1.0 or y_offset > 1.0:
        print("Error: y_offset must be between -1.0 and 1.0", file=sys.stderr)
        sys.exit(1)
    
    # Validate scale
    if scale <= 0.0 or scale > 1.0:
        print("Error: Scale must be between 0.0 (exclusive) and 1.0", file=sys.stderr)
        sys.exit(1)
    
    # Check if input file exists
    if not Path(input_path).exists():
        print(f"Error: Input file '{input_path}' not found", file=sys.stderr)
        sys.exit(1)
    
    resize_and_zoom_video(input_path, output_path, zoom_factor, y_offset, scale)


if __name__ == "__main__":
    main()
