# Pixel Art Noise Remover

A Python utility to remove noise and compression artifacts from pixel art images while preserving exact dimensions and pixel-perfect accuracy.

## Overview

This tool solves a common problem when creating pixel art in software like MediBang Paint: unwanted noise, semi-transparent "ghost pixels", and compression artifacts that distort clean pixel art. The script batch-processes entire folders of images, removing these artifacts while maintaining the exact size, width, height, and position of every sprite.

## Features

- 🎨 **Removes noise** - Eliminates semi-transparent artifacts and ghost pixels
- 📐 **Preserves dimensions** - Maintains exact width, height, and sprite positioning
- 🎯 **Color quantization** - Cleans up compression artifacts by snapping similar colors
- 📁 **Batch processing** - Process entire folders of images at once
- 💾 **Lossless output** - Saves as uncompressed PNG to preserve pixel-perfect quality
- ⚙️ **Configurable threshold** - Adjust sensitivity for different noise levels

## Requirements

- Python 3.6+
- PIL/Pillow
- NumPy

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/yourusername/pixel-art-cleaner.git
cd pixel-art-cleaner
```

2. Install dependencies:
```bash
pip install pillow numpy
```

## Usage

### Basic Usage

Process all PNG images in a folder (creates a `cleaned` subfolder):

```bash
python pixel_art_cleaner.py /path/to/your/images
```

### Specify Output Folder

```bash
python pixel_art_cleaner.py /path/to/input /path/to/output
```

### Adjust Noise Threshold

The threshold parameter (0-255) determines how aggressive the noise removal is. Lower values remove only very transparent pixels, higher values are more aggressive:

```bash
python pixel_art_cleaner.py /path/to/input /path/to/output 15
```

**Recommended thresholds:**
- `5-10` - Light noise removal (default: 10)
- `10-20` - Medium noise removal
- `20-30` - Aggressive noise removal

### Examples

```bash
# Basic: Clean all images in 'weapons' folder
python pixel_art_cleaner.py ./weapons

# Custom output folder
python pixel_art_cleaner.py ./weapons ./weapons_cleaned

# More aggressive noise removal
python pixel_art_cleaner.py ./sprites ./sprites_clean 20
```

## How It Works

The script uses a multi-step process to clean pixel art:

1. **Alpha Threshold Filtering** - Pixels with alpha values below the threshold are made fully transparent, removing noise
2. **Alpha Normalization** - Remaining pixels with high alpha (>200) are snapped to fully opaque (255)
3. **Color Quantization** - RGB values are quantized to multiples of 8, reducing compression artifacts
4. **Lossless Export** - Images are saved as PNG with compression level 0 to preserve pixel accuracy

### Technical Details

- Input: PNG images (supports both `.png` and `.PNG` extensions)
- Output: RGBA PNG with no compression
- Processing: NumPy array manipulation for efficient batch processing
- Preservation: Exact dimensions, no resampling or resizing

## Use Cases

- Cleaning pixel art exported from MediBang Paint
- Removing compression artifacts from game sprites
- Preparing pixel art for game engines (Unity, Godot, etc.)
- Batch processing sprite sheets
- Cleaning up pixel art from any source with unwanted noise

## Common Issues

### "No PNG files found"
Make sure your folder contains `.png` files and the path is correct.

### "Read-only file system" error
The script cannot write to the input folder. Specify a different output folder:
```bash
python pixel_art_cleaner.py /read-only/folder /writable/output
```

### Output looks too aggressive
Lower the threshold value:
```bash
python pixel_art_cleaner.py ./images ./output 5
```

### Some details are lost
The color quantization might be too aggressive. You can modify the `quantize_level` variable in the script (default: 8). Set it to a lower value like 4 for gentler quantization.

## Customization

You can modify the script to adjust cleaning behavior:

- **`threshold`** - Alpha cutoff for noise removal (default: 10)
- **`quantize_level`** - Color quantization step (default: 8)
  - Located on line 45: `quantize_level = 8`
  - Lower values (2-4) = gentler, higher values (8-16) = more aggressive

## License

This project is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

You are free to:
- **Share** - copy and redistribute the material in any medium or format
- **Adapt** - remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** - You must give appropriate credit, provide a link to the license, and indicate if changes were made.

See the [LICENSE](LICENSE) file for details or visit: https://creativecommons.org/licenses/by/4.0/

## Credits

**Created by:** Alexandros Panagiotakopoulos

---

**Author:** Alexandros Panagiotakopoulos  
**License:** CC BY 4.0  
**Year:** 2026
