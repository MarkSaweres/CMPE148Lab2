# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start

serverPort = 1234
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        # Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        # Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(bytes("\nHTTP/1.1 200 OK\n\n", "UTF-8"))
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(bytes("404 Not Found\r\n", "UTF-8"))
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data
