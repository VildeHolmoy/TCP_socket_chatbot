import sys
import socket
from bots import activationBot

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
              f"For the ip address you can use 'localhost'. The port should be the same as used in the server file. \n"
              f"The bots to choose from are: Grumpy Gina, Happy Holly, Crazy Carl and Responsible Ralph. \n"
              f"Please only use the bots first names, as their sensitivity-meter is turned all the way up "
              f"and they will be hurt if called any adjectives. \n"
              f"Remember that bots have an unbelievable memory. Don't get on their bad side.\n"
              f"If the bot you choose are already taken the terminal will show you who is available. \n"
              f"Example to connect to server: client.py localhost 2022 Gina \n"
              f"Have fun!")
        sys.exit()
    port = int(sys.argv[2])

except(IndexError, ValueError):                                         # If ip and port not specified correctly
    print(f"Ip and port must be specified")
    sys.exit()

allBots = {"Gina", "Holly", "Carl", "Ralph"}

# Command line input on bots
try:                                                                    # Checks if given botname is one of the bots
    name = sys.argv[3]
    if name not in allBots:
        print(f"Sorry, that is not a botname in this program. \n"
              f"Please choose one of these bots: "
              f"Gina, Holly, Carl or Ralph.")
        sys.exit()

except KeyError:                                                        # If botname is not a bot
    print(f"Sorry, something went wrong! Please try again.")
    sys.exit()

# Connection setup
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Creates TCP socket
try:
    clientSocket.connect((ip, port))                                    # Connects to the server

except:                                                                 # If the IP address or port is not matching the server
    print(f"Sorry, your IP or port is not typed in right. "
          f"Please try again. \n"
          f"Remember the port number must be the same "
          f"as the server port number. For IP-address"
          f" you could use 'localhost'.")
    sys.exit()                                                          # Exit program after guidance

# Main program
def main():
    while True:
        try:
            message = clientSocket.recv(SIZE).decode(FORMAT)            # Is always receiving messages sent from server

            if message == "GetUsername":                                # Takes request from server to get botname/username
                clientSocket.send(name.encode(FORMAT))

            elif message == "Taken":                                    # If username is taken,
                print(f"This bot is already spoken for. "
                      f"Please choose another bot.")
                msg = clientSocket.recv(SIZE).decode(FORMAT)            # the client gets told which bots are available
                print(msg)
                clientSocket.shutdown(2)
                clientSocket.close()                                    # disconnects from the socket

            elif message.startswith(f"The President: We "):             # When the President starts dialogue
                words = message.split(' ')                              # Makes each word in message a string in list
                activity = words[4]                                     # Picks out the words that is activities from the Presidents message
                try:
                    activity2 = words[6]
                except:                                                 # If activity is None
                    activity2 = None
                print(message)

                clientMessage = activationBot(name, activity, activity2)    # The activities are sent to bots.py
                clientSocket.send(f"{name}: {clientMessage}".encode())      # Message is then sent to server.

            elif message == "Bye":                                      # Round 3 has completed
                print(f"Server disconnected, you have "
                      f"had enough botchat for now."
                      f"You can start again by "
                      f"restarting server and reconnecting")
                clientSocket.close()                                    # Closes connection
                sys.exit()                                              # Closes program

            elif message.startswith("You have been"):                   # Kickout message from server.
                print(message)
                clientSocket.close()                                    # Closes connection
                sys.exit()                                              # Closes program

            elif message != "":
                print(message)

        except:                                                         # If no messages is received
            clientSocket.close()                                        # Close connection
            sys.exit()                                                  # Close program


main()
