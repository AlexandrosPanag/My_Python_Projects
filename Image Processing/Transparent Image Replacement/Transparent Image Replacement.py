# Transparent Color Replacement.py
# This script processes a PNG image, replacing its colors with shades of blue
# based on the original grayscale values while preserving transparency.
# LICENSE: CC4.0 BY-4.0
# Copyright (C) Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# Date: 24/11/2025

from PIL import Image

def paint_png_blue(input_path, output_path):
    # Open the image
    img = Image.open(input_path).convert('RGBA')
    pixels = img.load()
    width, height = img.size
    
    # Process each pixel
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Calculate grayscale value (0-255)
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            
            # Map grayscale to blue hues
            # Darker gray -> darker blue, lighter gray -> lighter blue
            blue_value = gray
            new_r = 0
            new_g = int(gray * 0.3)  # Add a bit of green for variety
            new_b = blue_value
            
            # Keep original alpha
            pixels[x, y] = (new_r, new_g, new_b, a)
    
    # Save the result
    img.save(output_path)
    print(f"Saved blue-painted image to {output_path}")

# Usage
input_file = "input.png"
output_file = "output_blue.png"
paint_png_blue(input_file, output_file)
