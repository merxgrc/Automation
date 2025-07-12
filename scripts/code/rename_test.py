import os

for filename in os.listdir("."):
    if os.path.isfile(filename) and filename.endswith(".txt"):
        new_name = filename.lower()
        if filename != new_name:
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")
