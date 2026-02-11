#!/usr/bin/env python3
"""
White Background Remover
Removes white backgrounds from images and saves them with transparency.
"""

import argparse
from PIL import Image
import numpy as np
from pathlib import Path


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def remove_white_background(input_path, output_path=None, threshold=240, tolerance=15, target_color=None):
    """
    Remove white background or specific color from an image.
    
    Args:
        input_path: Path to input image
        output_path: Path to save output (optional, defaults to input_transparent.png)
        threshold: RGB value above which pixels are considered white (0-255) - ignored if target_color is set
        tolerance: How much variation from target color to accept
        target_color: Hex color code (e.g., '#F6EED7') or RGB tuple to remove instead of white
    """
    # Open image
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    img = img.convert("RGBA")
    
    # Convert to numpy array
    data = np.array(img)
    
    # Get RGB channels
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
    
    if target_color:
        # Convert hex to RGB if needed
        if isinstance(target_color, str):
            target_rgb = hex_to_rgb(target_color)
        else:
            target_rgb = target_color
        
        # Create mask for target color pixels
        # A pixel matches if all RGB values are within tolerance of target
        color_mask = (np.abs(r - target_rgb[0]) <= tolerance) & \
                     (np.abs(g - target_rgb[1]) <= tolerance) & \
                     (np.abs(b - target_rgb[2]) <= tolerance)
    else:
        # Create mask for white pixels
        # A pixel is considered white if all RGB values are above threshold - tolerance
        color_mask = (r >= threshold - tolerance) & \
                     (g >= threshold - tolerance) & \
                     (b >= threshold - tolerance)
    
    # Set alpha channel to 0 for matched pixels
    data[color_mask, 3] = 0
    
    # Create new image from modified data
    result = Image.fromarray(data, mode='RGBA')
    
    # Determine output path
    if output_path is None:
        input_path_obj = Path(input_path)
        output_path = input_path_obj.parent / f"{input_path_obj.stem}_transparent.png"
    
    # Save result
    result.save(output_path, 'PNG')
    print(f"✓ Saved: {output_path}")
    
    return output_path


def batch_process(input_dir, output_dir=None, threshold=240, tolerance=15, target_color=None):
    """
    Process all images in a directory.
    
    Args:
        input_dir: Directory containing images
        output_dir: Directory to save processed images (optional)
        threshold: RGB value above which pixels are considered white
        tolerance: How much variation from target color to accept
        target_color: Hex color code or RGB tuple to remove instead of white
    """
    input_path = Path(input_dir)
    
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = input_path
    
    # Supported image formats
    formats = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.tiff', '*.webp']
    
    images = []
    for fmt in formats:
        images.extend(input_path.glob(fmt))
        images.extend(input_path.glob(fmt.upper()))
    
    if not images:
        print(f"No images found in {input_dir}")
        return
    
    print(f"Processing {len(images)} images...")
    
    for img_path in images:
        try:
            out_file = output_path / f"{img_path.stem}_transparent.png"
            remove_white_background(img_path, out_file, threshold, tolerance, target_color)
        except Exception as e:
            print(f"✗ Error processing {img_path.name}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Remove white backgrounds from images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Remove white background
  python remove_white_bg.py image.jpg
  
  # Remove specific color (beige #F6EED7)
  python remove_white_bg.py image.jpg -c beige
  python remove_white_bg.py image.jpg -c "#F6EED7"
  
  # Single image with custom output
  python remove_white_bg.py image.jpg -o result.png
  
  # Batch process directory with color removal
  python remove_white_bg.py -d ./images -c beige
  
  # Adjust sensitivity (lower tolerance = more strict matching)
  python remove_white_bg.py image.jpg -c "#F6EED7" --tolerance 20
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input image file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-d', '--directory', help='Process all images in directory')
    parser.add_argument('--output-dir', help='Output directory for batch processing')
    parser.add_argument('-c', '--color', help='Target color to remove (hex code like #F6EED7 or "beige")')
    parser.add_argument('-t', '--threshold', type=int, default=240,
                        help='White threshold (0-255, default: 240) - ignored if --color is set')
    parser.add_argument('--tolerance', type=int, default=15,
                        help='Tolerance for color detection (default: 15)')
    
    args = parser.parse_args()
    
    # Color presets
    color_presets = {
        'beige': '#F6EED7',
        'cream': '#F6EED7',
        'lightbeige': '#F6EED7'
    }
    
    # Parse target color
    target_color = None
    if args.color:
        # Check if it's a preset name
        if args.color.lower() in color_presets:
            target_color = color_presets[args.color.lower()]
        else:
            target_color = args.color
    
    if args.directory:
        batch_process(args.directory, args.output_dir, args.threshold, args.tolerance, target_color)
    elif args.input:
        remove_white_background(args.input, args.output, args.threshold, args.tolerance, target_color)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()