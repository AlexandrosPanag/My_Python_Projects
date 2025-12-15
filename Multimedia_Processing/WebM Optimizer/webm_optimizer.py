# Written by Alexandros Panagiotakopoulos
# 15/12/2025
# Enhanced VP9 encoding for better quality WebM videos
# License: CC-BY-SA-4.0

#!/usr/bin/env python3
"""
WebM Quality Optimizer
Enhances WebM video quality using modern VP9 encoding with quality improvements
without changing dimensions - optimized for Dec 2025
"""

import subprocess
import sys
import os
import json
from pathlib import Path
from typing import Dict, Optional, Tuple

class WebMOptimizer:
    def __init__(self):
        self.ffmpeg_path = "ffmpeg"
        self.ffprobe_path = "ffprobe"
        
    def check_ffmpeg(self) -> bool:
        """Check if FFmpeg is installed and accessible"""
        try:
            result = subprocess.run(
                [self.ffmpeg_path, "-version"],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0:
                print(f"✓ FFmpeg found: {result.stdout.split()[2]}")
                return True
        except FileNotFoundError:
            pass
        
        print("✗ FFmpeg not found. Please install FFmpeg:")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt install ffmpeg")
        return False
    
    def get_video_info(self, input_file: str) -> Optional[Dict]:
        """Extract video information using ffprobe"""
        try:
            cmd = [
                self.ffprobe_path,
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                input_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            data = json.loads(result.stdout)
            
            # Find video stream
            video_stream = next(
                (s for s in data["streams"] if s["codec_type"] == "video"),
                None
            )
            
            if not video_stream:
                print("✗ No video stream found")
                return None
            
            info = {
                "width": int(video_stream.get("width", 0)),
                "height": int(video_stream.get("height", 0)),
                "fps": self._parse_fps(video_stream.get("r_frame_rate", "30/1")),
                "duration": float(data["format"].get("duration", 0)),
                "bitrate": int(data["format"].get("bit_rate", 0)) // 1000,
                "codec": video_stream.get("codec_name", "unknown")
            }
            
            return info
            
        except Exception as e:
            print(f"✗ Error getting video info: {e}")
            return None
    
    def _parse_fps(self, fps_str: str) -> float:
        """Parse FPS from fraction string"""
        try:
            num, den = map(int, fps_str.split("/"))
            return num / den
        except:
            return 30.0
    
    def calculate_optimal_bitrate(self, width: int, height: int, fps: float) -> int:
        """Calculate optimal bitrate based on resolution and fps"""
        # Pixels per second
        pps = width * height * fps
        
        # Bitrate calculation (bits per pixel scaled by resolution)
        if width * height <= 640 * 360:  # 360p
            bpp = 0.10
        elif width * height <= 854 * 480:  # 480p
            bpp = 0.08
        elif width * height <= 1280 * 720:  # 720p
            bpp = 0.07
        elif width * height <= 1920 * 1080:  # 1080p
            bpp = 0.06
        else:  # 4K+
            bpp = 0.05
        
        bitrate = int((pps * bpp) / 1000)  # Convert to kbps
        return max(500, bitrate)  # Minimum 500kbps
    
    def optimize_webm(
        self,
        input_file: str,
        output_file: Optional[str] = None,
        quality_preset: str = "high",
        two_pass: bool = True
    ) -> bool:
        """
        Optimize WebM video with enhanced quality settings
        
        Args:
            input_file: Input WebM file path
            output_file: Output file path (default: input_optimized.webm)
            quality_preset: 'ultra', 'high', 'medium', 'fast'
            two_pass: Use two-pass encoding for better quality
        """
        input_path = Path(input_file)
        
        if not input_path.exists():
            print(f"✗ Input file not found: {input_file}")
            return False
        
        # Get video info
        print(f"\n📊 Analyzing: {input_path.name}")
        info = self.get_video_info(input_file)
        if not info:
            return False
        
        print(f"   Resolution: {info['width']}x{info['height']}")
        print(f"   FPS: {info['fps']:.2f}")
        print(f"   Duration: {info['duration']:.1f}s")
        print(f"   Current bitrate: {info['bitrate']} kbps")
        
        # Output file
        if not output_file:
            output_file = str(input_path.parent / f"{input_path.stem}_optimized.webm")
        
        # Quality presets
        presets = {
            "ultra": {"speed": 0, "crf": 20, "quality": "best"},
            "high": {"speed": 1, "crf": 23, "quality": "good"},
            "medium": {"speed": 2, "crf": 28, "quality": "good"},
            "fast": {"speed": 4, "crf": 31, "quality": "good"}
        }
        
        preset = presets.get(quality_preset, presets["high"])
        target_bitrate = self.calculate_optimal_bitrate(
            info["width"], info["height"], info["fps"]
        )
        
        print(f"\n🎬 Encoding with '{quality_preset}' preset")
        print(f"   Target bitrate: {target_bitrate} kbps")
        print(f"   Speed: {preset['speed']}, CRF: {preset['crf']}")
        
        # Build filter chain for quality enhancement
        filters = [
            # Denoise (subtle)
            "nlmeans=s=1.5:p=7:r=15",
            # Slight sharpening
            "unsharp=5:5:0.8:5:5:0.0",
            # Color enhancement
            "eq=contrast=1.05:brightness=0.02:saturation=1.1"
        ]
        
        vf_chain = ",".join(filters)
        
        # Calculate tile columns based on width
        tile_cols = min(6, (info["width"] // 512).bit_length())
        
        if two_pass:
            success = self._two_pass_encode(
                input_file, output_file, info, preset,
                target_bitrate, vf_chain, tile_cols
            )
        else:
            success = self._single_pass_encode(
                input_file, output_file, info, preset,
                target_bitrate, vf_chain, tile_cols
            )
        
        if success:
            output_size = Path(output_file).stat().st_size / (1024 * 1024)
            print(f"\n✓ Optimization complete!")
            print(f"   Output: {output_file}")
            print(f"   Size: {output_size:.2f} MB")
        
        return success
    
    def _single_pass_encode(
        self, input_file: str, output_file: str, info: Dict,
        preset: Dict, bitrate: int, vf_chain: str, tile_cols: int
    ) -> bool:
        """Single pass encoding"""
        cmd = [
            self.ffmpeg_path,
            "-i", input_file,
            "-c:v", "libvpx-vp9",
            "-b:v", f"{bitrate}k",
            "-crf", str(preset["crf"]),
            "-quality", preset["quality"],
            "-speed", str(preset["speed"]),
            "-row-mt", "1",
            "-tile-columns", str(tile_cols),
            "-frame-parallel", "1",
            "-auto-alt-ref", "1",
            "-lag-in-frames", "25",
            "-g", str(int(info["fps"] * 2)),  # 2 second GOP
            "-vf", vf_chain,
            "-c:a", "libopus",
            "-b:a", "128k",
            "-y",
            output_file
        ]
        
        return self._run_ffmpeg(cmd, "Encoding")
    
    def _two_pass_encode(
        self, input_file: str, output_file: str, info: Dict,
        preset: Dict, bitrate: int, vf_chain: str, tile_cols: int
    ) -> bool:
        """Two-pass encoding for better quality"""
        # Pass 1
        pass1_cmd = [
            self.ffmpeg_path,
            "-i", input_file,
            "-c:v", "libvpx-vp9",
            "-b:v", f"{bitrate}k",
            "-crf", str(preset["crf"]),
            "-quality", preset["quality"],
            "-speed", "4",  # Fast first pass
            "-row-mt", "1",
            "-tile-columns", str(tile_cols),
            "-frame-parallel", "1",
            "-auto-alt-ref", "1",
            "-lag-in-frames", "25",
            "-g", str(int(info["fps"] * 2)),
            "-vf", vf_chain,
            "-pass", "1",
            "-an",
            "-f", "webm",
            "-y",
            os.devnull if sys.platform != "win32" else "NUL"
        ]
        
        if not self._run_ffmpeg(pass1_cmd, "Pass 1/2"):
            return False
        
        # Pass 2
        pass2_cmd = [
            self.ffmpeg_path,
            "-i", input_file,
            "-c:v", "libvpx-vp9",
            "-b:v", f"{bitrate}k",
            "-minrate", f"{int(bitrate * 0.5)}k",
            "-maxrate", f"{int(bitrate * 1.5)}k",
            "-crf", str(preset["crf"]),
            "-quality", preset["quality"],
            "-speed", str(preset["speed"]),
            "-row-mt", "1",
            "-tile-columns", str(tile_cols),
            "-frame-parallel", "1",
            "-auto-alt-ref", "1",
            "-lag-in-frames", "25",
            "-g", str(int(info["fps"] * 2)),
            "-vf", vf_chain,
            "-pass", "2",
            "-c:a", "libopus",
            "-b:a", "128k",
            "-y",
            output_file
        ]
        
        success = self._run_ffmpeg(pass2_cmd, "Pass 2/2")
        
        # Cleanup pass files
        for f in ["ffmpeg2pass-0.log", "ffmpeg2pass-0.log.mbtree"]:
            try:
                if os.path.exists(f):
                    os.remove(f)
            except:
                pass
        
        return success
    
    def _run_ffmpeg(self, cmd: list, stage: str) -> bool:
        """Run FFmpeg command with progress display"""
        try:
            print(f"\n🔄 {stage}...")
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            for line in process.stdout:
                if "frame=" in line:
                    # Show progress
                    print(f"\r   {line.strip()}", end="", flush=True)
            
            process.wait()
            print()  # New line after progress
            
            if process.returncode != 0:
                print(f"✗ Encoding failed with code {process.returncode}")
                return False
            
            return True
            
        except Exception as e:
            print(f"✗ Error during encoding: {e}")
            return False


def main():
    print("=" * 60)
    print("WebM Quality Optimizer - VP9 Enhanced Edition")
    print("=" * 60)
    
    optimizer = WebMOptimizer()
    
    if not optimizer.check_ffmpeg():
        sys.exit(1)
    
    # Get input file
    if len(sys.argv) < 2:
        print("\nUsage: python webm_optimizer.py <input.webm> [output.webm] [preset]")
        print("\nPresets: ultra, high (default), medium, fast")
        print("\nExample:")
        print("  python webm_optimizer.py video.webm")
        print("  python webm_optimizer.py video.webm output.webm ultra")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    preset = sys.argv[3] if len(sys.argv) > 3 else "high"
    
    # Validate preset
    if preset not in ["ultra", "high", "medium", "fast"]:
        print(f"✗ Invalid preset '{preset}'. Using 'high'.")
        preset = "high"
    
    # Optimize
    success = optimizer.optimize_webm(
        input_file,
        output_file,
        quality_preset=preset,
        two_pass=True
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()