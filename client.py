import socket
import sys


IP = socket.gethostbyname(socket.gethostname())
PORT = 2022
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():

    print(f"Hi! To connect to chatserver please write ip, port and botname. \n"
          f"Example: localhost, 2022, Grumpy Gina. The current avaliable bots are .. \n"
          f"Choose the bot that resonates the most with your current mood")

    try:
        ip = input(sys.argv[1])
        port = input(int(sys.argv[2]))

    except:
        print(f"Ip and port must be specified")
        sys.exit()



    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ip, port)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("> ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MESSAGE:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__ == "__main__":
    main()




# Need a loop as long as the client is connected do this ...

# Need input parameter, with possible exit code

