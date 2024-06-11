import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Process images to remove background."
    )
    subparsers = parser.add_subparsers(
        dest="mode",
        help="Choose to process a single image or a folder",
        required=True
    )

    single_parser = subparsers.add_parser(
        "single",
        help="Process a single image"
    )
    single_parser.add_argument(
        "file_path",
        type=str,
        help="Full path of the image file"
    )
    single_parser.add_argument(
        "output_file_path",
        type=str,
        help="Output path for the processed image"
    )
    single_parser.add_argument(
        "--output_format",
        type=str,
        default="PNG",
        choices=["PNG", "GIF", "WebP", "TIFF"],
        help="Output format (default: PNG)"
    )
    single_parser.add_argument(
        "--resize",
        type=str,
        help="Resize dimensions (e.g., 500,500)"
    )

    folder_parser = subparsers.add_parser(
        "folder",
        help="Process all images in a folder"
    )
    folder_parser.add_argument(
        "path_folder",
        type=str,
        help="Path of the folder with images"
    )
    folder_parser.add_argument(
        "output_path_folder",
        type=str,
        help="Output path folder"
    )
    folder_parser.add_argument(
        "--file_format",
        type=str,
        default=".jpg,.jpeg,.webp,.png",
        help="File formats to include (default: .jpg,.jpeg,.webp,.png)"
    )
    folder_parser.add_argument(
        "--output_format",
        type=str,
        default="PNG",
        choices=["PNG", "GIF", "WebP", "TIFF"],
        help="Output format (default: PNG)"
    )
    folder_parser.add_argument(
        "--resize",
        type=str,
        help="Resize dimensions (e.g., 500,500)"
    )

    return parser
