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
    try:
        rel_dir = os.path.relpath(dirpath, src_dir).rstrip('ò').rstrip('É')
        
        rel_dir_enc = rel_dir.encode(ENC_FORMAT, "ignore").decode("shiftjis")
    except UnicodeDecodeError:
        click.secho(f"Couldn't decrypt {rel_dir}. Copying as original", fg="red")
        rel_dir_enc = rel_dir

    final_dir = os.path.join(dest_dir, rel_dir_enc)
    os.makedirs(final_dir, exist_ok=True)
        

    for file in filenames:
        try:
            file_enc = file.rstrip('ò').rstrip('É').encode(ENC_FORMAT, "ignore").decode("shiftjis")
            print(f'Decoding  "{rel_dir_enc}/{file_enc}"')
        except UnicodeDecodeError:
            click.secho(f"Couldn't decrypt {file}. Copying as original", fg="red")
            file_enc = file

        shutil.copy2(os.path.join(dirpath, file), os.path.join(final_dir, file_enc))


