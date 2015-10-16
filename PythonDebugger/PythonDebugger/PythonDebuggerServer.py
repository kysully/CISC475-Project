# CISC475 - Project 4
# Kyle Sullivan
# This code sets up a server that listens on 
# a port and handles a connection being made
# from the postgres client
#!/usr/bin/env python

import socket

print("This is the server")

#sets up the ip address and port to operate on
#local host is 127.0.0.1
TCP_IP = '127.0.0.1'
TCP_PORT = 10000
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

#creates the socket we will connect on and binds it to the localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#accepts the connection when the client does its part
conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    #recieves the data sent by the client
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #print out the data sent after converting back to a string
    print ("received data:", data.decode('utf-8'))
    conn.send(data)  # echo the data we recieved
#close out the connection
conn.close()