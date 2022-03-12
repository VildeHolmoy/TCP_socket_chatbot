import socket
import sys

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

allBots = {"Grumpy Gina", "Happy Holly", "Crazy Carl", "Responsible Ralph"}


#try:


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
name = sys.argv[3]
print(f" ======== Welcome to the chatroom ======== \n"
      f"Hi {name}! You are connected to server at {ip}:{port} \n"
      f"... are already here! \n"
      f"The chat will start when the room is full or in ... time")

