# Photo-Background-Remover

This Python script is designed to process images and efficiently remove their backgrounds. It offers two main modes of operation: processing a single image and processing a folder of images.

## Features:

- **Single Image Processing**: Remove the background from a single image file.
- **Folder Processing**: Process all images within a specified folder, removing their backgrounds.
- **Flexible Output Options**: Choose the output format for processed images (PNG, GIF, WebP, TIFF).
- **Optional Resizing**: Resize images before background removal for better performance and control.

## Usage:

1. **Single Image Mode**: 
    ```bash
    python main.py single <file_path> <output_file_path> [--output_format OUTPUT_FORMAT] [--resize RESIZE]
    ```
   - `file_path`: Full path to the input image file.
   - `output_file_path`: Output path for the processed image.
   - `--output_format OUTPUT_FORMAT` (optional): Output format for the processed image (default: PNG). Options: PNG, GIF, WebP, TIFF.
   - `--resize RESIZE` (optional): Resize dimensions for the input image (e.g., 500,500).

2. **Folder Mode**:
    ```bash
    python main.py folder <path_folder> <output_path_folder> [--file_format FILE_FORMAT] [--output_format OUTPUT_FORMAT] [--resize RESIZE]
    ```
   - `path_folder`: Path to the folder containing input images.
   - `output_path_folder`: Output folder path for processed images.
   - `--file_format FILE_FORMAT` (optional): File formats to include (default: .jpg, .jpeg, .webp, .png).
   - `--output_format OUTPUT_FORMAT` (optional): Output format for processed images (default: PNG). Options: PNG, GIF, WebP, TIFF.
   - `--resize RESIZE` (optional): Resize dimensions for input images (e.g., 500,500).

## Dependencies:

- `rembg`: Library for efficient background removal.
- `Pillow`: Python Imaging Library for image processing.

## Installation:

1. Clone the repository:
    ```bash
    git clone https://github.com/AndriiHomeniuk1/Photo-Background-Remover.git
    cd Photo_Background_Remover
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Examples:

### Single Image Mode

  ```bash
  python main.py single "C:\Users\38097\Desktop\image_for_project\Daniel_Craig_2021.png" "C:\Users\38097\Desktop\image_for_project\for_test\new_image.png" --output_format PNG --resize 500,500
  ```
 ### Folder Mode

  ```bash
  python main.py folder "C:\Users\38097\Desktop\image_for_project" "C:\Users\38097\Desktop\image_for_project\for_test" --file_format .jpg,.png --output_format PNG --resize 500,500
  ```
Author:
Andrii Homeniuk
Contact: andreygomenuk@gmail.com



