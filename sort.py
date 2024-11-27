import os
from pathlib import Path

def organize_files(directory):
    # Create a Path object for the directory
    dir_path = Path(directory)

    if not dir_path.is_dir():
        print(f"Error: {directory} is not a valid directory.")
        return

    for file in dir_path.iterdir():
        if file.is_file():
            # Get the file extension (without the dot)
            ext = file.suffix[1:].lower() or "no_extension"
            # Create a subdirectory for the extension
            subdir = dir_path / ext
            subdir.mkdir(exist_ok=True)
            # Move the file to the corresponding subdirectory
            file.rename(subdir / file.name)

    print("Files have been organized.")
  
directory_to_organize = input("path: ")
organize_files(directory_to_organize)
