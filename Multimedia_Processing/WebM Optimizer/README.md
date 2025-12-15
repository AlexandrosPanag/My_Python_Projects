# WebM Quality Optimizer

A powerful Python-based tool for enhancing WebM video quality using modern VP9 encoding techniques. This optimizer improves video clarity, reduces blurriness, and enhances color correction while maintaining original dimensions.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Features

- **Quality Enhancement**: Applies denoising, sharpening, and color correction filters
- **Dimension Preservation**: Maintains original video width and height (1:1 optimization)
- **Modern VP9 Encoding**: Uses latest VP9 codec features for optimal compression
- **Smart Bitrate Calculation**: Automatically determines optimal bitrate based on resolution and framerate
- **Multiple Quality Presets**: Choose between ultra, high, medium, and fast encoding modes
- **Two-Pass Encoding**: Optional two-pass mode for superior quality results
- **Multi-threaded Processing**: Utilizes row-based multithreading for faster encoding
- **Progress Monitoring**: Real-time encoding progress display

## Quality Improvements

The optimizer applies the following enhancements:

1. **Denoising** (NLMeans filter): Reduces compression artifacts and smooths video playback
2. **Sharpening** (Unsharp filter): Reduces blurriness without over-sharpening
3. **Color Correction**: Enhanced contrast (+5%), brightness (+2%), and saturation (+10%)
4. **Advanced VP9 Settings**: Alternate reference frames, adaptive GOP structure, and frame parallelization

## Requirements

- Python 3.6 or higher
- FFmpeg 4.0 or higher (with libvpx-vp9 and libopus support)

## Installation

### 1. Install FFmpeg

#### Windows
```bash
# Using winget (recommended)
winget install ffmpeg

# Or using Chocolatey
choco install ffmpeg
```

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Download the Script

```bash
git clone https://github.com/yourusername/webm-quality-optimizer.git
cd webm-quality-optimizer
```

Or download `webm_optimizer.py` directly.

### 3. Verify FFmpeg Installation

```bash
ffmpeg -version
```

You should see FFmpeg version information displayed.

## Usage

### Basic Usage

Optimize a WebM video with default settings (high quality preset):

```bash
python webm_optimizer.py input.webm
```

This creates `input_optimized.webm` in the same directory.

### Specify Output File

```bash
python webm_optimizer.py input.webm output.webm
```

### Choose Quality Preset

```bash
python webm_optimizer.py input.webm output.webm ultra
```

## Quality Presets

| Preset | Speed | CRF | Best For | Encoding Time |
|--------|-------|-----|----------|---------------|
| **ultra** | 0 | 20 | Maximum quality, archival | Slowest |
| **high** | 1 | 23 | Excellent quality/speed balance (default) | Moderate |
| **medium** | 2 | 28 | Good quality, faster encoding | Fast |
| **fast** | 4 | 31 | Quick encoding, acceptable quality | Fastest |

### CRF Explanation
Lower CRF values = higher quality. Range: 0-63 (0 = lossless, 63 = worst quality)

## Examples

### Optimize AI-generated video with ultra quality
```bash
python webm_optimizer.py ai_generated.webm enhanced.webm ultra
```

### Quick optimization for testing
```bash
python webm_optimizer.py test_video.webm test_output.webm fast
```

### Batch process multiple videos (Windows)
```bash
for %f in (*.webm) do python webm_optimizer.py "%f"
```

### Batch process multiple videos (Linux/macOS)
```bash
for file in *.webm; do python webm_optimizer.py "$file"; done
```

## Technical Details

### Encoding Parameters

The optimizer uses the following VP9 encoding parameters:

- **Codec**: libvpx-vp9 (VP9 video codec)
- **Audio Codec**: libopus at 128 kbps
- **Row-based Multithreading**: Enabled for parallel processing
- **Tile Columns**: Automatically calculated based on resolution
- **Frame Parallelization**: Enabled for improved encoding speed
- **Alternate Reference Frames**: Enabled for better compression
- **Lag-in-frames**: 25 frames for optimal quality
- **GOP Structure**: 2 seconds (improves seeking and quality)

### Bitrate Calculation

The script automatically calculates optimal bitrate using bits-per-pixel (BPP) methodology:

- **360p and below**: 0.10 BPP
- **480p**: 0.08 BPP
- **720p**: 0.07 BPP
- **1080p**: 0.06 BPP
- **4K and above**: 0.05 BPP

Minimum bitrate: 500 kbps

### Filter Chain

Applied filters in order:
1. `nlmeans=s=1.5:p=7:r=15` - Non-local means denoising
2. `unsharp=5:5:0.8:5:5:0.0` - Subtle sharpening
3. `eq=contrast=1.05:brightness=0.02:saturation=1.1` - Color enhancement

## Output Information

The script provides detailed information during processing:

- Input video resolution, framerate, duration, and bitrate
- Selected quality preset and target bitrate
- Real-time encoding progress (frames, fps, bitrate)
- Output file size and location

## Troubleshooting

### FFmpeg not found
- **Windows**: Restart Command Prompt after installation
- **All platforms**: Verify FFmpeg is in PATH: `ffmpeg -version`
- Try logging out and back in, or restart your computer

### Encoding fails
- Check input file is a valid WebM video
- Ensure sufficient disk space for output file
- Verify FFmpeg supports VP9: `ffmpeg -codecs | grep vp9`

### Slow encoding
- Use a faster preset: `medium` or `fast`
- Disable two-pass encoding (modify script: `two_pass=False`)
- Close other resource-intensive applications

### Output file is larger
- This is normal for quality enhancement
- Original may have been over-compressed
- Try a higher CRF value (lower quality, smaller size)

## Performance Tips

- **Ultra preset**: Use for final renders and archival
- **High preset**: Best for most use cases (default)
- **Medium/Fast presets**: Use for quick testing or time-sensitive work
- **Two-pass encoding**: Better quality but doubles encoding time
- **Resolution impact**: 4K videos take significantly longer than 1080p

## Limitations

- Processes one video at a time (use shell loops for batch processing)
- Requires significant CPU resources during encoding
- Two-pass encoding requires temporary storage for log files
- Cannot process videos requiring authentication or DRM-protected content

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

**Credits**: Alexandros Panagiotakopoulos - [alexandrospanag.github.io](https://alexandrospanag.github.io)

You are free to:
- **Share**: Copy and redistribute the material in any medium or format
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made

See the [LICENSE](https://creativecommons.org/licenses/by/4.0/) for full details.



## Acknowledgments

- FFmpeg team for the powerful multimedia framework
- VP9 codec developers at Google
- The open-source community for continuous improvements
