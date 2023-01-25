import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory


Tk().withdraw()
folder_path = askdirectory()
destination_folder = folder_path + "_decrypted"

print('\ndecrypting folder "' + os.path.basename(folder_path) + '"...\n')

for root, dirs, files in os.walk(folder_path):
    dest_dir = os.path.join(destination_folder, os.path.relpath(root, folder_path))
    os.makedirs(dest_dir, exist_ok=True)

    for file_name in files:
        original_filepath = os.path.join(root, file_name)
        decoded_filename = file_name.encode("cp850", "ignore").decode("shiftjis")
        print("decrypting file  " + decoded_filename)
        decoded_filepath = os.path.join(dest_dir, decoded_filename)
        shutil.copy2(original_filepath, decoded_filepath)
print('\n')

def rename_subdirectories(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name.endswith("ò"): # REMOVING THAT ONE ANNOYING CARACTER THAT BREAKS THE DECODING
                dir_name = dir_name.rstrip('ò')
            original_filepath = os.path.join(root, dir_name)
            decoded_dirname = dir_name.encode("cp850", "ignore").decode("shiftjis")
            print("decrypting folder  " + decoded_dirname)
            decoded_filepath = os.path.join(root, decoded_dirname)
            os.rename(original_filepath, decoded_filepath)
            rename_subdirectories(decoded_filepath)
rename_subdirectories(destination_folder)
