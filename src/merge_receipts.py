from PIL import Image
from src import merge
import os
from time import sleep
import re


def get_images(dir: str, files: list) -> list:
    """Takes a list of filenames with suffix, and a directory they are stored in.
    Returns a list of PIL.ImageFile~ objects.
    dir: Directory where images are stored
    files: list of filenames, ex. ['image.jpg', 'image2.png']"""
    images = []
    for file in files:
        image = Image.open(os.path.join(dir, file))
        image.thumbnail((2200, 3500), Image.Resampling.LANCZOS)
        if image.mode == "RGBA":
            image = image.convert("RGB")
        images.append(image)

    return images


def merge_receipts(
    parent_dir: str | os.PathLike, img_dir: str | os.PathLike, regex_str: str
) -> None:
    """Merges receipts, places refund form first (name your refund form 'refusjonsskjema').
    parent_dir: directory where refund form is stored, and output destination
    img_dir: child directory where images are stored"""

    try:
        imgfiles = merge.getFiles(os.path.join(parent_dir, img_dir), ["jpg", "png"])

        images = get_images(os.path.join(parent_dir, img_dir), imgfiles)
        images[0].save(
            os.path.join(parent_dir, "images.pdf"),
            resolution=300,
            save_all=True,
            append_images=images[1:],
        )
    except OSError as e:
        print(f"File could not be saved. Error: {e}")
        raise

    try:
        sleep(1)  # Sleep a lil bit, let the images finish
        pdffiles = merge.getFiles(os.path.abspath(parent_dir))

        # Move refund form to start of list before merging
        regex = re.compile(regex_str)
        for i in range(len(pdffiles)):
            if regex.match(pdffiles[i]):
                pdffiles.insert(0, pdffiles[i])
                pdffiles.pop(i + 1)
                break

        success = merge.mergeFiles(parent_dir, pdffiles)
        if success:
            print(
                f"Files merged successfully. File saved at {parent_dir}/merged_files.pdf"
            )
        else:
            print("Merge failed.")

        os.remove(os.path.join(parent_dir, "images.pdf"))
    except FileNotFoundError as e:
        print(
            f"File {parent_dir}/images.pdf could not be found. This file \
            is created during the merging process. Error: {e}"
        )
        raise
