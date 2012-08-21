import os #this library provides an interface between Python and an operating system 

def add_preamble(directory):
    for path, names, files in os.walk(directory): #os.walk(directory) returns the path, names of subdirectories and names of files of a directory, creating a directory treee
        if names != 'vendor' or names != 'vendor-local': #files in the vendor and vendor-local directories should not have a preamble
            for afile in files: 
                afile_path = os.path.join(path, afile) #concatenates the path returned in os.walk and the filename, resulting in an absolute path
                if afile_path.endswith('.py') and afile != 'addpreamble.py': #add the preamble to all .py files except this one
                    f = open(afile_path, 'r')
                    all_lines = f.readlines()
                    f.close()
                    if all_lines != []:		
                        first_line = all_lines[0]
                        if first_line == '#!/usr/bin/env python\n' or first_line == 'coding: utf-8': #these lines need to remain at the top
                            f = open(afile_path, 'w')
                            f.write(first_line)
                            f.write(str(all_lines[1:]))
                            f.write("preamble\n\n")
                            f.close()				
                        elif first_line != '#!/usr/bin/env python': #elif is used instead of else here in order not to "catch" too much
                            old_contents = f.read()
                            f = open(afile_path, 'w')
                            f.write("preamble\n\n")
                            f.write(old_contents)
                            f.close()




#--------------------------------------------------------------------------------
add_preamble('.') #calls add_preamble on the directory from which python addpreamble.py is run

