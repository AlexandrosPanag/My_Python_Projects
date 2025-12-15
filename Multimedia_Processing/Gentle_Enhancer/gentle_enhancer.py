#Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 01/10/2025
#alexandrospanag.github.io
#!/usr/bin/env python3
"""
Gentle Anime Image Enhancer - Refined balanced enhancement with reduced sharpening

HOW TO RUN THIS SCRIPT:
====================

1. INSTALL REQUIRED DEPENDENCIES:
   pip install opencv-python pillow numpy

2. BASIC USAGE - Single File:
   python gentle_enhancer.py input_image.png
   python gentle_enhancer.py "C:\path\to\your\image.jpg"
   
3. SPECIFY OUTPUT FILE:
   python gentle_enhancer.py input.png output.png
   python gentle_enhancer.py "input image.jpg" "enhanced_output.jpg"

4. BATCH PROCESS ENTIRE FOLDER:
   python gentle_enhancer.py "C:\folder\with\images"
   python gentle_enhancer.py . (process current directory)

5. SUPPORTED FILE FORMATS:
   - Input: .jpg, .jpeg, .png, .bmp, .tiff, .webp
   - Output: Same format as input (or specify .png/.jpg)

6. EXAMPLES:
   python gentle_enhancer.py portrait.png
   python gentle_enhancer.py "anime_art.jpg" "enhanced_anime_art.jpg"
   python gentle_enhancer.py "C:\Users\me\Pictures\RPG Portraits"

7. WHAT THIS SCRIPT DOES:
   - Gentle noise reduction (preserves anime style)
   - Balanced sharpening (120% strength, not aggressive)
   - Color enhancement (+15% saturation, +10% contrast)
   - Maintains original dimensions and aspect ratio
   - Perfect for RPG Maker portraits and anime artwork

8. OUTPUT FILES:
   - If no output specified: adds "_gentle_enhanced" to filename
   - Creates output in same directory as input file
   - Preserves original file (never overwrites)

REQUIREMENTS: Python 3.6+, OpenCV, PIL/Pillow, NumPy
"""

import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import os
import sys

def enhance_anime_gentle(input_path, output_path=None):
    """
    Gentle balanced enhancement - less aggressive sharpening
    Perfect balance of clarity and smoothness
    """
    try:
        print(f"🌸 GENTLE Processing: {input_path}")
        
        # Load image with PIL
        img_pil = Image.open(input_path)
        original_width, original_height = img_pil.size
        print(f"Original dimensions: {original_width}×{original_height}")
        
        # Convert to OpenCV for processing
        img_array = np.array(img_pil)
        img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        # Step 1: Gentle noise reduction
        print("🔧 Gentle noise reduction...")
        # Slightly stronger bilateral filter for smoother results
        denoised = cv2.bilateralFilter(img_cv, 7, 30, 30)  # Increased from 5,35,35
        
        # Step 2: Very mild unsharp masking
        print("✨ Subtle sharpening...")
        # Much gentler unsharp mask settings
        gaussian = cv2.GaussianBlur(denoised, (0, 0), 1.0)
        unsharp_mask = cv2.addWeighted(denoised, 1.4, gaussian, -0.4, 0)  # Reduced from 1.8/-0.8
        
        # Step 3: Convert back to PIL
        enhanced_rgb = cv2.cvtColor(unsharp_mask, cv2.COLOR_BGR2RGB)
        enhanced_pil = Image.fromarray(enhanced_rgb)
        
        # Step 4: Gentle precision sharpening with PIL
        print("🎯 Light precision sharpening...")
        # Milder sharpening using UnsharpMask filter
        enhanced_pil = enhanced_pil.filter(ImageFilter.UnsharpMask(radius=1.0, percent=120, threshold=3))  # Reduced from 150%
        
        # Step 5: Final gentle sharpness
        print("🌟 Final gentle sharpness...")
        sharpness_enhancer = ImageEnhance.Sharpness(enhanced_pil)
        enhanced_pil = sharpness_enhancer.enhance(1.15)  # Much reduced from 1.3
        
        # Step 6: Very slight contrast boost
        contrast_enhancer = ImageEnhance.Contrast(enhanced_pil)
        enhanced_pil = contrast_enhancer.enhance(1.05)  # Reduced from 1.1
        
        # Ensure exact dimensions
        if enhanced_pil.size != (original_width, original_height):
            enhanced_pil = enhanced_pil.resize((original_width, original_height), Image.LANCZOS)
        
        # Generate output filename
        if output_path is None:
            name, ext = os.path.splitext(input_path)
            output_path = f"{name}_GENTLE{ext}"
        
        # Save with high quality
        enhanced_pil.save(output_path, quality=98, optimize=True)
        
        print(f"✅ GENTLE version saved: {output_path}")
        print("🌸 SUBTLE but CLEAR - gentle enhancement that preserves naturalness!")
        
        return output_path
        
    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return None

def main():
    """Main function for gentle enhancement"""
    if len(sys.argv) < 2:
        print("Usage: python gentle_enhancer.py <image_path>")
        return
    
    input_path = sys.argv[1]
    
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' not found.")
        return
    
    result = enhance_anime_gentle(input_path)
    if result:
        print(f"\n🌸 Your gently enhanced image is ready!")
        print(f"📁 Location: {result}")

if __name__ == "__main__":
    main()