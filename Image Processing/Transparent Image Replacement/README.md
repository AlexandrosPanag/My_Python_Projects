# 🎨 Transparent Color Replacement Script Documentation

![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author

**Alexandros Panagiotakopoulos**

- **Website:** [https://alexandrospanag.github.io](https://alexandrospanag.github.io)
- **Date:** November 24, 2025

---

**Copyright © 2025 Alexandros Panagiotakopoulos. All Rights Reserved.**

**Version:** 1.0.0  
**Compatibility:** Python 3.6+, PIL/Pillow  
**Copyright:** Alexandros Panagiotakopoulos. All Rights Reserved Ⓒ  
**License:** Creative Commons Attribution 4.0 International License (CC BY-4.0)


## 🎯 Overview

The Transparent Color Replacement script is a powerful Python utility that transforms transparent or grayscale PNG images into vibrant colored versions. It intelligently maps the brightness values of each pixel to different hues of your chosen color, creating beautiful gradients while preserving the original image's alpha transparency.

### Key Benefits:
- **Intelligent color mapping** - Converts grayscale values to color hues
- **Transparency preservation** - Maintains original alpha channel
- **Customizable colors** - Easy to modify target color
- **Batch processing ready** - Simple to adapt for multiple files
- **High quality output** - No quality loss in conversion

---

## ✨ Features

### 🎨 Color Transformation
- Convert transparent/blank PNGs to colored versions
- Map grayscale brightness to color intensity
- Support for any target color (blue, red, green, etc.)
- Automatic gradient generation based on pixel luminance

### 🖼️ Image Processing
- **Preserves transparency:** Alpha channel remains intact
- **Smart color mixing:** Adds complementary tones for depth
- **Grayscale analysis:** Uses standard luminance formula
- **Lossless conversion:** PNG format maintained throughout

### 🔧 Easy Customization
- Simple color value modification
- Adjustable color mixing ratios
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

2. **Install Pillow Library**
   ```bash
   pip install Pillow
   ```
   
   Or if using pip3:
   ```bash
   pip3 install Pillow
   ```

### **Step-by-Step Setup:**

1. **Save the Script**
   - Create a new file named `Transparent Color Replacement.py`
   - Copy the script code into this file
   - Save it in your working directory

2. **Prepare Your Images**
   - Place PNG images in the same folder as the script
   - Or specify full file paths in the script

3. **Configure Input/Output**
   - Edit the script to set your input filename
   - Set your desired output filename
   - Adjust color values if needed

4. **Run the Script**
   ```bash
   python "Transparent Color Replacement.py"
   ```

### **File Structure:**
```
YourProject/
├── Transparent Color Replacement.py  ← The script
├── input.png                         ← Your source image
└── output_blue.png                   ← Generated output
```

---

## 🖼️ Image Format Requirements

### **Input Image Format**

**Supported Formats:**
- **PNG** - Primary format (required)
- Must support transparency (alpha channel)
- Can be transparent, semi-transparent, or opaque
- Grayscale or color images accepted

**Recommended Properties:**
- **Format:** PNG with alpha channel
- **Color Mode:** RGBA (automatic conversion if needed)
- **Bit Depth:** 8-bit or higher
- **Size:** Any dimensions supported

### **Output Image Format**

**Generated Properties:**
- **Format:** PNG with transparency
- **Color Mode:** RGBA
- **Dimensions:** Same as input image
- **Alpha Channel:** Preserved from original

### **Image Compatibility:**

✅ **Works With:**
- Transparent PNG files
- Grayscale images
- Color images (converts to grayscale first)
- Images with partial transparency
- Any image size or aspect ratio

❌ **Not Compatible:**
- JPEG files (no transparency support)
- GIF files (use PNG instead)
- BMP files (no alpha channel)
- Non-image files

### **Example Input Images:**

**Transparent Silhouettes:**
- Character sprites with transparent backgrounds
- Logo designs
- Icon sets
- Cut-out shapes

**Grayscale Images:**
- Black and white photos
- Sketches and line art
- Texture maps
- Height maps

**Partially Transparent:**
- Images with fade effects
- Soft-edged graphics
- Shadow layers
- Gradient masks

---

## 📝 Usage Guide

### **Basic Usage**

1. **Open the Script**
   - Open `Transparent Color Replacement.py` in a text editor
   - Locate the configuration section at the bottom

2. **Set Input/Output Files**
   ```python
   # Usage
   input_file = "input.png"
   output_file = "output_blue.png"
   paint_png_blue(input_file, output_file)
   ```

3. **Run the Script**
   ```bash
   python "Transparent Color Replacement.py"
   ```

4. **Check Results**
   - Find your colored image at the output path
   - Console will confirm: "Saved blue-painted image to output_blue.png"

### **Default Behavior**

**Color Mapping:**
- **Darker pixels** → Darker blue shades
- **Lighter pixels** → Lighter blue shades
- **Black (0)** → Pure dark blue
- **White (255)** → Light cyan-blue
- **Transparent areas** → Remain transparent

**Example Transformation:**
```
Original Pixel: Gray (128, 128, 128, 255)
↓
Grayscale Value: 128
↓
New Pixel: Blue (0, 38, 128, 255)
```

---

## 📊 Performance & Optimization

### **System Requirements**
- **Python:** 3.6 or higher
- **Memory:** ~10-50MB per image (depends on size)
- **CPU:** Single-threaded processing
- **Disk Space:** Output size same as input

### **Processing Speed**

**Typical Performance:**
- 1000×1000 image: ~1-2 seconds
- 2000×2000 image: ~4-8 seconds
- 4000×4000 image: ~15-30 seconds

**Factors Affecting Speed:**
- Image resolution (larger = slower)
- CPU speed
- Disk I/O speed
- Available RAM

---

### **File Size Optimization**

**Compress Output:**
```python
img.save(output_path, optimize=True, compress_level=9)
```

**Reduce Color Depth (if appropriate):**
```python
# Convert to 256 colors if suitable
img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
img.save(output_path)
```


### **Image Processing Pipeline**

1. **Load Image**
   - Opens PNG file
   - Converts to RGBA mode (if needed)
   - Loads pixel data into memory

2. **Analyze Pixels**
   - Iterates through each pixel
   - Calculates grayscale value using luminance formula
   - Preserves alpha channel

3. **Apply Color Transformation**
   - Maps grayscale to color components
   - Applies custom color formula
   - Maintains transparency

4. **Save Output**
   - Writes modified pixels to new file
   - Preserves PNG format and transparency
   - Confirms save with console message

---

### **Color Conversion Algorithm**

**Grayscale Calculation:**
```
gray = 0.299×R + 0.587×G + 0.114×B
```

**Default Color Mapping:**
```
new_R = 0
new_G = gray × 0.3
new_B = gray × 1.0
alpha = original_alpha (preserved)
```

**Output Pixel:**
```
(new_R, new_G, new_B, alpha)
```

---

### **Performance Characteristics**

**Time Complexity:** O(width × height)  
**Space Complexity:** O(width × height)  
**Processing:** Linear pass through all pixels

**Memory Usage:**
- Input image: ~4 bytes per pixel (RGBA)
- Output image: ~4 bytes per pixel (RGBA)
- Peak usage: ~2× image size

---

### **Supported Color Spaces**

**Input:**
- RGB
- RGBA
- Grayscale
- Grayscale + Alpha
- (Auto-converted to RGBA)

**Output:**
- RGBA (always)


