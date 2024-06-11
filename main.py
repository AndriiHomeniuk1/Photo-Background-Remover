from typing import Tuple
from cli_parser import get_parser
from image_folder import OpenFolderWithImages
from image_processing import ImageProcessing
from remove_background import RemoveBackGround


def process_single_image(
        file_path: str,
        output_file_path: str,
        output_format: str = "PNG",
        resize=None
) -> None:
    RemoveBackGround(
        photo_file_full_path=file_path,
        output_file_full_path=output_file_path,
        output_format=output_format,
        resize=resize
    ).remove_background()
    print(f"Processed single image: {file_path}")


def process_images_in_folder(
        path_folder: str,
        output_path_folder: str,
        file_format: Tuple[str, ...],
        output_format: str = "PNG",
        resize=None
) -> None:
    open_folder = OpenFolderWithImages(
        path_folder, file_format).get_list_from_inbox()
    ImageProcessing(
        files_paths_list_from_folder=open_folder,
        path_folder=path_folder,
        output_path_folder=output_path_folder,
        output_format=output_format,
        resize=resize
    ).image_folder_processing()


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.mode == "single":
        resize = tuple(map(int, args.resize.split(','))) if args.resize else None
        RemoveBackGround(
            photo_file_full_path=args.file_path,
            output_file_full_path=args.output_file_path,
            output_format=args.output_format,
            resize=resize
        ).remove_background()
        print(f"Processed single image: {args.file_path}")

    elif args.mode == "folder":
        file_format = tuple(args.file_format.split(','))
        resize = tuple(map(int, args.resize.split(','))) if args.resize else None

        open_folder = OpenFolderWithImages(args.path_folder, file_format).get_list_from_inbox()
        ImageProcessing(
            files_paths_list_from_folder=open_folder,
            path_folder=args.path_folder,
            output_path_folder=args.output_path_folder,
            output_format=args.output_format,
            resize=resize

        ).image_folder_processing()


if __name__ == "__main__":
    main()
