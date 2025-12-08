# 🎬 Video Resizer and Zoom Tool Documentation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author
**Alexandros Panagiotakopoulos**
- **Date:** December 8, 2025

---

## 📄 License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit
- **NonCommercial** — You may not use the material for commercial purposes
- **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license


---

## 🎯 Overview

The Video Resizer and Zoom Tool is a powerful Python utility that transforms videos into a portrait format (464x864) with customizable zoom effects. It intelligently resizes and crops videos to fit mobile-friendly dimensions while maintaining high quality output in WebM format with VP9 codec.

### Key Benefits:
- **Intelligent zoom and crop** - Focus on specific areas of your video
- **Mobile-optimized output** - Perfect 464x864 portrait format
- **High quality encoding** - VP9/Opus codecs for efficient compression
- **Customizable positioning** - Adjustable vertical offset for framing
- **Batch processing ready** - Simple command-line interface
- **No quality loss** - Maintains visual fidelity with smart encoding

---

## ✨ Features

### 🎬 Video Transformation
- Convert any video format to 464x864 portrait format
- Apply customizable zoom effects (1.0x to any factor)
- Vertical offset control for precise framing
- Support for any input video format supported by FFmpeg

### 🖼️ Video Processing
- **Smart cropping:** Centers content with adjustable vertical positioning
- **Quality preservation:** VP9 codec with optimized bitrate settings
- **Audio retention:** Opus audio codec maintains sound quality
- **Automatic scaling:** Intelligently resizes to target dimensions

### 🔧 Easy Customization
- Simple command-line parameters
- Adjustable zoom factor (default 1.5x)
- Vertical offset control (-1.0 to 1.0)
- Configurable input/output paths
- No complex coding required

---

## 📦 Installation

### **Prerequisites:**

1. **Python Installation**
   - Download Python 3.6 or higher from [python.org](https://python.org)
   - During installation, check "Add Python to PATH"
   - Verify installation:
     ```bash
     python --version
     ```

2. **Install FFmpeg**
   
   **Windows:**
   ```bash
   winget install ffmpeg
   ```
   Or download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   
   **macOS:**
   ```bash
   brew install ffmpeg
   ```
   
   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
   
   **Verify FFmpeg installation:**
   ```bash
   ffmpeg -version
   ```

### **Step-by-Step Setup:**

1. **Save the Script**
   - Create a new file named `video_resizer.py`
   - Copy the script code into this file
   - Save it in your working directory

2. **Prepare Your Videos**
   - Place WebM videos in the same folder as the script
   - Or specify full file paths when running

3. **Make Script Executable (Optional - Linux/macOS)**
   ```bash
   chmod +x video_resizer.py
   ```

4. **Run the Script**
   ```bash
   python video_resizer.py input.webm
   ```

### **File Structure:**
```
YourProject/
├── video_resizer.py          ← The script
├── input.webm               ← Your source video
└── input_resized.webm       ← Generated output
```

---

## 🎥 Video Format Requirements

### **Input Video Format**

**Supported Formats:**
- **WebM** - Primary format (required input)
- Must be a valid video file
- Any resolution supported
- Audio optional but preserved if present

**Recommended Properties:**
- **Format:** WebM with VP8/VP9 codec
- **Resolution:** Any (will be resized)
- **Aspect Ratio:** Any (will be cropped to fit)
- **Framerate:** Any (preserved in output)

### **Output Video Format**

**Generated Properties:**
- **Format:** WebM (VP9 + Opus)
- **Resolution:** 464x864 (fixed)
- **Video Codec:** VP9 (libvpx-vp9)
- **Audio Codec:** Opus (libopus)
- **Video Bitrate:** 1 Mbps
- **Audio Bitrate:** 128 kbps
- **CRF Quality:** 30 (good balance of quality/size)

### **Video Compatibility:**

✅ **Works With:**
- WebM format videos
- Any input resolution
- Videos with or without audio
- Any framerate
- Any aspect ratio

❌ **Not Compatible:**
- Non-WebM input formats (must convert first)
- Corrupted video files
- Audio-only files

### **Example Input Videos:**

**Portrait Videos:**
- Mobile phone recordings
- TikTok-style content
- Vertical social media videos
- Interview clips

**Landscape Videos:**
- YouTube videos (will be cropped)
- Movie clips
- Gaming footage
- Screen recordings

**Common Use Cases:**
- Converting landscape to portrait for social media
- Creating mobile-optimized video content
- Zooming into specific areas of footage
- Preparing videos for Instagram Stories/Reels

---

## 📝 Usage Guide

### **Basic Usage**

1. **Simple Resize (Default Settings)**
   ```bash
   python video_resizer.py input.webm
   ```
   - Uses default 1.5x zoom
   - Centers content vertically
   - Outputs to `input_resized.webm`

2. **Specify Output File**
   ```bash
   python video_resizer.py input.webm output.webm
   ```

3. **Custom Zoom Factor**
   ```bash
   python video_resizer.py input.webm output.webm 1.8
   ```
   - Zoom factor: 1.8x (80% zoom in)
   - Good for tight character framing

4. **Custom Vertical Positioning**
   ```bash
   python video_resizer.py input.webm output.webm 1.5 -0.2
   ```
   - Zoom: 1.5x
   - Y-offset: -0.2 (shifts frame slightly upward)
   - Useful for centering faces in portrait videos

### **Command-Line Parameters**

```bash
python video_resizer.py <input> [output] [zoom_factor] [y_offset]
```

**Parameters:**
- `input` - Input WebM video file (required)
- `output` - Output WebM video file (optional, auto-generated if omitted)
- `zoom_factor` - Zoom multiplier, ≥1.0 (optional, default: 1.5)
- `y_offset` - Vertical position, -1.0 to 1.0 (optional, default: 0.0)

**Y-Offset Guide:**
- `-1.0` - Frame focused on top of video
- `-0.5` - Upper portion emphasized
- `0.0` - Perfectly centered (default)
- `0.5` - Lower portion emphasized
- `1.0` - Frame focused on bottom of video

### **Default Behavior**

**Processing Pipeline:**
1. Reads input WebM video
2. Scales video by zoom factor
3. Crops to 464x864 from center
4. Applies vertical offset if specified
5. Encodes with VP9/Opus codecs
6. Saves to output file

**Example Transformation:**
```
Input: 1920x1080 landscape video
↓
Zoom 1.5x: 696x1296 intermediate
↓
Crop 464x864: Center extraction with offset
↓
Output: 464x864 portrait video
```

---

## 🎨 Zoom and Positioning Examples

### **Zoom Factor Guide**

**1.0x (No Zoom):**
- Fits entire video width/height
- Maximum area visible
- Best for content that fits naturally

**1.5x (Default - 50% Zoom):**
- Balanced crop
- Good for most content
- Removes outer ~25% on each side

**1.8x (80% Zoom):**
- Tight framing
- Great for character focus
- Removes outer ~40% on each side

**2.0x (100% Zoom):**
- Very tight crop
- Close-up effect
- Removes outer ~50% on each side

### **Positioning Examples**

**Center Face in Portrait:**
```bash
python video_resizer.py input.webm output.webm 1.5 -0.2
```

**Focus on Upper Action:**
```bash
python video_resizer.py input.webm output.webm 1.8 -0.5
```

**Show Bottom Subtitles:**
```bash
python video_resizer.py input.webm output.webm 1.5 0.3
```

**Dramatic Close-Up:**
```bash
python video_resizer.py input.webm output.webm 2.5 0.0
```

---

## 📊 Performance & Optimization

### **System Requirements**
- **Python:** 3.6 or higher
- **FFmpeg:** Latest stable version
- **Memory:** ~500MB-2GB (depends on video size)
- **CPU:** Multi-core recommended for faster encoding
- **Disk Space:** Output size typically 50-70% of input

### **Processing Speed**

**Typical Performance:**
- 30-second video (1080p): ~15-30 seconds
- 1-minute video (1080p): ~30-60 seconds
- 5-minute video (1080p): ~2-5 minutes

**Factors Affecting Speed:**
- Input video resolution (higher = slower)
- Video duration
- CPU speed and core count
- Disk I/O speed
- Encoding quality settings

### **Quality vs. File Size**

**Current Settings (Balanced):**
- CRF: 30 (good quality)
- Video Bitrate: 1 Mbps
- Audio Bitrate: 128 kbps

**Higher Quality (Larger Files):**
```python
# Modify in script:
'-crf', '23',      # Better quality
'-b:v', '2M',      # Higher bitrate
```

**Smaller Files (Lower Quality):**
```python
# Modify in script:
'-crf', '35',      # Lower quality
'-b:v', '500k',    # Lower bitrate
```

### **Video Processing Pipeline**

1. **Probe Video**
   - Reads input video metadata
   - Extracts dimensions using ffprobe
   - Validates video stream exists

2. **Calculate Dimensions**
   - Computes zoom dimensions
   - Calculates crop offsets
   - Applies vertical positioning

3. **Build FFmpeg Filter**
   - Creates scale filter
   - Adds crop filter with offsets
   - Combines into filter chain

4. **Encode Video**
   - Applies VP9 video codec
   - Applies Opus audio codec
   - Writes to output file

5. **Confirm Success**
   - Reports completion
   - Shows output path

---

## 🔧 Advanced Customization

### **Modify Encoding Settings**

Edit the script to customize encoding parameters:

```python
# Find this section in resize_and_zoom_video():
cmd = [
    'ffmpeg',
    '-i', input_path,
    '-vf', vf,
    '-c:v', 'libvpx-vp9',
    '-crf', '30',          # Change: 15-35 (lower = better)
    '-b:v', '1M',          # Change: 500k-5M (higher = better)
    '-c:a', 'libopus',
    '-b:a', '128k',        # Change: 64k-320k (higher = better)
    '-y',
    output_path
]
```

### **Change Target Resolution**

```python
# Modify these values:
target_width = 464   # Change to your width
target_height = 864  # Change to your height
```

### **Add Custom Filters**

```python
# Add additional FFmpeg filters:
vf = f"scale={zoom_width}:{zoom_height},crop={target_width}:{target_height}:{crop_x}:{crop_y},unsharp"
# Adds sharpening filter
```

---

## 🛠️ Troubleshooting

### **Common Issues**

**"ffmpeg not found"**
- FFmpeg is not installed or not in PATH
- Solution: Install FFmpeg and ensure it's accessible from command line

**"No video stream found"**
- Input file is corrupted or not a valid video
- Solution: Verify input file plays in a media player

**"Input file must be in WebM format"**
- Script only accepts .webm input files
- Solution: Convert your video to WebM first using FFmpeg

**Output video is too zoomed in/out**
- Zoom factor not suitable for content
- Solution: Adjust zoom_factor parameter (try 1.2 to 2.0 range)

**Video is cut off at top/bottom**
- Vertical offset needs adjustment
- Solution: Use y_offset parameter to reposition

### **Error Messages**

**FFmpeg stderr output**
- Check the error message for specific codec/format issues
- Ensure input video is not corrupted
- Verify FFmpeg supports the input format

---

## 💡 Tips and Best Practices

### **Choosing Zoom Factor**
- Start with default 1.5x
- Increase for landscape-to-portrait conversions
- Use 1.8-2.0x for character-focused content
- Use 1.0-1.3x if you want more context visible

### **Vertical Positioning**
- Use -0.2 to -0.3 for face-centered shots
- Use positive values if subtitles are at bottom
- Test different offsets to find optimal framing

### **Quality Optimization**
- For social media: Current settings (CRF 30) are good
- For archival: Use CRF 23 and higher bitrate
- For quick previews: Use CRF 35 and lower bitrate

### **Batch Processing**
```bash
# Process multiple files:
for file in *.webm; do
    python video_resizer.py "$file" "resized_$file" 1.5 0.0
done
```

---

## 📈 Technical Specifications

### **Video Processing Algorithm**

**Dimension Calculation:**
```
zoom_width = target_width × zoom_factor
zoom_height = target_height × zoom_factor
```

**Crop Offset Calculation:**
```
crop_x = (zoom_width - target_width) / 2
max_y_offset = (zoom_height - target_height) / 2
crop_y = max_y_offset + (max_y_offset × y_offset)
```

**FFmpeg Filter Chain:**
```
scale=WIDTH:HEIGHT,crop=464:864:X:Y
```

### **Codec Information**

**VP9 Video Codec:**
- Modern, efficient compression
- Better quality than VP8 at same bitrate
- Wide browser support
- Good for streaming

**Opus Audio Codec:**
- High-quality audio compression
- Designed for internet streaming
- Low latency
- Supports wide range of bitrates

### **Performance Characteristics**

**Time Complexity:** O(width × height × frames)  
**Space Complexity:** O(video_duration × bitrate)  
**Processing:** Sequential frame encoding

**Memory Usage:**
- Input buffer: ~100-500MB
- Processing buffer: ~200-1000MB
- Output buffer: ~100-500MB
- Peak usage: ~2-3GB for long videos

---

## 📚 Additional Resources

### **FFmpeg Documentation**
- Official docs: [ffmpeg.org/documentation.html](https://ffmpeg.org/documentation.html)
- VP9 encoding guide: [trac.ffmpeg.org/wiki/Encode/VP9](https://trac.ffmpeg.org/wiki/Encode/VP9)

### **Video Encoding Resources**
- VP9 quality settings: CRF 15-35 range
- Opus audio: 64k-320k bitrate range
- WebM container format specifications

### **Command-Line Tips**
- Use `-y` flag to overwrite without prompting
- Use `-n` flag to never overwrite existing files
- Add `-loglevel quiet` for silent processing

---

**Happy Video Processing! 🎬**
