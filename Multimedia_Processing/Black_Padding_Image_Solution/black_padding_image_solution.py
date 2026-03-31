"""
# Written by Alexandros Panagiotakopoulos
# alexandrospanag.github.io
# DATE: 31-03-2026
# LICENSE: CC 4.0 BY-NC-SA


Reads an image at its native resolution and adds a black border/padding
around it — no resizing, no stretching, just padding.

Usage:
    python add_padding.py input.jpg output.jpg --padding 50
    python add_padding.py input.jpg output.jpg --top 20 --right 40 --bottom 20 --left 40
    python add_padding.py input.jpg output.jpg --percent 10
    python add_padding.py input.jpg output.jpg --percent-top 5 --percent-right 10 --percent-bottom 5 --percent-left 10
    python add_padding.py input.jpg output.jpg --padding 30 --color 255 0 0
"""

import argparse
from pathlib import Path
from PIL import Image


def add_padding(
    input_path: str,
    output_path: str,
    top: int = 0,
    right: int = 0,
    bottom: int = 0,
    left: int = 0,
    color: tuple = (0, 0, 0),
) -> None:
    """
    Add padding around an image without altering its original pixels.

    Args:
        input_path:  Path to the source image.
        output_path: Path where the padded image will be saved.
        top:         Pixels of padding on the top edge.
        right:       Pixels of padding on the right edge.
        bottom:      Pixels of padding on the bottom edge.
        left:        Pixels of padding on the left edge.
        color:       RGB tuple for the padding colour (default black).
    """
    img = Image.open(input_path) #.convert("RGBA")  # Preserve alpha if present
    orig_mode = img.mode 

    # Work in RGB(A) so the padding colour always applies correctly
    if orig_mode == "RGBA": # Preserve alpha channel if it exists, but pad with opaque colour
        pad_color = (*color, 255) # Ensure padding is fully opaque
    elif orig_mode == "P": # Convert paletted images to RGBA to avoid palette issues with padding colour
        img = img.convert("RGBA") # Convert to RGBA to handle padding colour correctly
        pad_color = (*color, 255) # Use opaque padding colour
    else: # For all other modes, convert to RGB and use the specified colour
        img = img.convert("RGB") # Convert to RGB to ensure padding colour applies correctly
        pad_color = color # Use specified colour for padding

    orig_w, orig_h = img.size # Get original dimensions before padding
    new_w = orig_w + left + right # Calculate new width after adding left and right padding
    new_h = orig_h + top  + bottom # Calculate new height after adding top and bottom padding

    canvas = Image.new(img.mode, (new_w, new_h), pad_color) # Create new image with the new dimensions and padding colour
    canvas.paste(img, (left, top)) # Paste the original image onto the canvas at the correct position (accounting for left and top padding)
    canvas.save(output_path) # Save the final padded image to the specified output path

    print(f"Original size : {orig_w} × {orig_h} px") # Print original image dimensions
    print(f"Padding (px)  : top={top}  right={right}  bottom={bottom}  left={left}") # Print the amount of padding added on each side
    print(f"New size      : {new_w} × {new_h} px") # Print new image dimensions after padding
    print(f"Saved to      : {output_path}") # Print the path where the padded image was saved


def percent_to_px(percent: float, reference_px: int) -> int: 
    """Convert a percentage value to pixels based on a reference dimension."""
    return max(0, round(percent / 100.0 * reference_px))


# ── CLI ─────────────────────────────────────────────────────────────────────

def main(): # The main function to parse command-line arguments and execute the padding operation
    parser = argparse.ArgumentParser(
        description="Add black (or custom colour) padding around any image — pixels OR percent.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Fixed pixels (same size regardless of resolution):
    python add_padding.py input.jpg out.jpg --padding 50
    python add_padding.py input.jpg out.jpg --top 20 --right 40 --bottom 20 --left 40

  Percentage (scales with the image — great for batch processing):
    python add_padding.py input.jpg out.jpg --percent 10
    python add_padding.py input.jpg out.jpg --percent-top 5 --percent-right 15

  Custom colour:
    python add_padding.py input.jpg out.jpg --padding 30 --color 255 255 255
        """
    )

    parser.add_argument("input",  help="Input image path") # The path to the input image file that we want to add padding to
    parser.add_argument("output", help="Output image path") # The path where the output image with padding will be saved
 
    # ── Pixel options ──────────────────────────────────────────────────────
    px_group = parser.add_argument_group("Pixel padding (fixed px)") # A group of command-line arguments related to fixed pixel padding
    px_group.add_argument("--padding", type=int, default=None, 
                          help="Uniform padding in pixels on all four sides") # A command-line argument that allows the user to specify a uniform padding in pixels for all sides of the image
    px_group.add_argument("--top",    type=int, default=None) # A command-line argument that allows the user to specify the amount of padding in pixels for the top edge of the image
    px_group.add_argument("--right",  type=int, default=None) # A command-line argument that allows the user to specify the amount of padding in pixels for the right edge of the image
    px_group.add_argument("--bottom", type=int, default=None) # A command-line argument that allows the user to specify the amount of padding in pixels for the bottom edge of the image
    px_group.add_argument("--left",   type=int, default=None) # A command-line argument that allows the user to specify the amount of padding in pixels for the left edge of the image

    # ── Percent options ────────────────────────────────────────────────────
    pct_group = parser.add_argument_group(
        "Percent padding (scales with image size)",
        "Horizontal sides use image WIDTH; vertical sides use image HEIGHT."
    )
    pct_group.add_argument("--percent", type=float, default=None,
                           help="Uniform padding as %% of image dimension on all sides") # A command-line argument that allows the user to specify a uniform padding as a percentage of the image dimension for all sides of the image. The percentage is applied to the width for horizontal sides and to the height for vertical sides.
    pct_group.add_argument("--percent-top",    type=float, default=None) # A command-line argument that allows the user to specify the amount of padding as a percentage of the image height for the top edge of the image
    pct_group.add_argument("--percent-right",  type=float, default=None) # A command-line argument that allows the user to specify the amount of padding as a percentage of the image width for the right edge of the image
    pct_group.add_argument("--percent-bottom", type=float, default=None) # A command-line argument that allows the user to specify the amount of padding as a percentage of the image height for the bottom edge of the image
    pct_group.add_argument("--percent-left",   type=float, default=None) # A command-line argument that allows the user to specify the amount of padding as a percentage of the image width for the left edge of the image
 
    # ── Colour ─────────────────────────────────────────────────────────────
    parser.add_argument("--color", type=int, nargs=3, default=[0, 0, 0],
                        metavar=("R", "G", "B"),
                        help="Padding colour as R G B (default: 0 0 0 = black)")

    args = parser.parse_args()

    if not Path(args.input).exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    # Peek at image size so we can convert percentages
    with Image.open(args.input) as _img:
        img_w, img_h = _img.size

    # ── Resolve final pixel values (percent wins if both are given) ────────
    def resolve(side: str, px_val, pct_val, ref_px: int) -> int:
        if pct_val is not None:
            return percent_to_px(pct_val, ref_px)
        if px_val is not None:
            return px_val
        return 0   # default: no padding

    if args.percent is not None:
        # --percent sets all four sides at once (overrides per-side percent flags)
        top    = percent_to_px(args.percent, img_h)
        right  = percent_to_px(args.percent, img_w)
        bottom = percent_to_px(args.percent, img_h)
        left   = percent_to_px(args.percent, img_w)
    elif args.padding is not None:
        # --padding sets all four sides in pixels
        top = right = bottom = left = args.padding
    else:
        # Mix and match per-side pixel / percent flags
        top    = resolve("top",    args.top,    args.percent_top,    img_h) # Resolve the final pixel values for each side of the padding based on the command-line arguments provided by the user. If a percentage value is given, it takes precedence over the fixed pixel value. If neither is provided, it defaults to 0 (no padding).
        right  = resolve("right",  args.right,  args.percent_right,  img_w) # Resolve the final pixel values for each side of the padding based on the command-line arguments provided by the user. If a percentage value is given, it takes precedence over the fixed pixel value. If neither is provided, it defaults to 0 (no padding).
        bottom = resolve("bottom", args.bottom, args.percent_bottom, img_h) # Resolve the final pixel values for each side of the padding based on the command-line arguments provided by the user. If a percentage value is given, it takes precedence over the fixed pixel value. If neither is provided, it defaults to 0 (no padding).
        left   = resolve("left",   args.left,   args.percent_left,   img_w) # Resolve the final pixel values for each side of the padding based on the command-line arguments provided by the user. If a percentage value is given, it takes precedence over the fixed pixel value. If neither is provided, it defaults to 0 (no padding).

    add_padding(
        input_path=args.input, # The path to the input image file
        output_path=args.output, # The path where the output image with padding will be saved
        top=top, right=right, bottom=bottom, left=left, # The amount of padding to add on each side of the image, in pixels. These values are calculated based on the command-line arguments provided by the user, which can be specified as either fixed pixel values or as percentages of the image dimensions.
        color=tuple(args.color), # The colour to use for the padding, specified as an RGB tuple. This value is taken from the command-line arguments provided by the user, with a default of (0, 0, 0) for black if no colour is specified.
    )


if __name__ == "__main__":
    main()
