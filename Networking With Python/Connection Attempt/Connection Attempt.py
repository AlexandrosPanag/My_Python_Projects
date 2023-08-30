#By Alexandros Panagiotakopoulos - alexandrospanag.github.io

import socket #import the socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
mysock.connect(('data.pr4e.org', 80)) #connect to a website
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #encode the connection
mysock.send(cmd) #send commands

while True:  
    data = mysock.recv(512) #attempt to connect with 512 bytes
    if len(data) < 1: #if the connection attempt was not successful, disconnect (connection closed)
        break
    print(data.decode(),end='') #else print data
mysock.close() #close the socket connection