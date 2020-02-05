# Network programming I
# Dennis Osafo 

# Client Application

#!/usr/bin/env python3
import socket
import time
import sys



host = sys.argv[1]      # Host name or IP address
port = int(sys.argv[2]) # Port used by server
data_payload = 1000     # Message size (bytes) sent by TCP
m_type = 'RTT'          # Variable to represent RTT Measuring (RTT) or Throughput (TTPUT)
number_of_probes = '10' # Number of Probes to check 
server_delay = '0.5'    # Server delay for RTT Meauring and Throughput (tput) in seconds


""" The client application"""

#Create a TCP/IP socket
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect the socket to the server
serv_address = (host, port)
print("Connecting to %s port %s" % serv_address)
servsock.connect(serv_address)

#CSP message to send
csp_send_string = 's '+ m_type + ' ' + str(data_payload) + ' ' + number_of_probes + ' ' + server_delay + '\n'
message = csp_send_string.encode()
try:
    
    servsock.sendall(message)
    
    while True:
        data = servsock.recv(data_payload)
        message = data.decode()
        if message == '200 Ok: Ready':
            print('200 Ok: Ready')
            if  m_type == 'RTT':
                rtt_array = []
                probe_seq_number = 0
                for probe_seq_number in range(int(number_of_probes)):

                    #MP Message sending
                    MP_MESSAGE = 'm ' + 'Hello_World_welcome_to_lit ' + str(probe_seq_number) + '\n'
                    MP_MESSAGE = MP_MESSAGE.encode()
                    send_time = time.time() #time is measured in seconds
                    servsock.sendall(MP_MESSAGE)
                    check = servsock.recv(data_payload)
                    recv_time = time.time() #time is measured in seconds
                    rtt_in_s = round(recv_time - send_time, 10) #Round trip time is measured in seconds and rounded to the 10th decimal place
                    rtt_array.append(rtt_in_s)
                    message_measure = check.decode()
                    print(message_measure)
                    rtt_average = (sum(rtt_array)/len(rtt_array)) #measuring the mean or average RTT
                print(rtt_average)

                #Making CTP MESSAGE
                CTP_MESSAGE = 't \n'
                CTP_MESSAGE = CTP_MESSAGE.encode()
                servsock.sendall(CTP_MESSAGE)
                close_time = servsock.recv(data_payload)
                close_time = close_time.decode()
                print (close_time)
                break

            elif m_type == 'TTPUT':
                TTPUT_array = []
                probe_seq_number=0
                for probe_seq_number in range(int(number_of_probes)):
                    #MP Message sending
                    MP_MESSAGE = 'm ' + 'HelloWorldwelcometolit' + str(probe_seq_number) + '\n'
                    MP_MESSAGE = MP_MESSAGE.encode()
                    send_time = time.time() #time is measured in seconds
                    servsock.sendall(MP_MESSAGE)
                    check = servsock.recv(data_payload)
                    recv_time = time.time() #time is measured in seconds
                    ttput_in_s = round(recv_time_s - send_time_s, 10) #Raw time measured for througput
                    throughput_s = round(((data_payload*0.001)/(ttput_in_s)), 5)#Throughput is measured in seconds and rounded to the 10th decimal place
                    TTPUT_array.append(throughput_s)
                    message_measure = check.decode()
                    print(message_measure)
                    TTPUT_average = (sum(TTPUT_array)/len(TTPUT_array)) #measuring average or mean of the throughput
                print(TTPUT_average)

                #Making CTP Message
                CTP_MESSAGE = 't \n'
                CTP_MESSAGE = CTP_MESSAGE.encode()
                servsock.sendall(CTP_MESSAGE)  #sending CTP message 
                close_time = servsock.recv(data_payload)
                close_time = close_time.decode()
                print(close_time)
                break
        else:
            print(data)
            break
    

finally:
    print("Closing connection to the server")
    servsock.close()


