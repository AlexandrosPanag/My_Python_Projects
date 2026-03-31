# AddPadding

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-yellow.svg)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-green.svg)

## 👤 Author

**Alexandros Panagiotakopoulos**
[alexandrospanag.github.io](https://alexandrospanag.github.io)

A simple, lossless image padding utility that adds a border of any colour around any image — at its native resolution. No resizing, no stretching, no resampling. Just clean padding.

## ✨ Features

- 🎯 **Pixel-perfect** — Original image content is never altered or resampled
- 📐 **Flexible sizing** — Specify padding as fixed pixels or as a percentage of the image dimensions
- 🎨 **Custom colour** — Any RGB colour for the border (default: black)
- 🔄 **Per-side control** — Independent top / right / bottom / left values
- 🖼️ **Wide format support** — Works with JPEG, PNG, WEBP, BMP, TIFF, and more
- 🧩 **Alpha-aware** — Preserves transparency in RGBA and palette images
- ⚡ **Zero dependencies beyond Pillow** — Lightweight and fast

## 📦 Installation

**Requirements:** Python 3.7+ and [Pillow](https://pillow.readthedocs.io/).

```bash
pip install Pillow
```

Then simply download `add_padding.py` — no further setup needed.

## 🚀 Usage

### Basic Examples

```bash
# Uniform padding — 50 px black border on all sides
python add_padding.py input.jpg output.jpg --padding 50

# Per-side pixel padding
python add_padding.py input.jpg output.jpg --top 20 --right 40 --bottom 20 --left 40

# Uniform percentage — 10 % of each dimension on all sides
python add_padding.py input.jpg output.jpg --percent 10

# Per-side percentage
python add_padding.py input.jpg output.jpg --percent-top 5 --percent-right 10 --percent-bottom 5 --percent-left 10

# Custom colour (white border)
python add_padding.py input.jpg output.jpg --padding 30 --color 255 255 255
```

### CLI Reference

```
positional arguments:
  input        Input image path
  output       Output image path
```

#### Pixel Padding (fixed px)

| Argument | Type | Description |
|----------|------|-------------|
| `--padding` | int | Uniform padding in pixels on all four sides |
| `--top` | int | Top-edge padding in pixels |
| `--right` | int | Right-edge padding in pixels |
| `--bottom` | int | Bottom-edge padding in pixels |
| `--left` | int | Left-edge padding in pixels |

#### Percent Padding (scales with image size)

Horizontal sides (`--percent-right`, `--percent-left`) are relative to image **width**.
Vertical sides (`--percent-top`, `--percent-bottom`) are relative to image **height**.

| Argument | Type | Description |
|----------|------|-------------|
| `--percent` | float | Uniform padding as % of image dimension on all sides |
| `--percent-top` | float | Top-edge padding as % of image height |
| `--percent-right` | float | Right-edge padding as % of image width |
| `--percent-bottom` | float | Bottom-edge padding as % of image height |
| `--percent-left` | float | Left-edge padding as % of image width |

#### Colour

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--color R G B` | int int int | `0 0 0` | Padding colour as separate R G B values (0–255 each) |

### Priority Rules

When multiple padding arguments are given, the following precedence applies:

1. `--percent` — overrides all other arguments, sets all four sides at once
2. `--padding` — sets all four sides in pixels
3. Per-side flags (`--top`, `--percent-right`, etc.) — mixed freely; percentage wins over pixel for the same side

## 🎯 Use Cases

### Photography & Print Prep
Add a clean white or black matte around photos before printing or framing, without touching the original pixels.

### Social Media & Web
Pad images to a target aspect ratio (e.g., square for Instagram) by adding equal borders to the shorter sides.

### Batch Processing
Use `--percent` so the border scales consistently regardless of image resolution — ideal for processing folders of mixed-size images.

### Watermark Clearance
Add bottom or side padding to make room for a watermark or caption bar without cropping the image.

### Presentations & Documents
Frame screenshots or diagrams with a neutral border so they stand out against white slide backgrounds.

## 🔧 Technical Details

### How It Works

1. **Open** the input image with Pillow, preserving the original mode (RGB, RGBA, P, etc.)
2. **Resolve** pixel values — percentage arguments are converted using the image's native dimensions
3. **Create** a new blank canvas of the expanded size, filled with the specified padding colour
4. **Paste** the original image onto the canvas at the offset `(left, top)` — no resampling occurs
5. **Save** the result; the output format is inferred from the file extension

### Colour Mode Handling

| Input mode | Behaviour |
|------------|-----------|
| RGB | Padding uses the specified `(R, G, B)` colour |
| RGBA | Converted in-place; padding uses `(R, G, B, 255)` — fully opaque |
| P (palette) | Converted to RGBA first; padding uses `(R, G, B, 255)` |
| Other (L, CMYK, …) | Converted to RGB; padding uses the specified colour |

### Console Output

```
Original size : 1920 × 1080 px
Padding (px)  : top=50  right=50  bottom=50  left=50
New size      : 2020 × 1180 px
Saved to      : output.jpg
```

## 🐛 Troubleshooting

### Output looks identical to input
- Verify that at least one padding argument was supplied (the default for all sides is 0).
- Check the console output — it prints the resolved pixel values before saving.

### Colour looks wrong
- Ensure R, G, B values are in the range 0–255 and passed as three separate integers: `--color 255 0 0`.
- For RGBA images the padding is always fully opaque (`alpha = 255`), regardless of the specified colour.

### Unexpected file size or quality loss (JPEG)
- JPEG re-encodes on save, so some quality change is expected. Use PNG output (`output.png`) for fully lossless results.

### `ModuleNotFoundError: No module named 'PIL'`
- Install Pillow: `pip install Pillow`

## 📝 Changelog

### Version 1.0.0 (2026-03-31)
- Initial release
- Fixed-pixel and percentage-based padding
- Per-side control (top / right / bottom / left)
- Custom RGB padding colour
- Alpha channel and palette image support
- Priority resolution for mixed pixel/percent arguments

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**.

You are free to:
* ✅ **Share** — copy and redistribute in any medium or format
* ✅ **Adapt** — remix, transform, and build upon the material

Under the following terms:
* 📝 **Attribution** — You must give appropriate credit and indicate if changes were made
* 🚫 **NonCommercial** — You may not use the material for commercial purposes
* 🔁 **ShareAlike** — Derivatives must be distributed under the same license

[View Full License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## 👏 Credits

* **Author**: Alexandros Panagiotakopoulos
* **Technologies**: Python 3, [Pillow](https://pillow.readthedocs.io/)

---

**Made with ❤️ for anyone who just needs a border around their image**
