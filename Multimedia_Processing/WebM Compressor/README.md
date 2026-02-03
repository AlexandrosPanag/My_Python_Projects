# WebM Size Compressor

A powerful Python-based tool for minimizing WebM video file sizes while maintaining original resolution. This compressor uses aggressive VP9 encoding techniques to achieve maximum size reduction without altering video dimensions.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author
**Alexandros Panagiotakopoulos**

## Features

- **Maximum Compression**: Achieves 40-70% file size reduction on average
- **Resolution Preservation**: Maintains original video width and height (no dimension changes)
- **Modern VP9 Encoding**: Uses latest VP9 codec features for optimal compression
- **Aggressive Audio Compression**: Converts audio to efficient Opus codec at 64 kbps
- **Flexible CRF Control**: Adjustable compression levels (18-40) for size/quality balance
- **Two-Pass Encoding**: Optional two-pass mode for superior compression efficiency
- **Constrained Bitrate Mode**: Target specific bitrates for precise file size control
- **Multi-threaded Processing**: Utilizes row-based multithreading for faster encoding
- **Comprehensive Statistics**: Displays original size, compressed size, and reduction percentage

## Compression Strategy

The compressor applies the following techniques:

1. **VP9 Codec**: Modern video codec with superior compression efficiency
2. **Aggressive CRF Settings**: Default CRF of 35 for significant size reduction
3. **Opus Audio Codec**: Highly efficient audio encoding at 64 kbps
4. **Optimized Encoding Parameters**: Row-based multithreading, tile-based encoding
5. **Two-Pass Encoding**: Analyzes video first, then encodes optimally

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
git clone https://github.com/yourusername/webm-size-compressor.git
cd webm-size-compressor
```

Or download `webm_compressor.py` directly.

### 3. Verify FFmpeg Installation

```bash
ffmpeg -version
```

You should see FFmpeg version information displayed.

## Usage

### Basic Usage

Compress a WebM video with default settings (CRF 35):

```bash
python webm_compressor.py input.webm
```

This creates `input_compressed.webm` in the same directory.

### Specify Output File

```bash
python webm_compressor.py input.webm --output compressed.webm
```

Or use the short form:
```bash
python webm_compressor.py input.webm -o compressed.webm
```

### Adjust Compression Level

Higher CRF = smaller file size (but lower quality):

```bash
python webm_compressor.py input.webm --crf 40
```

Lower CRF = larger file size (but better quality):

```bash
python webm_compressor.py input.webm --crf 28
```

### Target Specific Bitrate

```bash
python webm_compressor.py input.webm --bitrate 500
```

Or use the short form:
```bash
python webm_compressor.py input.webm -b 500
```

### Single-Pass Encoding (Faster)

```bash
python webm_compressor.py input.webm --single-pass
```

## Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Specify output file path | `input_compressed.webm` |
| `--crf` | - | CRF value (18-40, higher = smaller) | 35 |
| `--bitrate` | `-b` | Target bitrate in kbps (overrides CRF) | None |
| `--single-pass` | - | Use faster single-pass encoding | Two-pass |

## CRF Guidelines

| CRF Value | Quality | File Size | Best For |
|-----------|---------|-----------|----------|
| **18-23** | Excellent | Larger | High-quality archival, minimal compression |
| **28-32** | Good | Medium | Balanced compression, good visual quality |
| **35-37** | Acceptable | Small | Significant compression (default) |
| **38-40** | Lower | Very Small | Maximum compression, smaller visuals acceptable |

### CRF Explanation
CRF (Constant Rate Factor) controls quality. Range: 18-40 for practical use (lower = better quality, larger file)

## Examples

### Maximum compression for web delivery
```bash
python webm_compressor.py large_video.webm --crf 40
```

### Balanced compression with custom output
```bash
python webm_compressor.py input.webm -o output.webm --crf 32
```

### Fast single-pass compression
```bash
python webm_compressor.py video.webm --crf 35 --single-pass
```

### Target 500 kbps bitrate
```bash
python webm_compressor.py video.webm -b 500 -o compressed.webm
```

### Batch compress multiple videos (Windows)
```bash
for %f in (*.webm) do python webm_compressor.py "%f" --crf 35
```

### Batch compress multiple videos (Linux/macOS)
```bash
for file in *.webm; do python webm_compressor.py "$file" --crf 35; done
```

## Technical Details

### Encoding Parameters

The compressor uses the following VP9 encoding parameters:

- **Video Codec**: libvpx-vp9 (VP9 video codec)
- **Audio Codec**: libopus at 64 kbps stereo
- **Deadline**: good (quality/speed tradeoff)
- **CPU-used**: 1 (0-5 scale, lower = slower but better compression)
- **Row-based Multithreading**: Enabled for parallel processing
- **Tile Columns**: 2 (parallel encoding blocks)
- **Tile Rows**: 1
- **CRF Mode**: Constant quality compression (default)
- **Constrained Quality Mode**: When bitrate is specified

### Two-Pass Encoding

When using two-pass mode with target bitrate:

1. **First Pass**: Analyzes the entire video, gathering statistics
2. **Second Pass**: Uses statistics to optimize bitrate distribution
3. **Result**: Better quality/size ratio compared to single-pass

Benefits:
- More consistent quality throughout video
- Better bitrate allocation to complex scenes
- Improved overall compression efficiency

Tradeoff:
- Takes approximately 2x longer than single-pass

### Compression Technique

The script achieves maximum compression by:

1. **Aggressive CRF**: Default of 35 provides significant size reduction
2. **Efficient Audio**: Opus codec at 64 kbps (vs typical 128 kbps)
3. **Optimized GOP**: Let encoder decide optimal keyframe placement
4. **Advanced VP9 Features**: Tile-based encoding, row multithreading
5. **Resolution Preservation**: No upscaling/downscaling overhead

## Output Information

The script provides detailed information during processing:

- Original video resolution detection
- Compression settings (CRF, two-pass status)
- Real-time encoding progress
- File size comparison (original vs compressed)
- Compression percentage achieved

Example output:
```
Original resolution: 1920x1080
Compressing: video.webm
Output: video_compressed.webm
Settings: CRF=35, Two-pass=True
Encoding...

✓ Compression complete!
Original size: 45.32 MB
Compressed size: 18.76 MB
Reduction: 58.6%
```

## Typical Compression Results

Based on real-world usage:

- **Screen recordings**: 50-70% reduction
- **Live action video**: 40-60% reduction
- **Animation**: 45-65% reduction
- **Static content**: 60-80% reduction

Note: Results vary based on source material complexity, original encoding, and chosen CRF value.

## Troubleshooting

### FFmpeg not found
- **Windows**: Restart Command Prompt after installation
- **All platforms**: Verify FFmpeg is in PATH: `ffmpeg -version`
- Try logging out and back in, or restart your computer

### Compression fails
- Check input file is a valid WebM video: `ffprobe input.webm`
- Ensure sufficient disk space for output file
- Verify FFmpeg supports VP9: `ffmpeg -codecs | grep vp9`

### Output quality is too low
- Use lower CRF value: `--crf 28` or `--crf 30`
- Try two-pass encoding (default) instead of single-pass
- Consider if 40-70% compression is too aggressive for your use case

### Encoding is slow
- Use single-pass encoding: `--single-pass`
- Increase CRF value (faster encoding, smaller file)
- Close other resource-intensive applications
- Use `--cpu-used 4` in script (faster, slightly lower quality)

### File size didn't reduce much
- Original may already be well-compressed
- Try higher CRF: `--crf 38` or `--crf 40`
- Check if original uses efficient encoding already

## Performance Tips

- **Two-pass encoding**: Better compression but 2x slower (default)
- **Single-pass**: Faster but slightly less efficient compression
- **CRF 35-37**: Sweet spot for most content (default is 35)
- **CRF 40**: Maximum compression, use for non-critical videos
- **Bitrate mode**: Use when you need exact file size targets
- **Batch processing**: Process multiple videos using shell loops

## Advanced Usage

### Modify CPU-used setting

Edit the script to change encoding speed (line 87):
```python
'-cpu-used', '1',       # Change to 0 (slower, better) or 4 (faster, good enough)
```

### Adjust audio bitrate

Edit the script to change audio quality (line 93):
```python
'-b:a', '64k',          # Change to '96k' for better audio or '48k' for more compression
```

### Customize tile settings

Edit the script for different parallel encoding (lines 89-90):
```python
'-tile-columns', '2',   # Increase for wider videos (max 6)
'-tile-rows', '1',      # Increase for taller videos (max 2)
```

## Limitations

- Processes one video at a time (use shell loops for batch processing)
- Requires significant CPU resources during encoding
- Two-pass encoding creates temporary log files
- Cannot process DRM-protected content
- Resolution is preserved (no downscaling option built-in)

## Use Cases

Perfect for:
- Reducing file sizes for web hosting
- Compressing screen recordings
- Archiving videos with storage constraints
- Preparing videos for upload (size limits)
- Batch processing large video collections

Not ideal for:
- Professional archival (consider lossless compression)
- Videos requiring maximum quality preservation
- Content where file size is not a concern

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
- Users who have achieved 40-70% compression savings
