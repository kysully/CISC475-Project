/*
* Cisc 475 - Project 4
* This code creates a postgres user defined function 
* for the language Pl/Python
* The function serves as a client to connect to 
* a python server listening
*/
CREATE OR REPLACE FUNCTION debuggerConnect(func text)
returns text AS
$$
import socket

print("This is the client")

TCP_IP = '127.0.0.1'
TCP_PORT = 10000
BUFFER_SIZE = 1024
MESSAGE = bytes(func, 'UTF-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

return data.decode('utf-8')
$$
  Language 'plpython3u' VOLATILE;