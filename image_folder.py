import os
from typing import Tuple


class OpenFolderWithImages:

    def __init__(
        self,
        folder_path: str,
        file_format: Tuple[str, ...] | None = None
    ) -> None:
        self.folder_path = folder_path
        self.file_format = (
            ".jpg", ".jpeg", ".webp") if file_format is None else file_format

    def get_list_from_inbox(self) -> list:
        list_with_images_path = os.listdir(self.folder_path)
        result = []
        for file in list_with_images_path:
            if file.lower().endswith(self.file_format):
                result.append(file)
                continue

        return result
