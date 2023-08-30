#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

import urllib.request, urllib.parse, urllib.error #import the urllib library


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #open the url
for line in fhand: #make a dictionary , split it
    print(line.decode().strip()) #bounce through the words and print the dictionary out