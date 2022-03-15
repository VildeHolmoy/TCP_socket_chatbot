import sys
import socket

import client
from bots import activationBot
import threading
import time

# Constants
SIZE = 1024
FORMAT = "utf-8"

# Make user specify ip and port. Also gives help if needed.
try:
    ip = sys.argv[1]
    if ip == "--help":
        print(f" ======== Help has arrived ======== \n"
              f"To start a client and connect to the chatroom please write: \n"
              f"client.py <ip> <port> <botname> \n"
              f"The ip and port should be the same as used in the server file. \n"
              f"The bots to choose from are: Grumpy Gina, Happy Holly, Crazy Carl and Responsible Ralph. \n"
              f"Please only use the bots names, as they are very emotional and will lash out if called any superlatives. \n"
              f"If the bot you choose are already taken the terminal will show you who is available. \n"
              f"Example to start chatroom: client.py localhost 2022 Gina \n"
              f"Have fun!")
        sys.exit()
    port = int(sys.argv[2])

except(IndexError, ValueError):
    print(f"Ip and port must be specified")
    sys.exit()

allBots = {"Gina", "Holly", "Carl", "Ralph"}

# not working
try:
    name = sys.argv[3]
    if name not in allBots:
        print(f"Please choose one of these bots: Gina, Holly, Carl, Ralph")

except(KeyError):
    print(f"Sorry, your bot is already taken, please choose another one")
    sys.exit()

# Kobler til socket på server, sender valgt botnavn
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((ip, port))


def main():
    while True:
        try:
            # Is always receiving messages sent from server
            message = clientSocket.recv(SIZE).decode(FORMAT)

            # Takes request from server to get botname/username
            if message == "GetUsername":
                clientSocket.send(name.encode(FORMAT))

            # If username is taken, the client disconnects from the socket
            elif message == "Taken":
                print(f"This bot is already spoken for. Please choose another bot.")
                msg = clientSocket.recv(SIZE).decode(FORMAT)
                print(msg)
                clientSocket.shutdown(2)
                clientSocket.close()

            # When the President starts dialouge, the clients should respond // needs fixing
            elif message.startswith(f"The President: We"):
                words = message.split(' ')
                activity = words[4]
                try:
                    activity2 = words[6]
                except:
                    activity2 = None
                print(message)
                clientMessage = activationBot(name, activity, activity2)
                clientSocket.send(f"{name}: {clientMessage}".encode())

            elif message == "Bye":
                print(f"Server disconnected, you have had enough botchat for now."
                      f"You can start again by restarting server and reconnecting")
                clientSocket.close()
                quit()

            elif message != "":
                print(message)

        except:
            clientSocket.close()
            quit()
            break



main()

