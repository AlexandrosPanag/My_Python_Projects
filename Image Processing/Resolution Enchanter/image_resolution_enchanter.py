#Copyright (c) 2025 Alexandros Panagiotakopoulos
#All Rights Reserved
#DATE: 01/10/2025
#alexandrospanag.github.io
#!/usr/bin/env python3
# For Windows: python image_resolution_enchanter.py
"""
Image Resolution Enhancer - Creates high-quality 2x resolution images
Advanced scaling technique that produces visually superior results
Perfect for enhancing pixel art, game assets, and graphics
"""

from PIL import Image
import os
import sys

def double_image_resolution(input_path, output_path=None):
    """
    Create a high-resolution version by scaling up with nearest-neighbor, then scaling back down with better sampling
    This creates a visually improved version while maintaining the original display dimensions
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path for the output image (optional)
    
    Returns:
        str: Path to the output image
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            original_size = img.size
            print(f"Original size: {original_size} ({img.width}x{img.height})")
            
            # Step 1: Scale up 4x using nearest-neighbor to preserve pixel art style
            temp_width = img.width * 4
            temp_height = img.height * 4
            upscaled = img.resize((temp_width, temp_height), Image.NEAREST)
            
            # Step 2: Apply a slight blur to smooth edges (optional - can be removed for pure pixel art)
            # from PIL import ImageFilter
            # upscaled = upscaled.filter(ImageFilter.GaussianBlur(radius=0.5))
            
            # Step 3: Scale back down to 2x the original size using high-quality resampling
            final_width = img.width * 2
            final_height = img.height * 2
            enhanced = upscaled.resize((final_width, final_height), Image.LANCZOS)
            
            print(f"Enhanced size: {enhanced.size} ({final_width}x{final_height})")
            print(f"Resolution doubled with improved quality!")
            
            # Generate output filename if not provided
            if output_path is None:
                name, ext = os.path.splitext(input_path)
                output_path = f"{name}_enhanced_2x{ext}"
            
            # Save the enhanced image
            enhanced.save(output_path, dpi=(144, 144))  # Also set higher DPI
            print(f"Saved enhanced image to: {output_path}")
            
            return output_path
            
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def batch_double_images(folder_path, output_folder=None):
    """
    Double the DPI/resolution of all images in a folder while keeping same dimensions
    
    Args:
        folder_path (str): Path to folder containing images
        output_folder (str): Path to output folder (optional)
    """
    # Supported image formats
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    processed_count = 0
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(folder_path, filename)
            
            if output_folder:
                name, ext = os.path.splitext(filename)
                output_filename = f"{name}_enhanced_2x{ext}"
                output_path = os.path.join(output_folder, output_filename)
            else:
                output_path = None
            
            result = double_image_resolution(input_path, output_path)
            if result:
                processed_count += 1
    
    print(f"\nProcessed {processed_count} images successfully!")
    print("All images now have enhanced resolution with visible quality improvements!")

def main():
    """Main function with command-line interface"""
    print("🎨 Image Resolution Enhancer v1.0")
    print("=" * 40)
    print("Creates visually improved 2x resolution images with enhanced quality")
    print()
    
    if len(sys.argv) > 1:
        # Command line usage
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        
        if os.path.isfile(input_path):
            double_image_resolution(input_path, output_path)
        elif os.path.isdir(input_path):
            batch_double_images(input_path, output_path)
        else:
            print(f"Error: '{input_path}' is not a valid file or directory.")
    else:
        # Interactive mode
        print("Choose an option:")
        print("1. Enhance resolution of a single image (2x size with better quality)")
        print("2. Enhance resolution of all images in a folder")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            input_path = input("Enter path to image file: ").strip().strip('"')
            output_path = input("Enter output path (press Enter for auto): ").strip().strip('"')
            output_path = output_path if output_path else None
            
            double_image_resolution(input_path, output_path)
            
        elif choice == "2":
            folder_path = input("Enter path to folder: ").strip().strip('"')
            output_folder = input("Enter output folder (press Enter for same folder): ").strip().strip('"')
            output_folder = output_folder if output_folder else None
            
            batch_double_images(folder_path, output_folder)
            
        else:
            print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()

