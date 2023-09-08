import socket

serversocket = socket.socket(
    # specifies IPv4 and TCP and creates socket object
    socket.AF_INET, socket.SOCK_STREAM
)

# setting variables
host = socket.gethostname() # host = ip address
port = 444


# binding port and host to a socket
serversocket.bind((host, port))

# setting up listener and how many connections
serversocket.listen(3)

# establishing connection
while True:
    clientsocket, address = serversocket.accept()

    print("connection received from %s" % str(address))

    message = 'Connection established hahaha' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()