# import socket module
from socket import *
import html
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket:
port = 5000
serverSocket.bind(('', port))
serverSocket.listen(1)

while True:
    # Establish the connection:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket:
        http_header = "HTTP/1.1 200 OK\n\n".encode("utf-8")
        connectionSocket.send(http_header)

        # Send the content of the requested file to the client:
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("utf-8"))
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:

        # Send response message for file not found:
        not_found = "HTTP/1.1 404 Not Found\n\n".encode("utf-8")
        connectionSocket.send(not_found)

        # Close client socket:
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
