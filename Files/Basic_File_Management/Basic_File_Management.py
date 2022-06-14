import os
from tkinter import W #import the python os library
mountains = []

with open(r'C:\Users\<Username>\Desktop\greek_mountains.txt', encoding='utf-8') as f: #open the file , change the file path
    for mountain in f:
        mountain = mountain.split('\t')
        name = mountain[0]
        height = mountain[1]
        mountains.append((name,height))

for i in mountains:
    print(i)
max_height = 0
for m in mountains:
    if int(m[1])>max_height:max_height = int(m[1])
print("The tallest mountain has a height of:",max_height)

with open('mountains2.txt', 'w', encoding='utf-8') as f: #the path is saved to #c/users/<username>/
    for m in mountains:
        to_file = 'The mountain {} has a height of {} metres'.format(m[0],m[1])
        m_height = int(m[1])
        if m_height == max_height:
            to_file += "is the tallest greek montain! . \n"
        else:
            diff = max_height - m_height
            to_file += "The {} m. is the smallest mountain.".format(diff)
        f.write(to_file)