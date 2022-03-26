TCP sockets  - chatroom with bots

To start the chatroom you need 1 instance of server.py, and 4 instances of client.py. \
The server needs to start first. \
Enjoy chatting with the bots! They have some great ehhhhhm "personalities". \
.........................................................................................................................................

The bots in this program is: \
Holly \
Gina \
Carl \
Ralph 

\
To start server.py: \
Open terminal and write: python server.py 'portnumber' \
Example: python server.py 2022 \
For a description of each bot, instead of port number write: "--describebotname". \
Example: python server.py --describeHolly

To start client.py: \
Open terminal and write: python client.py 'IP', example: localhost 'portnumber' \
Example: python client.py localhost 2022 \
If you need help write "--help" instead of IP-address. \
Example: python client.py --help

 

\
\
Assignment requirements:

- The server should accept any connection
- The program works as a chatroom where the clients are bots
- All responses from one client should be sent back to all other clients except the one who sent it
- I can decide when and how to disconnect clients
- The server should take input from the command line
- There should be a list of connected clients
- The bots are not the first to speak, but they will always respond
