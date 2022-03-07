import socket
import threading

# Need to setup connection to client server
# Mangler threading



# Connection to clients
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ip, 2022))
serverSocket.listen(5)



# Need to make 5 bots
# The bots should have one of them to take input from client,
# then the rest should respond in a dialog.

# Rules:
# The server should accept any connection e.g there can be more than one user on client??
# It should be a sort of "chat room"
# All responses should be sent back to all clients (except the one who sent it? (from assignment))
# There should be a list of connected clients
# I can decide when and how to disconnect clients
# one bot should take response from command line
# The bots are not the first to speak, but they will always respond
#