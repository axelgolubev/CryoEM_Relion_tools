'''
Created: 3 Jan 2023, A.Golubev
CSSB, Landau Group
------------------------------
The script is adding correct optical groups for each particle in particles.star file. 
The correct optic groups are taken from micrographs_ctf.star file.

To start the script: 
1) copy this .py file to a folder when results will be stored.
2) add corresponding pathways for micrographs_ctf.star and particles.star file to the field below in the beggining of the script
3) Run script in terminal: python change_optic.py

Possible problems to fix:
1) Script recreates the particles file with different spacing between columns - it could possibly cause problems reading the file with Relion.
   To solve it we have to understand how to add correct spacing between columns or use other tools to transform .star files (for example with pyem).
'''

# Pathways to files:
starting_file_micrographs = "micrographs_ctf.star"
starting_file_particles = "particles.star"

# Part one - trace file with micrographs and extract info about micrographs names and corresponding optic groups
with open(starting_file_micrographs, "r") as micrographs:
    print('---------------------------------------------')
    print('Reading data about optical groups from micrographs...')
    rows = micrographs.readlines()
    normal_mapping = {}
    for row in rows:
        if row.find('CtfFind') != -1:
            clean_line = row.split()
            name_optic = clean_line[0:2]
            micrograph_pathway = name_optic[0]
            micrograph_name = micrograph_pathway[micrograph_pathway.rfind('/') + 1 :]
            optic_group = name_optic[1]
            normal_mapping[micrograph_name] = optic_group
    print('Reading is finished! Optical groups are saved.')
    print('---------------------------------------------')

# Part two - trace the file with particles, change optic groups corresponding to the table with normal optic groups (step 1) and create a final file 
with open(starting_file_particles, "r") as particles, open("particles_with_normal_mapping.star", "w") as result:
    print('Setting optical groups for each particle. The process could take some time...') 
    lines = particles.readlines()
    for line in lines:
        if line.find('MotionCorr') == -1:
            result.write(line)
        else:
            clean_line = line.split()
            mic_path = clean_line[8]
            mic_name = mic_path[mic_path.rfind('/') + 1 :]
            for micrograph_name in normal_mapping:         
                if mic_name == micrograph_name:
                    clean_line[9] = normal_mapping[micrograph_name]
                    edited_line = "    ".join(clean_line)
                    result.write(' ' + edited_line + '\n')
                else:
                    pass

print('Changing of optical groups is complete!')
print('---------------------------------------------')
