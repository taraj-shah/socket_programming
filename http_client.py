# Taraj Shah shahts

from socket import *
import sys

# Server name: Can be IP or name (e.g. "128.138.32.126" or "yourserver.eng.uci.edu")
serverName = sys.argv[1]

# Specify port
serverPort = int(sys.argv[2])

# Create socket for communication
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiate the TCP connection (3-way handshake completes after this line is done)
clientSocket.connect((serverName, serverPort))

message = 'GET /' + sys.argv[3] + ' HTTP/1.1'
clientSocket.send(message.encode())

# Wait for a response from the server (max 1024 bytes)
response = clientSocket.recv(1024)

# Print the response and close the socket
print(response.decode())
clientSocket.close()
