import os
from typing import Tuple, List
from remove_background import RemoveBackGround


class ImageProcessing:
    def __init__(
        self,
        files_paths_list_from_folder: List[str],
        path_folder: str,
        output_path_folder: str,
        output_format: str = "PNG",
        resize: Tuple[int, int] = None
    ) -> None:
        self.files_paths_list_from_folder = files_paths_list_from_folder
        self.path_folder = path_folder
        self.output_path_folder = output_path_folder
        self.output_format = output_format
        self.resize = resize

    def image_folder_processing(self) -> None:
        processed_counter = 0
        unprocessed_counter = 0
        unprocessed_files = []

        for file_name in self.files_paths_list_from_folder:
            input_path = os.path.join(self.path_folder, file_name)
            name, format_file = file_name.split(".")
            output_path = os.path.join(self.output_path_folder, f"{name}.{self.output_format}")
            try:
                RemoveBackGround(
                    photo_file_full_path=input_path,
                    output_file_full_path=output_path,
                    output_format=self.output_format,
                    resize=self.resize
                ).remove_background()

                processed_counter += 1

            except Exception as e:
                print(f"Error - {e}")
                unprocessed_counter += 1
                unprocessed_files.append(file_name)

        print(
            f"\nphoto_folder_processing completed: {processed_counter}\n"
            f"unprocessed: {unprocessed_counter}\n"
            f"unprocessed_files: {unprocessed_files}"
        )
