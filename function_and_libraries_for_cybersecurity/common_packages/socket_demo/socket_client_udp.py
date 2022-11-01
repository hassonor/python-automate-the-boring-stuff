import socket

HOST = "127.0.0.1"  # The Local IP for loopback
PORT = 12345  # The server's Port

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# No Connect as UDP is connection less
s.sendto(b"ORHASSONWASHERE", (HOST, PORT))

data, addr = s.recv(4096)
print(data)
