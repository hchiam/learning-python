#!/usr/bin/python3

# https://www.freecodecamp.org/learn/information-security/python-for-penetration-testing/creating-a-tcp-client

# socket = internal endpoint for sending and receiving data

import socket
# TODO: modules for encryption, etc.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket family: AF_INET = IPv4, just one way of routing data
# socket type: SOCK_STREAM = TCP, which indicates using a 3-way handshake
#     (UDP would be socket.SOCK_DGRAM)

# host = '192.168.1.###'
host = socket.gethostname()
print(host)
port = 8000
address = (host, port)
client_socket.connect(address)

buffer_size = 1024  # max data size we're allowing client to receive at once
message = client_socket.recv(buffer_size)

client_socket.close()

print(message.decode('ascii'))
