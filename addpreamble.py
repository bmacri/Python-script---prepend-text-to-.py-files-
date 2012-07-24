import os

def add_preamble(current_directory):
    for path, names, files in os.walk(current_directory):
        if names != 'vendor' or names != 'vendor-local':
            for afile in files:
                afile_path = os.path.join(path, afile)
                if afile_path.endswith('.py') and afile != 'addpreamble.py':
                    f = open(afile_path, 'r')
                    all_lines = f.readlines()		
				    first_line = all_lines[0]
				    if first_line == '#!/usr/bin/env python\n':
					    all_lines = f.readlines()
					    f.close()
					    f = open(afile_path, 'w')
					    f.write(first_line)
					    f.write(all_lines[1:])
					    f.write("preamble\n\n")
					    f.close()				
				    elif first_line != '#!/usr/bin/env python':
					    old_contents = f.read()
					    f = open(afile_path, 'w')
					    f.write("preamble\n\n")
					    f.write(old_contents)
					    f.close()




#--------------------------------------------------------------------------------
add_preamble('.') 

