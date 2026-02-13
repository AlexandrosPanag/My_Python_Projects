#Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 14/02/2025
#alexandrospanag.github.io

#!/usr/bin/env python3
"""
Pixel Art Noise Cleaner
Removes noise and artifacts from pixel art while preserving exact dimensions and positions.
Processes all images in a specified folder.

Usage: python pixel_art_cleaner.py /folder/here
"""

import os
from PIL import Image
import numpy as np
from pathlib import Path


def clean_pixel_art(image_path, output_path, alpha_threshold=128, color_threshold=10):
    """
    Clean pixel art by removing semi-transparent pixels and color noise.
    
    Args:
        image_path: Input image path
        output_path: Output image path
        alpha_threshold: Alpha values below this become fully transparent (0-255)
        color_threshold: How much color variation to tolerate in similar pixels
    """
    # Open image
    img = Image.open(image_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Convert to numpy array for processing
    data = np.array(img)
    
    # Get alpha channel
    alpha = data[:, :, 3]
    
    # Clean alpha channel - make semi-transparent pixels either fully transparent or opaque
    # This removes the "fuzzy edges" that editors add
    alpha_cleaned = np.where(alpha < alpha_threshold, 0, 255)
    
    # Apply cleaned alpha back
    data[:, :, 3] = alpha_cleaned
    
    # Optional: Remove color noise from fully transparent pixels
    # (set them to a consistent value to reduce file size)
    transparent_mask = alpha_cleaned == 0
    data[transparent_mask, 0:3] = 0  # Set RGB to black for transparent pixels
    
    # Create cleaned image
    cleaned_img = Image.fromarray(data, 'RGBA')
    
    # Save with no compression artifacts
    cleaned_img.save(output_path, 'PNG', compress_level=9, optimize=False)
    
    return cleaned_img


def process_folder(input_folder, output_folder=None, alpha_threshold=128, 
                   color_threshold=10, suffix="_cleaned"):
    """
    Process all images in a folder.
    
    Args:
        input_folder: Folder containing images to clean
        output_folder: Folder to save cleaned images (default: same as input with suffix)
        alpha_threshold: Alpha threshold for transparency (0-255)
        color_threshold: Color variation tolerance
        suffix: Suffix to add to cleaned filenames
    """
    input_path = Path(input_folder)
    
    if not input_path.exists():
        print(f"Error: Input folder '{input_folder}' does not exist!")
        return
    
    # Set output folder
    if output_folder is None:
        output_path = input_path / "cleaned"
    else:
        output_path = Path(output_folder)
    
    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Supported image formats
    image_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'}
    
    # Find all images
    image_files = [f for f in input_path.iterdir() 
                   if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not image_files:
        print(f"No images found in '{input_folder}'")
        return
    
    print(f"Found {len(image_files)} images to process")
    print(f"Output folder: {output_path}")
    print(f"Alpha threshold: {alpha_threshold}")
    print("-" * 50)
    
    processed = 0
    for img_file in image_files:
        try:
            # Create output filename
            output_file = output_path / f"{img_file.stem}{suffix}{img_file.suffix}"
            
            print(f"Processing: {img_file.name}...", end=" ")
            
            # Clean the image
            clean_pixel_art(img_file, output_file, alpha_threshold, color_threshold)
            
            # Verify dimensions are preserved
            original = Image.open(img_file)
            cleaned = Image.open(output_file)
            
            if original.size == cleaned.size:
                print(f"✓ ({original.size[0]}x{original.size[1]})")
                processed += 1
            else:
                print(f"⚠ Size mismatch! {original.size} -> {cleaned.size}")
                
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("-" * 50)
    print(f"Successfully processed {processed}/{len(image_files)} images")
    print(f"Cleaned images saved to: {output_path}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Clean pixel art noise while preserving dimensions and positions"
    )
    parser.add_argument(
        "input_folder",
        help="Folder containing images to clean"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output folder (default: input_folder/cleaned)",
        default=None
    )
    parser.add_argument(
        "-a", "--alpha-threshold",
        type=int,
        default=128,
        help="Alpha threshold (0-255). Pixels below this become transparent (default: 128)"
    )
    parser.add_argument(
        "-c", "--color-threshold",
        type=int,
        default=10,
        help="Color variation tolerance (default: 10)"
    )
    parser.add_argument(
        "-s", "--suffix",
        default="_cleaned",
        help="Suffix for cleaned filenames (default: _cleaned)"
    )
    
    args = parser.parse_args()
    
    process_folder(
        args.input_folder,
        args.output,
        args.alpha_threshold,
        args.color_threshold,
        args.suffix
    )
