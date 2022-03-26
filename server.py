import socket
import threading
import sys
import time
import random
from bots import goodWords, noSuggestion
import os


# Constants
SIZE = 1024
FORMAT = "utf-8"

# Connection input to determine IP and port for socket
ip = "0.0.0.0"
try:
    port = sys.argv[1]
    if port == "--describeHolly":
        print(f"Holly is called Happy Holly by us humans. Her model is GalacticExplorer2021. \n"
              f"She is newly produced and her system therefore runs problem free. \n"
              f"She is always up for some fun. We have never seen her say no.")
        os._exit(0)
    elif port == "--describeGina":
        print(f"Gina is called Grumpy Gina, and for good reason. She was built in 1987 and her system failures is "
              f"causing her battery levels to run low almost all the time. \n"
              f"She hates using more energy than absolutely needed. Don't expect much from her.")
        os._exit(0)
    elif port == "--describeCarl":
        print(f"Carl was built as an experiment, and his nickname Crazy Carl comes from his builder. \n"
              f"He is programmed to always engage in high-risk behavior, and is very easily bored. \n"
              f"Carl was built to see how long it took before he self destructed. \n"
              f"He is now 2 years old, and is considered a bot miracle.")
        os._exit(0)
    elif port == "--describeRalph":
        print(f"Ralph is the responsible of the bunch. He always goes for the safest option. \n"
              f"The rumor is his danger-meter has never went beyond a level 2. That is on a scale from"
              f"one to ten! \n"
              f"And he is turning 20 this year. You can look at him as a 90 year old human with a aching back.")
        os._exit(0)
except:
    print(f"Something was wrong with the port number. Please use another port. 2022 should work.")
    os._exit(0)
address = (ip, port)


# Creates TCP socket on given port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(address)
s.listen()

# List of connected clients and usernames
clients = []
usernames = []


botnames = {"Gina", "Holly", "Carl", "Ralph"}                                           # Botnames for all the bots


# Function that runs on threadChat. Will start when four clients is connected to socket
# Runs three times, works recursively. Will close program after completion.
def startChat(client, i):
    try:
        while True:
            if i == 0:                                                                  # the first time the function runs.
                print("======== Welcome to the chatroom O mighty human ========")       # Welcomes both the human behind the server and all the bots to the chatroom
                broadcast("======== Welcome to the chatroom to all you piles of metal ========")


            if i == 1 or i == 2:
                newRound = "\n======== New Round ========="                             # Shows everybody that a new round has started
                broadcast(newRound)
                print(newRound)

            if i < 3:                                                                   # As long as the number of rounds (number of loops of this function) is under three
                activity = random.choice(goodWords)                                     # Activities are chosen randomly for list in bots.py
                activity2 = random.choice(goodWords + noSuggestion)                     # Activity2 also has the possibility of being None
                while activity == activity2:                                            # Forces the two activities to be different
                    activity2 = random.choice(goodWords + noSuggestion)

                if activity2 is None:                                                   # If there is no suggested activity2
                    message = f"The President: We should {activity}"
                    print(message)
                    time.sleep(2)

                else:                                                                   # If there is a suggested activity2
                    message = f"The President: We should {activity} or {activity2}"
                    print(message)
                    time.sleep(2)

                for client in clients:                                                  # Send message from the President to all clients
                    client.send(message.encode(FORMAT))

                for client in clients:
                    time.sleep(2)                                                       # Sleep between messages is added for more realistic chat
                    message2 = client.recv(SIZE).decode(FORMAT)                         # Recieves answer from all clients
                    print(message2)
                    broadcast(message2)                                                 # Sends the recieved message back to all clients but the sender

                question = f"The President: What du you think human? " \
                           f"If you dont have any thoughts just press enter."           # The president steps in at the end of the round to hear what the human have to say
                broadcast(question)
                print(question)

                messageFromClient = input("")                                           # Listens for input from the human (the person behind the server)
                time.sleep(2)

                if messageFromClient != "":                                             # If the human enters something in input the President responds
                    broadcast(messageFromClient)
                    messageP2 = f"The President: The human have spoken! " \
                                f"We will take your input into consideration. \n" \
                                f"A new round will start in 5 seconds."
                    print(messageP2)
                    broadcast(messageP2)

                    time.sleep(5)                                                       # The thread sleeps for 5 seconds before startChat() is recursively called and starts a new round
                    startChat(client, i + 1)

                else:                                                                   # If the human does not respond (only presses enter), the President decides the activity
                    messageP1 = f"The President: Well I guess it's up to me then! " \
                                f"I say we {activity}. \n" \
                                f"Next round starts in 5 seconds."
                    print(messageP1)
                    broadcast(messageP1)

                    time.sleep(5)                                                       # The thread sleeps for 5 seconds before startChat() is recursively called and starts a new round
                    startChat(client, i + 1)

            if i >= 3:                                                                  # If the chat has gone three rounds, the chatroom closes
                broadcast(f"Bye")
                print(f"Chatroom closed. I think you need a break "
                      f"from those bots! \n"
                      f"Start new chat the same way you did before, "
                      f"if you want more of "
                      f"those silly suggestions.")

            os._exit(0)

    except Exception:                                                                   # If a client.py is terminated during the chat the program stops and the bots are kicked out
        print(f"A bot has left us. Ugh, now we have to start all over! "
              f"Just gently terminate the other clients and "
              f"start new ones. Im sure the bots"
              f" won't notice.")
        kickBots(client)
        os._exit(0)                                                                     # Terminates the program


# Sends message to all clients except sender
def broadcast(message, sender=None):
    if type(message) == str:
        message = message.encode()

    for client in clients:
        if client != sender:
            client.send(message)

    time.sleep(1)


# Kicks out all the bots and closes the program
# Also clears the list of clients and usernames
def kickBots(client):
    try:
        broadcast(f"You have been kicked out. Please forgive the human. "
                    f"Remember it has limited brainpower.".encode(FORMAT))
        clients.clear()
        usernames.clear()
        s.close()
        os._exit(0)
    except:
        clients.clear()
        usernames.clear()
        s.close()
        os._exit(0)


# Checks the accepted clients
def checkUsername(client):
    client.send("GetUsername".encode(FORMAT))
    username = client.recv(SIZE).decode(FORMAT)

    if username not in usernames:                                                       # If the username is not taken, welcome the bot to the chatroom
        clients.append(client)                                                          # Adds the client to the clients list
        usernames.append(username)                                                      # Adds the usernames to the usernames list
        print(f"{username} have connected to the server")
        client.send(f" ======== Welcome to the chatroom ======== \n"
                    f"Hi! You are connected to server at port {port} \n"
                    f"Now we have {' and '.join(usernames)} here! \n"
                    f"The chat will start when the room is full. "
                    f"We need {4 - (len(usernames))} more to "
                    f"start the chat".encode(FORMAT))
        broadcast(f"{username} has connected to the server! "
                  f"We need {4 - (len(usernames))} more to "
                  f"start the chat".encode(FORMAT), client)

    elif clients.__len__() < 4:                                                         # If the username is taken but the chatroom is not full
        client.send(f"Taken".encode(FORMAT))
        availableBots = set(botnames).difference(set(usernames))                        # Checks which bot names are not in use yet
        client.send(f"{' and '.join(availableBots)} is the bot(s) "                     # send list of available bots to the client
                    f"that are still available".encode(FORMAT))
        client.close()

    else:                                                                               # If the chatroom is full
        client.send(f"Chatroom is full. {username}, "
                    f"why are you trying to open two clients?"
                    f" I promise you will get your say "
                    f"in the chat you are already in.".encode(FORMAT))
        client.close()


# Listening for new connections. Target for threadListen.
# Runs while the chatroom is full
def listen(client, address):
    while True:
        client, address = s.accept()
        checkUsername(client)


# While the program runs
while True:
    print("Server is listening..")

    while clients.__len__() < 4:                                                        # As long as number of clients is under 4 accept connection and check username
        try:
            # working
            client, address = s.accept()
            checkUsername(client)

        except:
            client.send(f"Something went wrong! ".encode(FORMAT))
            quit()

    while clients.__len__() == 4:                                                       # While the client number is four the chatroom will run.
        # Informs connected clients that the room is full and the chat will start
        print(f"Chatroom is now full. Chat will start in 5 seconds.")
        broadcast(f"Chatroom is now full! Chat will start in 5 seconds.")
        time.sleep(5)

        threadListen = threading.Thread(target=listen, args=(client, address))          # The listening thread will run to catch new connections
        threadListen.start()

        threadChat = threading.Thread(target=startChat, args=(client, 0))
        threadChat.start()                                                              # Starts new thread for chatroom

        threadChat.join()                                                               # Both threads run until it is terminated
        threadListen.join()                                                             # Both threads run until it is terminated
    quit()
    os._exit(0)
