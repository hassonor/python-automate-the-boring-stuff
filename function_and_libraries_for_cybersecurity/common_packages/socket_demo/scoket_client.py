import socket
import sys

HOST = "127.0.0.1"  # The Local IP for loopback
PORT = 12345  # The server's Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(sys.argv[1], 'utf-8'))  # Dropping a message in the arg for control what will send to server
    data = s.recv(4096)

print(data)
