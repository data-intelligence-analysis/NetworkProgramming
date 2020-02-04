# Network programming I
# Dennis Osafo

# Server Application

#!/usr/bin/env python3
import socket
import time
import sys 



host = sys.argv[1] # Server's hostname/IP address
MESS_SIZE = 1024 
port = int(sys.argv[2]) # Port to listen too. Ports 9000 to 10000 are open on linux machine
number_for_probe = 1
client_request = 2


""" The server application"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servsock:  # Create a TCP/IP socket
    servsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Enable reuse address/port
    #Bind the socket to the port
    server_addr = (host, port)
    print ("Starting up server on %s port %s" %server_addr)
    servsock.bind(server_addr)
    #Listen to clients, client request specifies the max no. of queued connections
    servsock.listen()
    print("Waiting to receive message from client")
    connect, client_address = servsock.accept()

    with connect:
        print('Connected by', client_address)
        while True:
            data = connect.recv(MESS_SIZE)
            message = data.decode()
            message = message.split()
            protocol_phase = message[0]
            if protocol_phase == 's':
                if len(message) >=5:
                    m_type = message[1]
                    MESS_SIZE = int(message[2])
                    probe_limit = int(message[3])
                    server_delay = float(message[4])
                    connect.sendall(b'200 Ok: Ready')
                    print('200 OK: Ready')
                else:
                    connect.sendall (b'404 ERROR: Invalid Connection Setup Message')
                    print('404 ERROR: Invalid Connection Setup Message')
                    break
                
            elif protocol_phase == 'm':
                data_measurement = message[1]
                number_probe = int(message[2])
                if number_probe > probe_limit:
                    time.sleep(server_delay)
                    connect.sendall(b'404 ERROR: Invalid Measurement Message')
                    print('404 ERROR: Invalid Measurement Message')
                    break
                else:
                    print(data.decode())
                    time.sleep(server_delay)
                    connect.sendall(data)
            elif protocol_phase == 't':
                time.sleep(server_delay)
                connect.sendall(b'200 OK: Closing Connection')
                print('200 OK: Closing Connection')
                break

            else:
                connect.sendall(b'404 ERROR: Invalid Connection Setup Message')
                print('404 ERROR: Invalid Connection Setup Message')
                break
    # end connection
    connect.close()   


        
