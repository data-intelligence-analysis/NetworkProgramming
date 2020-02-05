## Network programming I
# Client Application

import socket
import sys
import argparse
import time
import os 

host = 'localhost'
data_payload = 1024
m_type = 'rtt'


def echo_client_app(port):

    #Create a TCP/IP socket
    servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect the socket to the server
    serv_address = (host, port)
    print("Connecting to %s port %s" % serv_address)
    servsock.connect(serv_address)

    # Send data
    
    try:
        send_time_s = time.time()

        #Send data
        t1=time.time()
        message = "Hello world!"
        print("Sending: %s"%message)
        servsock.sendall(message)
        ##data = servsock.recv(data_payload)
        with open('received_file', 'wb') as file:
            print('file opened')
            t2 =time.time()
            ##while True:
                ##data = servsock.recv(data_payload)
                ##if not data:
                    ##break
                ##file.write(data)
                ##t3 = time.time()
        
        #Look for the response
            data = servsock.recv(data_payload)
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data1 = servsock.recv(24)
                amount_received += len(data1)
                print("Received: %s" % data1)

            file.write(data)
            t3 = time.time()

        recv_time_s = time.time()
        rtt_in_s = round(recv_time_s - send_time_s, 5)
        
        print ('Received:', repr(data))
        print ('RTT Time: ', rtt_in_s, 's')
        print ('Raw timers:', t1, t2, t3)
        print ('Total: ', t3-t1)
        print ('Throughput: ', round(((data_payload*0.001)/(t3-t1)),3)),
        #(data_payload*0.001)/(t3-t1),3))
        print('Kb/sec') 
        file.close()
        print('Successfully received the file')
        
    ##except socket.errno e:
        ##print("Socket error: %s" % str(e))
    ##except Exception, e:
        ##print("Other exception: %s" %str(e))
    finally:
        print("Closing connection to the server")
        servsock.close()

   

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest ="port", type=int, required=True)
    give_args = parser.parse_args()
    port = give_args.port
    echo_client_app(port)
 
