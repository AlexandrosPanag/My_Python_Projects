# 🎨 Image Resolution Doubler

A Python utility that doubles the resolution of images using pixel-perfect scaling while preserving the original visual appearance. Perfect for upscaling pixel art, game assets, icons, and any images where maintaining crisp edges is essential.


![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-orange)

## 👤 Author
**Alexandros Panagiotakopoulos**

## ✨ Features

- **Pixel-Perfect Scaling**: Uses nearest-neighbor interpolation for 1:1 visual reproduction
- **Batch Processing**: Process single images or entire folders
- **Format Preservation**: Maintains original file formats
- **Smart Output**: Auto-generates descriptive filenames
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Interactive & CLI**: Both command-line and interactive modes
- **Multiple Formats**: Supports PNG, JPG, JPEG, BMP, GIF, TIFF, WebP

## 📋 Requirements

- Python 3.6 or higher
- Pillow library (PIL)

## 🚀 Installation

1. **Clone or download** the script to your desired location
2. **Install dependencies**:
   ```bash
   pip install Pillow
   ```

## 🎯 Usage

### Command Line Interface

#### Single Image
```bash
python image_doubler.py input_image.png
python image_doubler.py input_image.png output_image_2x.png
```

#### Batch Process Folder
```bash
python image_doubler.py /path/to/input/folder
python image_doubler.py /path/to/input/folder /path/to/output/folder
```

### Interactive Mode

Simply run the script without arguments:
```bash
python image_doubler.py
```

The script will guide you through the process with a user-friendly menu.

## 📖 Detailed Examples

### Example 1: Single Image Processing
```bash
# Input: sprite.png (16x16 pixels)
# Output: sprite_2x.png (32x32 pixels)
python image_doubler.py sprite.png

# Custom output name
python image_doubler.py sprite.png large_sprite.png
```

### Example 2: Batch Processing
```bash
# Process all images in a folder
python image_doubler.py ./game_assets

# Process with custom output folder
python image_doubler.py ./game_assets ./upscaled_assets
```

### Example 3: Interactive Mode
```
🎨 Image Resolution Doubler v1.0
========================================
Choose an option:
1. Double a single image
2. Double all images in a folder

Enter your choice (1 or 2): 1
Enter path to image file: C:\path\to\image.png
Enter output path (press Enter for auto): 
Original size: (64, 64) (64x64)
New size: (128, 128) (128x128)
Saved doubled image to: C:\path\to\image_2x.png
```

## 🔧 Technical Details

### Interpolation Method
The script uses **nearest-neighbor interpolation** (`Image.NEAREST` in Pillow), which:
- Duplicates each pixel exactly 4 times (2x2 grid)
- Preserves sharp edges and pixel boundaries
- Maintains the original color palette
- Creates no new colors or smoothing artifacts

### File Handling
- **Input**: Automatically detects and handles various image formats
- **Output**: Preserves the original file format and metadata when possible
- **Naming**: Auto-generates output files with `_2x` suffix
- **Error Handling**: Graceful handling of invalid files and paths

### Memory Efficiency
- Opens images using context managers to ensure proper cleanup
- Processes images one at a time to minimize memory usage
- Suitable for large batch operations

## 🎮 Perfect Use Cases

### Game Development
- **Sprite Upscaling**: Double pixel art sprites for HD displays
- **Tileset Enhancement**: Scale tilesets for higher resolution games
- **UI Assets**: Upscale interface elements and icons

### Digital Art
- **Pixel Art**: Maintain crisp pixel boundaries while scaling
- **Retro Graphics**: Preserve the authentic look of vintage graphics
- **Icon Creation**: Create larger versions of small icons

### Web Development
- **Favicon Scaling**: Create multiple sizes from a single source
- **Asset Optimization**: Generate different resolutions for responsive design

## 📊 Supported Formats

| Format | Extension | Read | Write | Notes |
|--------|-----------|------|--------|--------|
| PNG | `.png` | ✅ | ✅ | Best for pixel art (lossless) |
| JPEG | `.jpg`, `.jpeg` | ✅ | ✅ | Lossy compression |
| BMP | `.bmp` | ✅ | ✅ | Uncompressed bitmap |
| GIF | `.gif` | ✅ | ✅ | Supports transparency |
| TIFF | `.tiff`, `.tif` | ✅ | ✅ | High quality format |
| WebP | `.webp` | ✅ | ✅ | Modern web format |

## ⚠️ Important Notes

### Quality Considerations
- **Best for Pixel Art**: Optimal results with pixel art and low-resolution graphics
- **Not for Photos**: Photographs may look blocky - consider other interpolation methods
- **Transparency**: Preserves alpha channels in supported formats

### Performance
- **Memory Usage**: Doubled images use 4x the memory temporarily
- **Processing Speed**: Fast for small to medium images, scales with image size
- **Batch Operations**: Efficient for processing multiple files

## 🐛 Troubleshooting

### Common Issues

**"File not found" Error**
```bash
Error: File 'image.png' not found.
```
- **Solution**: Check file path and ensure file exists
- Use absolute paths or navigate to the correct directory

**"Permission denied" Error**
```bash
PermissionError: [Errno 13] Permission denied
```
- **Solution**: Ensure write permissions to output directory
- Run with appropriate privileges if needed

**Memory Error with Large Images**
```bash
MemoryError: Unable to allocate array
```
- **Solution**: Process smaller images or increase available RAM
- Consider processing images individually rather than in batch

**Unsupported Format**
```bash
Error processing image: cannot identify image file
```
- **Solution**: Ensure file is a valid image format
- Check supported formats list above

## 📈 Version History

### v1.0.0 (Current)
- Initial release
- Single and batch image processing
- Interactive and CLI modes
- Support for major image formats
- Nearest-neighbor interpolation
- Comprehensive error handling

## 🤝 Contributing

Feel free to contribute improvements, bug fixes, or new features:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is released under the MIT License. Feel free to use, modify, and distribute as needed.

## 💡 Tips & Best Practices

### For Best Results
- **Use PNG**: Best format for pixel art and graphics with transparency
- **Start Small**: Begin with smaller test images to verify results
- **Batch Wisely**: Group similar images together for batch processing
- **Backup Originals**: Always keep original images as backups

### Performance Optimization
- **Close Other Applications**: Free up memory for large batch operations
- **Use SSD**: Faster storage improves processing speed
- **Process Overnight**: Set up large batch jobs to run during off hours

### Integration Ideas
- **Automation Scripts**: Integrate into build pipelines
- **Game Engines**: Use for asset preprocessing
- **Web Workflows**: Automate responsive image generation

---

## 🎯 Quick Start

1. **Install**: `pip install Pillow`
2. **Run**: `python image_doubler.py`
3. **Choose**: Single image or batch processing
4. **Enjoy**: Perfect 2x scaled images!

For questions, issues, or suggestions, please feel free to reach out or create an issue in the repository.

**Happy scaling!** 🚀
