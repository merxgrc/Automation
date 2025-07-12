import os
import shutil

for filename in os.listdir("."):
    if filename.endswith((".jpg", ".png")):
        os.makedirs("images", exist_ok=True)
        shutil.move(filename, f"images/{filename}")
