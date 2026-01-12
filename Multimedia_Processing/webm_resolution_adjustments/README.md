# WebM Video Processing Tools

A collection of Python scripts for processing WebM videos with resolution scaling and subtle sharpening effects.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Resolution Doubler](#resolution-doubler)
  - [Resolution Halver](#resolution-halver)
  - [Subtle Sharpener](#subtle-sharpener)
- [Technical Details](#technical-details)
- [Examples](#examples)
- [License](#license)
- [Credits](#credits)

## ✨ Features

This toolkit includes three complementary tools:

1. **webm_doubler.py** - Doubles video resolution (2x width, 2x height) with subtle sharpening
2. **webm_halver.py** - Halves video resolution (0.5x width, 0.5x height) with subtle sharpening
3. **webm_sharpen.py** - Applies gentle sharpening without changing resolution

All tools use high-quality Lanczos scaling (where applicable) and apply very subtle unsharp masking to reduce pixelation and maintain crisp edges without introducing artifacts.

## 🔧 Requirements

- Python 3.6 or higher
- FFmpeg with VP9 and Opus codec support

### Installing FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to your PATH.

**Verify installation:**
```bash
ffmpeg -version
```

## 📥 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/webm-video-tools.git
cd webm-video-tools
```

2. Make scripts executable (Linux/macOS):
```bash
chmod +x webm_doubler.py webm_halver.py webm_sharpen.py
```

## 🚀 Usage

### Resolution Doubler

Doubles both width and height of your WebM video.

```bash
# Basic usage (creates output.webm)
python webm_doubler.py input.webm

# Specify custom output filename
python webm_doubler.py input.webm doubled_video.webm
```

**Example:**
- Input: 1920x1080 → Output: 3840x2160
- Input: 640x480 → Output: 1280x960

### Resolution Halver

Reduces both width and height by half.

```bash
# Basic usage (creates output.webm)
python webm_halver.py input.webm

# Specify custom output filename
python webm_halver.py input.webm smaller_video.webm
```

**Example:**
- Input: 1920x1080 → Output: 960x540
- Input: 3840x2160 → Output: 1920x1080

### Subtle Sharpener

Applies gentle sharpening without changing resolution. Perfect for cleaning up slightly soft or pixelated videos.

```bash
# Basic usage (creates output.webm)
python webm_sharpen.py input.webm

# Specify custom output filename
python webm_sharpen.py input.webm sharpened_video.webm
```

**Example:**
- Input: 1920x1080 → Output: 1920x1080 (sharpened)

## 🔬 Technical Details

### Video Processing

- **Codec:** VP9 (libvpx-vp9) for optimal WebM compression
- **Audio Codec:** Opus (libopus) for doubler/halver, direct copy for sharpener
- **Scaling Algorithm:** Lanczos (high-quality resampling)
- **Quality:** CRF 23 (constant rate factor, adjustable)

### Sharpening Parameters

All scripts use the unsharp filter with conservative settings:

```
unsharp=5:5:0.3:5:5:0.0  (doubler/halver)
unsharp=5:5:0.4:5:5:0.0  (sharpener)
```

- **Matrix Size:** 5x5 (gentle blur radius)
- **Luma Amount:** 0.3-0.4 (subtle sharpening intensity)
- **Chroma Amount:** 0.0 (no color sharpening to avoid artifacts)

These settings provide a subtle enhancement without introducing halos, ringing, or other sharpening artifacts.

### Customization

To adjust sharpening intensity, modify the `filter_complex` line in the script:

```python
# Increase sharpening (range: 0.0 to 1.5 recommended)
filter_complex = "unsharp=5:5:0.8:5:5:0.0"

# Decrease sharpening
filter_complex = "unsharp=5:5:0.2:5:5:0.0"

# Disable sharpening entirely
filter_complex = "unsharp=5:5:0.0:5:5:0.0"
```

## 📊 Examples

### Upscaling a 720p video to 1440p

```bash
python webm_doubler.py video_720p.webm video_1440p.webm
```

### Downscaling 4K to 1080p

```bash
python webm_halver.py video_4k.webm video_1080p.webm
```

### Sharpening a slightly blurry video

```bash
python webm_sharpen.py blurry_video.webm sharp_video.webm
```

### Batch Processing

Process multiple files using a simple bash loop:

```bash
# Sharpen all WebM files in current directory
for file in *.webm; do
    python webm_sharpen.py "$file" "sharpened_$file"
done
```

## 📄 License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

See the [LICENSE](LICENSE) file for details or visit [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)

## 👤 Credits

**Created by:** Alexandros Panagiotakopoulos

**Website:** [alexandrospanag.github.io](https://alexandrospanag.github.io)

---

## 🐛 Troubleshooting

**"ffmpeg is not installed or not in PATH"**
- Install FFmpeg following the instructions in the Requirements section
- Verify installation with `ffmpeg -version`

**"Could not read video information"**
- Ensure the input file is a valid WebM video
- Check file permissions

**Output file is too large**
- Adjust the CRF value in the script (lower = better quality but larger file)
- Try values between 20-28 for different quality/size tradeoffs

**Video appears over-sharpened**
- Reduce the `luma_amount` parameter in the script
- Try values between 0.1-0.3 for gentler sharpening

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a star on GitHub!

---

**Happy video processing! 🎥✨**
