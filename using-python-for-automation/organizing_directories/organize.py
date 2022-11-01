import os
from pathlib import Path

# Run This File will older all files into folders on this dir

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'  # If filetype doesn't exist in our dictionary


def organize_directory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pick_directory(filetype)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            directory_path.mkdir()
        filePath.rename(directory_path.joinpath(filePath))


organize_directory()
