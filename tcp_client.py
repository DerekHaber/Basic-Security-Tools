import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

#connecting to socket
clientsocket.connect((host, port))

# setting max bytes of data to receive
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))