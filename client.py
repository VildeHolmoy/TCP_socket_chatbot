import socket


# Need to make connection to server

# Instansiates a client socket
#clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects client to server, corresponds with ip and port in server.py
#clientSocket.connect((2022))

IP = socket.gethostbyname(socket.gethostname())
PORT = 2022
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
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

