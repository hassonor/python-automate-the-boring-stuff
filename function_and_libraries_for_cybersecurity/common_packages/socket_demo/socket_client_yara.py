import socket

import yara
import os

HOST = "127.0.0.1"  # The Local IP for loopback
PORT = 12345  # The server's Port

directory = '/orhme'
yara_rules = yara.compile(filepath='/orhme/yara_rules/test_rule.yar')

for filename in os.listdir(directory):
    matches = yara_rules.match(data=filename)
    if matches:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.send(filename + b": Matched and Possibly Infected :(")
            data = s.recv(2048)
    else:
        print(filename + ": Clean :)")
