# Script for changing optical groups in relion .star files

The script is adding correct optical groups for each particle in particles.star file if optical groups weren't specified for some reason. 
The correct optic groups are taken from micrographs_ctf.star file.

To start the script: 
1) copy this change_optic.py file to a folder when results will be stored.
2) add corresponding pathways for micrographs_ctf.star and particles.star file to the fields in the beggining of the script
3) Run in terminal: python change_optic.py

The processing takes around 1-2 minutes depending on the number of particles.

Possible problems to fix:
1) Script recreates the particles file with different spacing between columns - it could possibly cause problems reading the file with Relion.
