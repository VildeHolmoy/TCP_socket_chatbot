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
            message = clientSocket.recv(SIZE).decode(FORMAT)

            if message == "Bot":
                clientSocket.send(name.encode(FORMAT))

            elif message == "Taken":
                print(f"This bot is already spoken for. Please choose another bot.")
                msg = clientSocket.recv(SIZE).decode(FORMAT)
                print(msg)
                clientSocket.shutdown(2)
                clientSocket.close()

            else:
                print(message)

        except:
            clientSocket.close()
            quit()
            break


main()