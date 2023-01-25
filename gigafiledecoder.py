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

print('\nDecryption complete.')
