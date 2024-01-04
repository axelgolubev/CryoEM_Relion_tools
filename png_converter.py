# The script is created for a fast convertation of mrc files to png.
# The script should be located inside a job before 'Tiff' folder with required mrc files.
# Load relion module before use.
# To start job on Maxwell one can use: sbatch --partition=cssb --constraint=INTEL --wrap 'python3 png_converter.py'

import glob
import os
import subprocess

os.mkdir('pngs')
os.chdir('Tiff')

old_pix = 0.832 # pixel size of micrographs
new_pix = 10.0258 # new pixel size for binning > png files becomes lighter, but smaller and pixelated
contrast = 2 # '0' is no contrast adjustment

# glob create a list of all file names from the folder. Then we loop through the names, remove extensions and apply relion rescaling and convertation
for file in glob.glob("*.mrc"):
    name = file[:-4]
    command = f'relion_image_handler --i {name}.mrc --o ../pngs/{name}.png --sigma_contrast {contrast} --angpix {old_pix} --rescale_angpix {new_pix}'
    subprocess.run(command, shell=True)