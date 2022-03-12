import socket
import threading
import sys
import time
import random
#from bots import goodWords, badWords, allWords

#Constants
SIZE = 1024
FORMAT = "utf-8"

ip = sys.argv[1]
port = int(sys.argv[2])
adress = (ip, port)


# Creates TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(adress)
s.listen(4)

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
def handleClient(client):
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
def broadcast(message, sender = None):
    if type(message) == str:
        message = message.encode()

    for client in clients:
        if client != sender:
            client.send(message)
    time.sleep(0.1)

# main function, runs the show. Adds clients to the server
def connect():
    print("Server is listening..")

    while clients.__len__() < 4:
        try:
            #working
            client, adress = s.accept()
            username = client.recv(SIZE).decode(FORMAT)
            clients.append(client)

            # not working
            if username in usernames:
                s.close()

            #working
            usernames.append(username)
            print(usernames)
            print(f"{username} have connected to the server")
            client.send(f" ======== Welcome to the chatroom ======== \n"
                        f"Hi! You are connected to server at {ip}:{port} \n"
                        f"Now we have {' and '.join(usernames)} here! \n"
                        f"The chat will start when the room is full or in ... time".encode(FORMAT))

            # working
            broadcast(f"{username} has connected to the server! We need {4-(len(usernames))} more \n"
                      f"to start the chat".encode(FORMAT), client)



        except:
            #Not working
            client.send(str(f"something has happened. You were kicked out").encode(FORMAT))
            s.close()

    if clients.__len__() == 4:
        # dont know what this does
        thread = threading.Thread()
        thread.start()
        thread.join()

        # Start broadcast chat here

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
