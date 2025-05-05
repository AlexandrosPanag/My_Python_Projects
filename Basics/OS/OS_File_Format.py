import os
import os.path

# example user input C:\Users\<yourownusername>\Desktop

while True:
    dir = input('Input the path file:')
    if dir == '': break
    if os.path.isdir(dir):
        file_types = {}
        file_size = {}
        for r,d,f in os.walk(dir):
            for fi in f:
                if fi[0] not in '.~':
                    f_parts = fi.split('.')
                    if len(f_parts)>1:
                        f_type = f_parts[-1]
                        file_types[f_type]=file_types.get(f_type,0)+1
    for t in file_types:
        print(t,'\t\t',file_types[t])