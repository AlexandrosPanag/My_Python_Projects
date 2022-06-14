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
                    # file format
                    f_parts = fi.split('.')
                    if len(f_parts)>1:
                        f_type = f_parts[-1]
                        file_types[f_type]=file_types.get(f_type,0)+1
                        #file size
                        full_f_name = os.path.join(r,fi)
                        size = os.path.getsize(full_f_name)
                        file_size[f_type] = file_size.get(f_type,0)+ size
    for t in file_types:
        print(t,'\t\t',file_types[t])
    print(50*'*')
    total_size = sum(file_size.values())
    print("Total size:",total_size)
    for t in file_size:
        percent = 100*file_size[t]/total_size #creating a percentage
        print('{}\t\t{}\t\t{:5.2f}%'.format(t, file_size[t], percent)) #printing the file size