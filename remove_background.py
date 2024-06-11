import os
from typing import Tuple
from rembg import remove
from PIL import Image


class RemoveBackGround:

    def __init__(
        self,
        photo_file_full_path: str,
        output_file_full_path: str,
        output_format: str = "PNG",
        resize: Tuple[int, int] | None = None
    ) -> None:
        self.photo_file_full_path = photo_file_full_path
        self.output_file_full_path = output_file_full_path
        self.output_format = output_format
        self.resize = resize

    def remove_background(self) -> None:
        open_image = Image.open(self.photo_file_full_path)

        if self.resize is not None:
            open_image.thumbnail(self.resize)
            new_image = Image.new('RGB', self.resize, (255, 255, 255))

            x_offset = (self.resize[0] - open_image.width) // 2
            y_offset = (self.resize[1] - open_image.height) // 2

            new_image.paste(open_image, (x_offset, y_offset))
            open_image = new_image

        output_result = remove(open_image)
        output_result.save(self.output_file_full_path, format=f"{self.output_format}")

        base_name = os.path.basename(self.photo_file_full_path)
        print(f"Photo: '{base_name}' was completed")
