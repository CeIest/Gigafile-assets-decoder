import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory
import click


ENC_FORMAT = "cp437"




Tk().withdraw()
src_dir = askdirectory()

dest_dir = f"{src_dir}_decrypted"



click.secho(f'\nDecoding folder "{os.path.basename(src_dir)}"...\n', fg='green')





 
for dirpath, _, filenames in os.walk(src_dir):

    rel_dir = os.path.relpath(dirpath, src_dir)
    rel_dir_enc = rel_dir.encode(ENC_FORMAT, "ignore").decode("shiftjis")


    final_dir = os.path.join(dest_dir, rel_dir_enc)
    os.makedirs(final_dir, exist_ok=True)
        

    for file in filenames:
        file_enc = file.encode(ENC_FORMAT, "ignore").decode("shiftjis")
        print(f'Decoding  "{rel_dir_enc}/{file_enc}"')

        shutil.copy2(os.path.join(dirpath, file), os.path.join(final_dir, file_enc))


