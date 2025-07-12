import os

# loop through all items in curr dir
for filename in os.listdir("."):
    # if the item is a file and not a dir
    if os.path.isfile(filename):
        # check if file is jpg or png
        if filename.endswith((".jpg", ".png")):
            new_name = filename.lower()
            if filename != new_name:
                os.rename(filename, new_name)
                print(f"Renamed: {filename} -> {new_name}")
