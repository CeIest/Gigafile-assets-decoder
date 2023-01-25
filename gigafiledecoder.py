import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw()
folder_path = askdirectory()

for root, _, files in os.walk(folder_path):
    for file_name in files:
        original_filepath = os.path.join(root, file_name)
        decoded_filename = file_name.encode("cp850", "ignore").decode("shiftjis")
        print("decrypting " + decoded_filename)
        decoded_filepath = os.path.join(root, decoded_filename)
        os.rename(original_filepath, decoded_filepath)
        
# To-do:
# • Decode the folder names
# • Copy the decoded folder while keeping the original folder intact
