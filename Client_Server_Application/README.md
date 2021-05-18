# <b><u>Echo Application to measure TCP performance</u></b>

Implement a client and a server that communicate over a network using TCP. The server is essentially an echo server, which simply echoes the message it receives from the client

<b>Documentation is saved as Network Programming.pdf</b>

## Echo Client-Server Application

## Table of Contents
1. [Overview](#overview)

2. [Installation](#Installation)

3. [Usage](#usage)

4. [Performing RTT and Throughput Measurements](#Performing RTT and Throughput Measurements)

5. [Roadmap](#roadmap)

6. [Contributing](#contributing)



## Overview
Overview: Implement a client and a server that communicate over a network using TCP. The server is essentially an echo server, which simply echoes the message it receives from the client.  Here is what the server and client application must accomplish: 
1. The server should accept, as a command line argument, a port number that it will run at. After being started, the server should repeatedly accept an input message from a client and send back the same message
2. The client should accept, as command line arguments, a host name (or IP address), as well as a port number for the server. Using this information, it creates a connection (using TCP) with the server, which should be running already. The client program then sends a message (text string) to the server using the connection. When it receives back the message, it prints it and exits.

## Installation

## Usage
Files used:


## Performing RTT and Throughput Measurements
Performing RTT and Throughput Measurements

Overview: We are extending the echo client-server application to measure the round trip time (RTT) and throughput of the path connecting the client to the server.  To measure RTT, you will use TCP to send and receive messages of size 1, 100, 200,400, 800 and 1000 bytes.  To measure throughput, you will use TCP to send and receive messages of size 1K, 2K, 4K, 8K, 16K and 32K bytes. For each measurement and for each message size, the client will send at least ten probe messages to the server, which will echo back the messages.

For the purpose of this work sample would only use 1,000 bytes to measure RTT and 2K to measure throughput. 

Protocol phases: The echo application will be extended, however, by specifying the exact protocol interactions between the client and the server.  This entails specifying the exact message formats,  as  well  as  the  different  communication  phases,  as outlined next.
1.	Connection Setup Phase (CSP): This is the first phase in the protocol where the client informs the server that it wants to conduct active network measurements in order to compute the RTT and throughput of its path to the server. 
  a.	CSP: Client - After setting up a TCP connection to the server, the client must send a single message to the server having the following format:
    <PROTOCOL  PHASE><WS><M−TYPE><WS><MSG SIZE><WS><PROBES><WS><SERVER  DELAY>\n
    •	PROTOCOL PHASE: The protocol phase during the initial setup will be denoted by the lower case character ‘s’. This allows the server to differentiate between the different protocol phases that the client can be operating at, as we will see.
    •	M-TYPE (Measurement Type): Allows the client to specify whether it wants to compute the RTT, denoted by “RTT”, or the throughput,     denoted by “TTPUT”.
    •	MSG SIZE (Message Size): Specifies the number of bytes in the probe’s payload
    •	PROBES: Allows the client to specify the number of measurement probes that the server should expect to receive.   Once all the probe messages have been echoed back and a sample measurement is taken for each one, the client should compute an estimate of the mean (average) RTT or mean throughput, depending on the type of measurement being performed.
    •	SERVER DELAY: Specifies the amount of time that the server should wait be-fore echoing the message back to the client.  The default value should be 0.  You will vary this value later to emulate paths with longer propagation delays.  Even though increasing the server delay merely increases the processing time at the server, it nevertheless causes the feedback delay, observed by the sender, to in-crease, which has an effect somewhat similar to increasing the path’s propagation delay.
    •	WS: A single white space to separate the different fields in the message.  The white space could serve as a delimiter for the server when parsing or tokenizing the received message.
    •	The last is a new line character that indicates the end of the message.
  b.	CSP: Server - The server should parse the connection setup message to log the values of all the variables therein since they will be needed for error checking purposes.  Upon the reception of a valid connection setup message, the server should respond with a text message containing the string  “200 OK:  Ready” informing the client that it can proceed to the next phase.  On the other hand, if the connection setup message is incomplete or invalid, the server should respond with a text message containing the string “404 ERROR: Invalid Connection Setup Message” and then terminate the connection.
  c.	CSP: Summary - During correct operation, after setting up a TCP connection to the server, the client sends a single connection setup message to the server.  The server parses and logs the information in the message and responds with a “200 OK: Ready ”text message informing the client to proceed to the next phase.

2. Measurement Phase (MP) - In this phase, the client starts sending probe messages to the server in order to make the appropriate measurements required for computing the mean RTT or the mean throughput of the path connecting it to the server. 
  a.	MP: Client -The client should send the specified number of probe messages to the server with an increasing sequence number starting from 1. More specifically, the message format is as follows:<PROTOCOL  PHASE><WS><PAYLOAD><WS><PROBE SEQUENCE NUMBER>\n
    •	PROTOCOL PHASE: The protocol phase when conducting the measurements will be denoted by the lower case character ‘m’.
    •	PAYLOAD:  This is the probe’s payload and can be any arbitrary text whose size was specified in the connection setup message using the MESSAGE SIZE (MESS_SIZE) variable.
    •	PROBE SEQUENCE NUMBER: The probe messages should have increasing sequence numbers starting from 1 up to the number of probes specified in the connection setup message using the NUMBER OF PROBES variable.
  b.	MP: Server- the server should echo back every probe message received.  It should also keep track of the probe sequence numbers to make sure they are indeed being incremented by 1 each time and do not exceed the number of probes specified in the connection setup phase.  If the probe message is incomplete or invalid (contains an incorrect sequence number for example) the server should not echo the message back. Instead, the server should respond with a text message containing the string  “404ERROR: Invalid Measurement Message” and then terminate the connection
  c.	MP: Summary- The client repeatedly sends measurement messages to the server in an attempt to compute the mean RTT and/or mean throughput.  A sample measurement is taken for each probe sent out.  The server repeatedly echoes messages back to the client unless it detects erroneous behavior in which case it sends an error message and terminates the connection.
3.	Connection Termination Phase (CTP). In this phase, the client and the server attempt to gracefully terminate the connection.  We will outline the expected behavior from both the client and the server next.
  a.	CTP: Client - The client should send a termination request to the server and then wait for a response (unless of course the server already terminated the connection due to an error in the Measurement Phase).  Once a response is received, the client should terminate the connection.  The message format is as follows: <PROTOCOL  PHASE>\n
    •	PROTOCOL PHASE: The protocol phase when terminating the connection will be denoted by the lower case character ‘t’
  b.	CTP: Server - If the message format is correct, the server should respond with a text message containing the string  “200 OK:  Closing Connection”.   Otherwise, the server should respond with a text message containing the string “404 ERROR: In-valid Connection Termination Message”.  Either way the server should terminate the connection.
  c.	CTP: Summary - During correct operation, the client sends a termination message, the server responds with “200 OK: Closing Connection” text message and then both terminate the connection.



