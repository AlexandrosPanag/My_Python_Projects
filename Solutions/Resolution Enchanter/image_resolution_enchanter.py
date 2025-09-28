#!/usr/bin/env python3
"""
Image Resolution Doubler - Doubles image resolution 1:1 without altering appearance
Uses nearest-neighbor interpolation to maintain pixel-perfect scaling
"""

from PIL import Image
import os
import sys

def double_image_resolution(input_path, output_path=None):
    """
    Double the resolution of an image using nearest-neighbor interpolation
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path for the output image (optional)
    
    Returns:
        str: Path to the output image
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            print(f"Original size: {img.size} ({img.width}x{img.height})")
            
            # Calculate new dimensions (double the resolution)
            new_width = img.width * 2
            new_height = img.height * 2
            
            # Resize using nearest-neighbor interpolation for pixel-perfect scaling
            doubled_img = img.resize((new_width, new_height), Image.NEAREST)
            
            print(f"New size: {doubled_img.size} ({new_width}x{new_height})")
            
            # Generate output filename if not provided
            if output_path is None:
                name, ext = os.path.splitext(input_path)
                output_path = f"{name}_2x{ext}"
            
            # Save the doubled image
            doubled_img.save(output_path)
            print(f"Saved doubled image to: {output_path}")
            
            return output_path
            
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def batch_double_images(folder_path, output_folder=None):
    """
    Double the resolution of all images in a folder
    
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
                output_filename = f"{name}_2x{ext}"
                output_path = os.path.join(output_folder, output_filename)
            else:
                output_path = None
            
            result = double_image_resolution(input_path, output_path)
            if result:
                processed_count += 1
    
    print(f"\nProcessed {processed_count} images successfully!")

def main():
    """Main function with command-line interface"""
    print("🎨 Image Resolution Doubler v1.0")
    print("=" * 40)
    
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
        print("1. Double a single image")
        print("2. Double all images in a folder")
        
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