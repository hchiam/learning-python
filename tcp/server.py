# https://www.freecodecamp.org/learn/information-security/python-for-penetration-testing/understanding-sockets-and-creating-a-tcp-server

# socket = internal endpoint for sending and receiving data

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket family: AF_INET = IPv4, just one way of routing data
# socket type: SOCK_STREAM = TCP, which indicates using a 3-way handshake

# host = '192.168.1.###'
host = socket.gethostname()
print(host)
port = 8000
address = (host, port)
server_socket.bind(address)

how_many_simultaneous_connections = 3
server_socket.listen(how_many_simultaneous_connections)

while True:
    client_socket, client_address = server_socket.accept()
    print('received connection from ' + str(address))
    message_to_client = 'you connected to the server'
    server_socket.send(message_to_client.encode())
    client_socket.close()
