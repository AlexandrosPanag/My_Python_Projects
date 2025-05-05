import os
import os.path

# example user input C:\Users\<yourownusername>\Desktop

while True:
    dir =input('Input the path file:')
    if dir == '': break
    if os.path.isdir(dir):
        count_files = 0
        for r,d,f in os.walk(dir):
            level = r.replace(dir, '').count(os.sep)
            print(level*'\t',r)
            for fi in f:
                if fi[0] not in '.~':
                    print((level+1)*'\t',fi)
                    count_files += 1
    print('A total number of {} files were found.'.format(count_files))   