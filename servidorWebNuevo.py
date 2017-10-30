# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:45:00 2017

@author: Eros
"""

import socket

s=socket.socket()       #Create a socket object
host=socket.getfqdn()   #Get local machine name
port=6788
s.bind((host,port))     #Bind to the port
#sock=socket.create_connection((host,port))
print('Starting server on',host,port)
print('The Web server URL for this would be http://%s:%d/'%(host,port))
s.listen(5)             #Now wait for client connection.
print('Entering infinite loop; hit CTRL-C to exit')
while True:
    #Establish connection with client.
    c,(client_host,client_port)=s.accept()
    print('Got connection from',client_host,client_port)
    #c.send('Server Online\n')#This is invalid HTTP header
    c.recv(1000)# should receive request from client. (GET ....)
    c.send(b'HTTP/1.0 200 OK\n')
    c.send(b'Content-Type: text/html\n')
    c.send(b'\n')#header and body should be separated by additional newline
    fileHTML=open("index.html","rb")#read file in byte
    for line in fileHTML.readlines():
        c.send(line)
    c.close()