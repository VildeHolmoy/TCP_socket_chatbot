import socket
import threading
import time
import random
#from bots import goodWords, badWords, allWords


# Constants
IP = socket.gethostbyname(socket.gethostname())
PORT = 2022
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

# Creates TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()

# List of connected clients and usernames
clients = []
usernames = []

# Trenger:
# Username
# clientConnection fix
# threads ??

#class Client: ???
    # def __init__(this, username, ):

# Handles clients
def clientConnection(client):
   while True:
       try:
           message = client.recv(SIZE).decode(FORMAT)

           if message == "exit":
               for i in clients:
                   i.close()
               broadcast(f"{username} has left the server", client)

           else:
               broadcast(message, client)
       except:
           broadcast(f"{username} has left the server", client)



# Sends message to all clients
def broadcast(message, client):
    for i in clients:
        if i is not client:
            i.send(message)

# main function, runs the show. Adds clients to the server
def connect():
    print("Server is listening..")

    while True:
        client, ADDR = s.accept()
        client.send("Username?".encode(FORMAT))
        username = client.recv(SIZE).decode(FORMAT)
        clients.append(client)
        usernames.append(username)
        broadcast(f"{username} has connected to the server!".encode(FORMAT), client)
        client.send(f"You have been connected to the server! Welcome".encode(FORMAT))
        print(f"{username} have connected to the server")

        thread = threading.Thread()
        thread.start()

    # telle klienter
    # Skrive hvem som er koblet til



connect()




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