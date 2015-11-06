# CISC475 - Project 4
# This code sets up a client that connects to 
# a server and passes on a message from within
# the postgres database

import socket

def clientStart(message):
    print("This is the client")

    TCP_IP = '127.0.0.1'
    TCP_PORT = 10000
    BUFFER_SIZE = 1024
    MESSAGE = bytes(message, 'UTF-8')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    return data

#OLD CODE
#print("This is the client")

#TCP_IP = '127.0.0.1'
#TCP_PORT = 10000
#BUFFER_SIZE = 1024
#MESSAGE = bytes("Hello World!", 'UTF-8')

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
#data = s.recv(BUFFER_SIZE)
#s.close()

#print("received data:"), data