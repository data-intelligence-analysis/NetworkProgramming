# <b><u>Echo Application to measure TCP performance</u></b>

Implement a client and a server that communicate over a network using TCP. The server is essentially an echo server, which simply echoes the message it receives from the client

## Echo Client-Server Application

## Table of Contents
1. [Overview](#overview)

2. [Installation](#Installation)

3. [Usage](#usage)

4. [Support](#support)

5. [Roadmap](#roadmap)

6. [License](#license)

7. [Contributing](#contributing)



## Overview
Overview: Implement a client and a server that communicate over a network using TCP. The server is essentially an echo server, which simply echoes the message it receives from the client.  Here is what the server and client application must accomplish: 
1. The server should accept, as a command line argument, a port number that it will run at. After being started, the server should repeatedly accept an input message from a client and send back the same message
2. The client should accept, as command line arguments, a host name (or IP address), as well as a port number for the server. Using this information, it creates a connection (using TCP) with the server, which should be running already. The client program then sends a message (text string) to the server using the connection. When it receives back the message, it prints it and exits.
