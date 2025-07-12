import os
import shutil

# Define a map for the extensions, "folder mapping"

extension_map = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "docs",
    ".txt": "docs",
    ".py": "code"
}

for filename in os.listdir("."):
    if os.path.isfile(filename):
        # get file extension
        _, ext = os.path.splitext(filename)
        # check if we have folder for this ext
        if ext in extension_map:
            folder = extension_map[ext]
            os.makedirs(folder, exist_ok=True)
            shutil.move(filename, f"{folder}/{filename}")
            print(f"moved {filename} -> {folder}/")