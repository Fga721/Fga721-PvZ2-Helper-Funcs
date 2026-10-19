import os
import sys
from PIL import Image

# 1. Get the dropped file path or fallback to "file.png"
if len(sys.argv) > 1:
    original_path = sys.argv[1]
    # Set script_dir to the dropped file's folder so texture files look there
    script_dir = os.path.dirname(os.path.abspath(original_path))
else:
    # Fallback to local directory if run normally without drag-and-drop
    script_dir = os.path.dirname(os.path.abspath(__file__))
    original_path = os.path.join(script_dir, "file.png")

refs_dir = os.path.join(script_dir, "Refs")

left_ref_path = os.path.join(refs_dir, "texture_left.png")
mid_ref_path = os.path.join(refs_dir, "texture.png")
right_ref_path = os.path.join(refs_dir, "texture_right.png")

# 2. Verify that all required reference files exist
for path in [left_ref_path, mid_ref_path, right_ref_path, original_path]:
    if not os.path.exists(path):
        print(f"\n[ERROR] Required file not found: {path}")
        input("\nPress Enter to exit...")
        sys.exit(1)

# 3. Get widths and release the file handles immediately using .load()
with Image.open(left_ref_path) as img:
    img.load()
    w_left = img.width

with Image.open(mid_ref_path) as img:
    img.load()
    w_mid = img.width

with Image.open(right_ref_path) as img:
    img.load()
    w_right = img.width

# 4. Process the dropped image safely
try:
    with Image.open(original_path) as original:
        x0 = 0
        x1 = w_left
        x2 = x1 + w_mid
        x3 = x2 + w_right

        # If widths match, proceed with the crops
        crop_left = original.crop((x0, 0, x1, original.height))
        crop_mid = original.crop((x1, 0, x2, original.height))
        crop_right = original.crop((x2, 0, x3, original.height))
        
        # Force loading the cropped pixel data into memory
        crop_left.load()
        crop_mid.load()
        crop_right.load()

    # 5. Safely overwrite the files
    crop_left.save(left_ref_path)
    crop_mid.save(mid_ref_path)
    crop_right.save(right_ref_path)

    print("Images successfully updated in:", script_dir)
    print(" - texture_left.png")
    print(" - texture.png")
    print(" - texture_right.png")

except ValueError as e:
    print(f"\n[ERROR] Crop operation skipped: {e}")

# Keep the console open so you can read the success message or the error
print("\nExecution finished.")
input("Press Enter to close this window...")
