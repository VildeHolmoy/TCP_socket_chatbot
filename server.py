import socket
import threading
import sys
import time
import random
from bots import goodWords, noSuggestion

#Constants
SIZE = 1024
FORMAT = "utf-8"

# Connection input
ip = "0.0.0.0"
port = int(sys.argv[1])
adress = (ip, port)


# Creates TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(adress)
s.listen()

# List of connected clients and usernames
clients = []
usernames = []

# Botnames
botnames = {"Gina", "Holly", "Carl", "Ralph"}




# Handles clients
#def handleClient(client):

 #  while True:
  #     try:
   #        message = client.recv(SIZE).decode(FORMAT)

    #       if message == "exit":
     #          for i in clients:
      #             i.close()
       #        broadcast(f"{username} has left the server", client)
        #   else:
         #      broadcast(message, client)
      # except:
       #    broadcast(f"{username} has left the server", client)

def startChat(client, i):
    if i == 0:
        print("======== Welcome to the chatroom o mighty human ========")
        broadcast("======== Welcome to the chatroom to all you piles of metal ========")

    if i == 1 or i == 2:
        newRound = "======== New Round ========="
        broadcast(newRound)
        print(newRound)

    if i < 3:
        activity = random.choice(goodWords)
        activity2 = random.choice(goodWords + noSuggestion)

        if activity2 == None:
            message = f"The President: We should {activity}"

        else:
            message = f"The President: We should {activity} or {activity2}"

        print(message)
        time.sleep(2)

        for client in clients:
            client.send(message.encode(FORMAT))

        for client in clients:
            time.sleep(2)
            message2 = client.recv(SIZE).decode(FORMAT)
            client.send(message2.encode(FORMAT))
            print(message2)
            broadcast(message2, client)


        lastAnswer = "The President: You never agree on anything. We will start a new round in 5 seconds."
        broadcast(lastAnswer)
        print(lastAnswer)
        time.sleep(5)

        startChat(client, i+1)
    elif i >= 3:
        broadcast(f"Bye")
        print(f"Chatroom closed. Start new chat the same way you did before if you want more of "
              f"those silly suggestions")
    quit()
    sys.exit()



# Sends message to all clients
def broadcast(message, sender = None):
    if type(message) == str:
        message = message.encode()

    for client in clients:
        if client != sender:
            client.send(message)
    time.sleep(1)

def checkUsername(client):
    client.send("GetUsername".encode(FORMAT))
    username = client.recv(SIZE).decode(FORMAT)

    if username not in usernames:
        clients.append(client)
        usernames.append(username)
        print(f"{username} have connected to the server")
        client.send(f" ======== Welcome to the chatroom ======== \n"
                    f"Hi! You are connected to server at port {port} \n"
                    f"Now we have {' and '.join(usernames)} here! \n"
                    f"The chat will start when the room is full. We need {4 - (len(usernames))} more to start the chat".encode(FORMAT))
        broadcast(f"{username} has connected to the server! We need {4 - (len(usernames))} more to start the chat".encode(FORMAT), client)
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
            # Kan ha threading her for å lage egen thread til hver klient
            #thread = threading.Thread(target=startChat, args=(client, 0))
            #print(str(thread))

        except KeyboardInterrupt:
            #Not working
            client.send(str(f"something has happened. You were kicked out").encode(FORMAT))
            quit()


    if clients.__len__() == 4:
        print(f"Chatroom is now full, and chat will start in 5 seconds")
        broadcast(f"Chatroom is now full! chat will start in 5 seconds")
        #Starts new thread for chatroom
        time.sleep(5)
        thread = threading.Thread(target=startChat, args=(client, 0))
        thread.start()


        while True:
            try:
                #threadInput = threading.Thread()
                #threadInput.start()
                messageFromServer = input()

                if messageFromServer != "":
                    broadcast(f"Host: {messageFromServer}")

            except:
                quit()



    quit()

connect()


# Rules:
# The server should accept any connection
# It should be a sort of "chat room"
# All responses from one client should be sent back to all other clients except the one who sent it
# There should be a list of connected clients
# I can decide when and how to disconnect clients
# one bot should take response from command line
# The bots are not the first to speak, but they will always respond
