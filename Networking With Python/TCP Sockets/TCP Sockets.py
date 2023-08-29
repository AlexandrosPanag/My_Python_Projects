#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

import socket #import the socket library

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create a socket and begin to stream data
mysock.connect( ('data.pr4e.org',80)) #connect host, port