import socket
import threading
import sys
import time
import random

#Constants
SIZE = 1024
FORMAT = "utf-8"

# Connection input
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

# Botnames
botnames = {"Gina", "Holly", "Carl", "Ralph"}

# Verbs/actions
goodWords = ["play", "sing", "laugh", "talk", "eat", "paint", "walk", "build", "draw", "study",
             "read", "learn", "sleep", "work", "code"]
badWords = ["kill", "murder", "punch", "kick", "fight", "mock", "steal", "destroy", "scream",
            "break", "hurt", "abuse", "harm", "insult", "yell"]
allWords = goodWords + badWords

noSuggestion = [None]*(int(goodWords.__len__()/2))


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

def startChat(client):
    activity = random.choice(goodWords)
    activity2 = random.choice(goodWords + noSuggestion)

    if activity2 == None:
        message = f"The President: We should {activity}"

    else:
        message = f"The President: We should {activity} or {activity2}"

    for client in clients:
        client.send(message.encode(FORMAT))

    for client in clients:
        message2 = client.recv(SIZE).decode(FORMAT)
        broadcast(message2, client)
        time.sleep(1)


# Sends message to all clients
def broadcast(message, sender = None):
    if type(message) == str:
        message = message.encode()

    for client in clients:
        if client != sender:
            client.send(message)
    time.sleep(1)

def checkUsername(client):
    client.send("Bot".encode(FORMAT))
    username = client.recv(SIZE).decode(FORMAT)

    if username not in usernames:
        clients.append(client)
        usernames.append(username)
        print(f"{username} have connected to the server")
        client.send(f" ======== Welcome to the chatroom ======== \n"
                    f"Hi! You are connected to server at {ip}:{port} \n"
                    f"Now we have {' and '.join(usernames)} here! \n"
                    f"The chat will start when the room is full or in ... time".encode(FORMAT))
        broadcast(f"{username} has connected to the server! We need {4 - (len(usernames))} more to start the chat".encode(FORMAT), client)
        time.sleep(0.2)
    else:
        #usernamesLowercase = [i.lower for i in usernames]
        client.send(f"Taken".encode(FORMAT))
        availableBots = set(botnames).difference(set(usernames))
        client.send(f"{' and '.join(availableBots)} is the bot(s) that are still available".encode(FORMAT))
        client.close()


# main function, runs the show. Adds clients to the server
def connect():
    print("Server is listening..")

    while clients.__len__() < 4:
        try:
            #working
            client, adress = s.accept()
            checkUsername(client)


        except KeyboardInterrupt:
            #Not working
            client.send(str(f"something has happened. You were kicked out").encode(FORMAT))
            quit()


    if clients.__len__() == 4:
        # dont know what this does
        thread = threading.Thread(target=startChat, args=(client,))
        thread.start()
        print(str(thread))
        thread.join()

        # Not working properly, need fixing, maybe a sendtoall function
        broadcast(f"The President: Well, I'm the boss here and I say we sing")
        time.sleep(15)
        quit()

    # telle klienter
    # Skrive hvem som er koblet til

connect()


# Need to make 5 bots
# The bots should have one of them to take input from client,
# then the rest should respond in a dialog.

# Rules:
# The server should accept any connection
# It should be a sort of "chat room"
# All responses from one client should be sent back to all other clients except the one who sent it
# There should be a list of connected clients
# I can decide when and how to disconnect clients
# one bot should take response from command line
# The bots are not the first to speak, but they will always respond
