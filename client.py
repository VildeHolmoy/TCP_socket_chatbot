import socket


# Need to make connection to server

# Instansiates a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects client to server, corresponds with ip and port in server.py
clientSocket.connect((2022))




# Need a loop as long as the client is connected do this ...

# Need input parameter, with possible exit code

