# CISC475 - Project 4
# This code sets up a server that listens on 
# a port and handles a connection being made
# from the postgres client
import socket
import pdb

def serverListen():
    print("This is the server")

    #sets up the ip address and port to operate on
    #local host is 127.0.0.1
    TCP_IP = '127.0.0.1'
    TCP_PORT = 10000
    BUFFER_SIZE = 1024

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
        
        ##################################################
        # This is where we attempted to compile and exec #
        # the pl/python function that was passed in.     #
        # Continue the work here by properly compiling   #
        # and executing the properly formatted function  #
        ##################################################
        #source = (data.decode('utf-8'))
        #source = """if a > b:\n  return true\nreturn false"""
        #code = compile(source, '<string>', 'exec')
        #exec(code)

        # This will reply back to the postgres client.
        # In the future this may reply with any
        # output from the executed pl/python code 
        conn.send(data)

    #close out the connection
    conn.close()
