#!/usr/bin/env python3
"""
#Written by Alexandros Panagiotakopoulos
#alexandrospanag.github.io
#03/02/2026
#LICENSE: CC 4.0 BY-NC-SA

WebM File Compressor
Compresses .webm files to minimize file size while maintaining resolution.
Uses ffmpeg with VP9 codec and aggressive compression settings.



# python webm_compressor.py video.webm
"""

import subprocess
import os
import sys
from pathlib import Path


def get_video_info(input_file):
    """Get video information using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,duration,bit_rate',
        '-of', 'default=noprint_wrappers=1',
        input_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = {}
        for line in result.stdout.strip().split('\n'):
            if '=' in line:
                key, value = line.split('=')
                info[key] = value
        return info
    except subprocess.CalledProcessError:
        return None


def compress_webm(input_file, output_file=None, crf=35, target_bitrate=None, two_pass=True):
    """
    Compress a .webm file using VP9 codec with aggressive settings.
    
    Args:
        input_file: Path to input .webm file
        output_file: Path to output file (optional, defaults to input_compressed.webm)
        crf: Constant Rate Factor (18-40, higher = smaller file, 35 recommended)
        target_bitrate: Target bitrate in kbps (optional, overrides CRF)
        two_pass: Use two-pass encoding for better quality/size ratio
    """
    
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"Error: File '{input_file}' not found!")
        return False
    
    if not input_path.suffix.lower() == '.webm':
        print(f"Error: File '{input_file}' is not a .webm file!")
        return False
    
    # Set output file name
    if output_file is None:
        output_file = input_path.parent / f"{input_path.stem}_compressed.webm"
    
    output_path = Path(output_file)
    
    # Get original file info
    info = get_video_info(str(input_path))
    if info:
        print(f"Original resolution: {info.get('width', 'unknown')}x{info.get('height', 'unknown')}")
    
    print(f"Compressing: {input_path}")
    print(f"Output: {output_path}")
    print(f"Settings: CRF={crf}, Two-pass={two_pass}")
    
    # Base ffmpeg command with VP9 codec and aggressive compression
    base_cmd = [
        'ffmpeg',
        '-i', str(input_path),
        '-c:v', 'libvpx-vp9',  # VP9 codec
        '-deadline', 'good',    # good quality/speed tradeoff
        '-cpu-used', '1',       # 0-5, lower = slower but better compression
        '-row-mt', '1',         # Enable row-based multithreading
        '-tile-columns', '2',   # Parallel encoding
        '-tile-rows', '1',
    ]
    
    # Audio settings - compress audio as well
    audio_cmd = [
        '-c:a', 'libopus',      # Opus codec (better than Vorbis)
        '-b:a', '64k',          # 64kbps audio bitrate
        '-ac', '2',             # Stereo
    ]
    
    # Video quality settings
    if target_bitrate:
        # Constrained quality mode with target bitrate
        quality_cmd = [
            '-b:v', f'{target_bitrate}k',
            '-crf', str(crf),
            '-maxrate', f'{int(target_bitrate * 1.5)}k',
            '-bufsize', f'{int(target_bitrate * 2)}k',
        ]
    else:
        # CRF mode (constant quality)
        quality_cmd = [
            '-crf', str(crf),
            '-b:v', '0',  # Let CRF control bitrate
        ]
    
    if two_pass and target_bitrate:
        # Two-pass encoding for better compression
        print("Running first pass...")
        pass1_cmd = base_cmd + quality_cmd + [
            '-pass', '1',
            '-an',  # No audio in first pass
            '-f', 'null',
            '/dev/null' if os.name != 'nt' else 'NUL'
        ]
        
        try:
            subprocess.run(pass1_cmd, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error during first pass: {e}")
            return False
        
        print("Running second pass...")
        pass2_cmd = base_cmd + quality_cmd + audio_cmd + [
            '-pass', '2',
            '-y',  # Overwrite output file
            str(output_path)
        ]
        
        try:
            subprocess.run(pass2_cmd, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error during second pass: {e}")
            return False
        finally:
            # Clean up pass log files
            for log_file in Path('.').glob('ffmpeg2pass-*.log'):
                log_file.unlink()
    else:
        # Single pass encoding
        single_pass_cmd = base_cmd + quality_cmd + audio_cmd + [
            '-y',  # Overwrite output file
            str(output_path)
        ]
        
        try:
            print("Encoding...")
            subprocess.run(single_pass_cmd, check=True, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error during encoding: {e}")
            return False
    
    # Compare file sizes
    original_size = input_path.stat().st_size
    compressed_size = output_path.stat().st_size
    reduction = ((original_size - compressed_size) / original_size) * 100
    
    print(f"\n✓ Compression complete!")
    print(f"Original size: {original_size / (1024*1024):.2f} MB")
    print(f"Compressed size: {compressed_size / (1024*1024):.2f} MB")
    print(f"Reduction: {reduction:.1f}%")
    
    return True


def main():
    if len(sys.argv) < 2:
        print("WebM Compressor - Minimize file size while maintaining resolution")
        print("\nUsage:")
        print(f"  python {sys.argv[0]} <input.webm> [options]")
        print("\nOptions:")
        print("  --output, -o <file>     Output file path")
        print("  --crf <value>           CRF value (18-40, default: 35, higher = smaller)")
        print("  --bitrate, -b <kbps>    Target bitrate in kbps (overrides CRF)")
        print("  --single-pass           Use single-pass encoding (faster)")
        print("\nExamples:")
        print(f"  python {sys.argv[0]} video.webm")
        print(f"  python {sys.argv[0]} video.webm --crf 40 --single-pass")
        print(f"  python {sys.argv[0]} video.webm --bitrate 500 -o output.webm")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    crf = 35
    bitrate = None
    two_pass = True
    
    # Parse arguments
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg in ['--output', '-o']:
            output_file = sys.argv[i + 1]
            i += 2
        elif arg == '--crf':
            crf = int(sys.argv[i + 1])
            i += 2
        elif arg in ['--bitrate', '-b']:
            bitrate = int(sys.argv[i + 1])
            i += 2
        elif arg == '--single-pass':
            two_pass = False
            i += 1
        else:
            print(f"Unknown option: {arg}")
            sys.exit(1)
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: ffmpeg is not installed or not found in PATH!")
        print("Please install ffmpeg to use this script.")
        sys.exit(1)
    
    # Compress the file
    success = compress_webm(input_file, output_file, crf, bitrate, two_pass)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
