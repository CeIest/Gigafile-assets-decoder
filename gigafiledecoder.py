import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory


# Prompts folder input
Tk().withdraw()
folder_path = askdirectory()
destination_folder = folder_path + "_decrypted"

print('\nDecoding folder "' + os.path.basename(folder_path) + '"...\n')


# Decodes all filenames
for root, dirs, files in os.walk(folder_path):
    dest_dir = os.path.join(destination_folder, os.path.relpath(root, folder_path))
    os.makedirs(dest_dir, exist_ok=True)

    for file_name in files:
        original_filepath = os.path.join(root, file_name)
        try:
            decoded_filename = file_name.encode("cp437", "ignore").decode("shiftjis")
        except UnicodeDecodeError:
            decoded_filename = file_name
            print(f"Could not rename {decoded_filename}")
        print("Decoding file  " + decoded_filename)
        decoded_filepath = os.path.join(dest_dir, decoded_filename)
        shutil.copy2(original_filepath, decoded_filepath)
print('\n')


# Decodes all the folder names inside the decoded root folder
def rename_subdirectories(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            oworiginal_filepath = os.path.join(root, dir_name)
            if dir_name.endswith("ò"): # This char as suffix is useless and breaks the decoding.
                dir_name = dir_name.rstrip('ò')
            if dir_name.endswith("É"): # This char as suffix is useless and breaks the decoding.
                dir_name = dir_name.rstrip('É')
            try:
                decoded_dirname = dir_name.encode("cp437", "ignore").decode("shiftjis")
            except UnicodeDecodeError:
                decoded_dirname = dir_name
                print(f"Could not rename {decoded_dirname}")
            print("Decoding folder  " + decoded_dirname)
            decoded_filepath = os.path.join(root, decoded_dirname)
            os.rename(oworiginal_filepath, decoded_filepath)
            try:
                rename_subdirectories(decoded_filepath)
            except FileExistsError:
                print(f"Could not rename {oworiginal_filepath} into {decoded_filepath}")
rename_subdirectories(destination_folder)


print('\nDecoding complete.')
