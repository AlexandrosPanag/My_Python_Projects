#!/usr/bin/env python3
"""
WebM Toolkit
Written by Alexandros Panagiotakopoulos
alexandrospanag.github.io
LICENSE: CC 4.0 BY-NC-SA

Combines sharpening, compression, and frame interpolation for .webm files. 
NOTE: 30 FPS is recommended for best results; higher frame rates may cause issues.

Usage: python webm_megasolution.py input.webm [output.webm]
"""

import subprocess
import sys
import os
from pathlib import Path


# ─────────────────────────── ffmpeg helpers ───────────────────────────────

def find_ffmpeg():
    """Locate the ffmpeg binary, trying common paths."""
    candidates = [
        'ffmpeg',
        'C:\\ffmpeg\\bin\\ffmpeg.exe',
        'C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe',
        '.\\ffmpeg.exe',
    ]
    for path in candidates:
        try:
            subprocess.run([path, '-version'],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL,
                           check=True)
            return path
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    return None


def ffprobe_path(ffmpeg):
    if ffmpeg == 'ffmpeg':
        return 'ffprobe'
    return ffmpeg.replace('ffmpeg.exe', 'ffprobe.exe')


def get_video_info(input_file, ffmpeg):
    """Return (width, height, fps_float) of the first video stream."""
    ffprobe = ffprobe_path(ffmpeg)
    cmd = [
        ffprobe, '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height,r_frame_rate',
        '-of', 'default=noprint_wrappers=1',
        input_file
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = {}
        for line in result.stdout.strip().split('\n'):
            if '=' in line:
                k, v = line.split('=', 1)
                info[k.strip()] = v.strip()
        width  = int(info.get('width', 0))
        height = int(info.get('height', 0))
        # r_frame_rate is like "30/1" or "24000/1001"
        raw_fps = info.get('r_frame_rate', '30/1')
        num, den = raw_fps.split('/')
        fps = round(int(num) / int(den), 3)
        return width, height, fps
    except Exception:
        print(f"  Warning: could not read video info from '{input_file}'")
        return 0, 0, 30.0


def run_ffmpeg(cmd, label):
    """Run an ffmpeg command; exit on failure."""
    print(f"  Running {label}...")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(f"\n  Error: ffmpeg failed during {label}.")
        sys.exit(1)


def file_mb(path):
    return os.path.getsize(path) / (1024 * 1024)


# ─────────────────────────── processing functions ─────────────────────────

def sharpen(input_file, output_file, ffmpeg):
    """Apply a subtle unsharp mask to reduce pixelation."""
    w, h, fps = get_video_info(input_file, ffmpeg)
    print(f"  Resolution : {w}x{h}  |  FPS : {fps}")

    cmd = [
        ffmpeg,
        '-i', input_file,
        '-vf', 'unsharp=5:5:0.4:5:5:0.0',
        '-c:v', 'libvpx-vp9',
        '-crf', '23',
        '-b:v', '0',
        '-c:a', 'copy',
        '-y', output_file
    ]
    run_ffmpeg(cmd, "sharpening")
    print(f"  ✓ Sharpened → '{output_file}'  ({file_mb(output_file):.2f} MB)")


def compress(input_file, output_file, ffmpeg, crf=35):
    """Compress using VP9 CRF mode + Opus audio."""
    w, h, fps = get_video_info(input_file, ffmpeg)
    print(f"  Resolution : {w}x{h}  |  FPS : {fps}  |  CRF : {crf}")

    cmd = [
        ffmpeg,
        '-i', input_file,
        '-c:v', 'libvpx-vp9',
        '-crf', str(crf),
        '-b:v', '0',
        '-deadline', 'good',
        '-cpu-used', '1',
        '-row-mt', '1',
        '-tile-columns', '2',
        '-tile-rows', '1',
        '-c:a', 'libopus',
        '-b:a', '64k',
        '-ac', '2',
        '-y', output_file
    ]
    run_ffmpeg(cmd, "compression")

    original_size = file_mb(input_file)
    compressed_size = file_mb(output_file)
    reduction = ((original_size - compressed_size) / original_size) * 100
    print(f"  ✓ Compressed → '{output_file}'")
    print(f"     {original_size:.2f} MB  →  {compressed_size:.2f} MB  ({reduction:.1f}% reduction)")


def boost_framerate(input_file, output_file, ffmpeg, target_fps=60):
    """
    Increase fluidity / frame rate using the minterpolate filter.

    minterpolate uses motion-compensated frame interpolation (MCFI) to
    synthesise new in-between frames, producing smoother motion at the
    target frame rate.  mi_mode=mci gives the best quality; fps sets the
    output frame rate.
    """
    w, h, src_fps = get_video_info(input_file, ffmpeg)
    if src_fps >= target_fps:
        print(f"  Source FPS ({src_fps}) is already ≥ target ({target_fps}).")
        print(f"  Interpolating anyway to smooth motion further...")

    print(f"  Resolution : {w}x{h}  |  {src_fps} FPS  →  {target_fps} FPS")

    vf = f"minterpolate=fps={target_fps}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"

    cmd = [
        ffmpeg,
        '-i', input_file,
        '-vf', vf,
        '-c:v', 'libvpx-vp9',
        '-crf', '23',
        '-b:v', '0',
        '-c:a', 'copy',
        '-y', output_file
    ]
    run_ffmpeg(cmd, "frame interpolation")
    print(f"  ✓ Frame rate boosted → '{output_file}'  ({file_mb(output_file):.2f} MB)")


# ─────────────────────────── menu & orchestration ─────────────────────────

MENU = """
╔══════════════════════════════════════╗
║         WebM Toolkit  v1.0           ║
╠══════════════════════════════════════╣
║  1 → Sharpen   (reduce pixelation)   ║
║  2 → Compress  (minimise file size)  ║
║  3 → Fluidity  (boost frame rate)    ║
║  4 → All-in-one (1 → 3 → 2)         ║
╚══════════════════════════════════════╝
"""

def ask_choice():
    print(MENU)
    while True:
        choice = input("Enter your choice (1/2/3/4): ").strip()
        if choice in ('1', '2', '3', '4'):
            return choice
        print("  Please enter 1, 2, 3, or 4.")


def tmp_path(base, suffix):
    """Return a temporary file name derived from base."""
    p = Path(base)
    return str(p.parent / f"{p.stem}_tmp_{suffix}.webm")


def main():
    if len(sys.argv) < 2:
        print("Usage: python webm_toolkit.py input.webm [output.webm]")
        sys.exit(1)

    input_file  = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        sys.exit(1)

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        print("Error: ffmpeg is not installed or not in PATH.")
        print("Download from https://ffmpeg.org/download.html")
        print("Or: choco install ffmpeg  /  winget install FFmpeg")
        sys.exit(1)

    choice = ask_choice()

    # Default output names
    stem = Path(input_file).stem

    if choice == '1':
        out = output_file or f"{stem}_sharpened.webm"
        print(f"\n── Sharpening ──────────────────────────")
        sharpen(input_file, out, ffmpeg)

    elif choice == '2':
        out = output_file or f"{stem}_compressed.webm"
        print(f"\n── Compressing ─────────────────────────")
        compress(input_file, out, ffmpeg)

    elif choice == '3':
        fps_str = input("Target FPS? (default 60): ").strip()
        target_fps = int(fps_str) if fps_str.isdigit() else 60
        out = output_file or f"{stem}_fluid_{target_fps}fps.webm"
        print(f"\n── Boosting frame rate ─────────────────")
        boost_framerate(input_file, out, ffmpeg, target_fps)

    elif choice == '4':
        fps_str = input("Target FPS for fluidity step? (default 60): ").strip()
        target_fps = int(fps_str) if fps_str.isdigit() else 60

        out      = output_file or f"{stem}_processed.webm"
        tmp1     = tmp_path(input_file, "sharp")
        tmp2     = tmp_path(input_file, "fluid")

        print(f"\n── Step 1 / 3 : Sharpening ─────────────")
        sharpen(input_file, tmp1, ffmpeg)

        print(f"\n── Step 2 / 3 : Boosting frame rate ────")
        boost_framerate(tmp1, tmp2, ffmpeg, target_fps)

        print(f"\n── Step 3 / 3 : Compressing ────────────")
        compress(tmp2, out, ffmpeg)

        # Clean up temp files
        for t in (tmp1, tmp2):
            try:
                os.remove(t)
            except OSError:
                pass

        print(f"\n✓ All done!  Final file: '{out}'  ({file_mb(out):.2f} MB)")


if __name__ == '__main__':
    main()
