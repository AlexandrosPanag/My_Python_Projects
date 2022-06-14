import os
import os.path

# example user input C:\Users\<yourownusername>\Desktop

while True:
    dir=input('Input the path file:')
    if dir=='':break
    if os.path.isdir(dir):
        for r,d,f in os.walk(dir):
            print(r)
            for fi in f:
                print('\t\t',fi)
