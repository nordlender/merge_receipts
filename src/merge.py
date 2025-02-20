import pypdf as pp
import os


def getFiles(dir: str | os.PathLike, filetypelist: list = ["pdf"]) -> list:
    """Gets a list of filenames with suffix from dir
    dir: Directory where files are stored
    filetypelist: List of filetypes to use, i.e. ['pdf'] or ['png', 'jpg']"""

    try:
        # List all files in the given directory
        files = [
            file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))
        ]
        # Remove all files without .pdf extension
        for file in files:
            if file.split(".")[-1] not in filetypelist:
                files.remove(file)
        return files
    except FileNotFoundError:
        print(f"The directory '{dir}' was not found.")
        return []
    except PermissionError:
        print(f"Permission denied for accessing the directory '{dir}'.")
        return []


def mergeFiles(
    dir: str | os.PathLike,
    files: list,
    output_name: str = "merged_files.pdf",
    max: int = 100,
) -> bool:
    """Merges pdf files
    dir: directory where files are stored
    files: list of files
    output_name: file name with suffix, saved in dir"""
    # Check if valid dir is given
    if not os.path.isdir(dir):
        return False
    dir = os.path.abspath(dir)

    if files == []:
        return False
    else:
        nFiles = len(files)
        if nFiles > max:
            print(f"Number of files given larger than max, {nFiles} > {max}")
            return False

        merger = pp.PdfWriter()

        for file in files:
            with open(os.path.join(dir, file), "rb") as pdf:
                print(file)
                merger.append(fileobj=pdf)

        newfile = os.path.join(dir, output_name)
        with open(newfile, "wb") as newpdf:
            merger.write(newpdf)

        merger.close()
        return True
