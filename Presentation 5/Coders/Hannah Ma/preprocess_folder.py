import os
import shutil
import re

# Mount drive
from google.colab import drive
drive.mount('/content/drive')
# You need to have a shortcut to Krish's Patches folder in your drive

# Define filtering function
def filter(input_folder, output_base_folder):
    # Make sure input folder exists
    if not os.path.isdir(input_folder):
        print(f"Error: {input_folder} is not a valid directory.")
        return

    # Create the output base folder if it doesn't exist
    os.makedirs(output_base_folder, exist_ok=True)

    # Iterate over each item in the input folder
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if "patched_" in item_path or item_path[-3:] == 'tif' or os.path.isdir(item_path):
            pass
        else:
            size = os.stat(item_path).st_size
            if size > 2000 and bool(re.search("patch\d{1,3}", item_path)):
                shutil.copy(item_path, output_base_folder)
                print(f"Copied '{item}' to '{output_base_folder}'")

# call function - modify folder paths if needed !!!
if __name__ == "__main__":
    input_folder = '/content/drive/MyDrive/Patches' 
    output_base_folder = "/content/drive/MyDrive/filtered_patches"

    filter(input_folder, output_base_folder)
