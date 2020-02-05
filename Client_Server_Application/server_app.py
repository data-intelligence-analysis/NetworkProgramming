# Network programming I
# Server Application

import socket
import sys
import argparse
import os

##Create a TCP/IP socket
    #servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## get local machine name
    #host = socket.gethostname()

### Alternative method
    ## specify localhost and port number
        # server_addr = ('localhost', 1000)
        # print >>sys.stderr, 'starting up on %s port %s' % server_addr

##Give port number (testing)
    #port = 9900

host = 'localhost'

data_size = 1024
client_request = 2



def echo_server_app(port):

    #Create a TCP Socket
    servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Enable reuse address/port
    servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #Bind the socket to the port
    server_addr = (host, port)
    print ("Starting up server on %s port %s" %server_addr)
    servsock.bind(server_addr)

    #Listen to clients, client_request sepcifies the max no. of queued connections
    servsock.listen(client_request)
    
    while True:
        print("Waiting to receive message from client")
        connect_client, client_address = servsock.accept()
        # number of bytes to receive
        data = connect_client.recv(data_size)
        
        if data:
            print("Data: %s" %data)
            connect_client.send(data)
            print ("Send %s bytes back to %s" % (data, client_address))
        else:
            print ("no more data from", client_address)
            break
        
        #dummy file to run throughput
        filename='throughput.txt'
        osx = os.path.getsize(filename)
        file = open(filename,'rb')
        read1 = file.read(osx)

        while(read1):
            connect_client.send(read1)
            read = file.read(osx)
        file.close()

        print ('Done sending')
        connect_client.send('Thank you for connecting') 
        ##print('Thank you for connecting')
        
        # end connection
        connect_client.close()

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port',action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server_app(port)
        
