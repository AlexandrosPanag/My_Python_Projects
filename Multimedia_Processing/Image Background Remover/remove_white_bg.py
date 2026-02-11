#!/usr/bin/env python3
"""
White Background Remover
Removes white backgrounds from images and saves them with transparency.
"""

import argparse
from PIL import Image
import numpy as np
from pathlib import Path


def remove_white_background(input_path, output_path=None, threshold=240, tolerance=15):
    """
    Remove white background from an image.
    
    Args:
        input_path: Path to input image
        output_path: Path to save output (optional, defaults to input_transparent.png)
        threshold: RGB value above which pixels are considered white (0-255)
        tolerance: How much variation from pure white to accept
    """
    # Open image
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    img = img.convert("RGBA")
    
    # Convert to numpy array
    data = np.array(img)
    
    # Get RGB channels
    r, g, b, a = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]
    
    # Create mask for white pixels
    # A pixel is considered white if all RGB values are above threshold - tolerance
    white_mask = (r >= threshold - tolerance) & \
                 (g >= threshold - tolerance) & \
                 (b >= threshold - tolerance)
    
    # Set alpha channel to 0 for white pixels
    data[white_mask, 3] = 0
    
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


def batch_process(input_dir, output_dir=None, threshold=240, tolerance=15):
    """
    Process all images in a directory.
    
    Args:
        input_dir: Directory containing images
        output_dir: Directory to save processed images (optional)
        threshold: RGB value above which pixels are considered white
        tolerance: How much variation from pure white to accept
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
            remove_white_background(img_path, out_file, threshold, tolerance)
        except Exception as e:
            print(f"✗ Error processing {img_path.name}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Remove white backgrounds from images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single image
  python remove_white_bg.py image.jpg
  
  # Single image with custom output
  python remove_white_bg.py image.jpg -o result.png
  
  # Batch process directory
  python remove_white_bg.py -d ./images
  
  # Adjust sensitivity (lower threshold = more aggressive)
  python remove_white_bg.py image.jpg -t 230 --tolerance 20
        """
    )
    
    parser.add_argument('input', nargs='?', help='Input image file')
    parser.add_argument('-o', '--output', help='Output file path')
    parser.add_argument('-d', '--directory', help='Process all images in directory')
    parser.add_argument('--output-dir', help='Output directory for batch processing')
    parser.add_argument('-t', '--threshold', type=int, default=240,
                        help='White threshold (0-255, default: 240)')
    parser.add_argument('--tolerance', type=int, default=15,
                        help='Tolerance for white detection (default: 15)')
    
    args = parser.parse_args()
    
    if args.directory:
        batch_process(args.directory, args.output_dir, args.threshold, args.tolerance)
    elif args.input:
        remove_white_background(args.input, args.output, args.threshold, args.tolerance)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
