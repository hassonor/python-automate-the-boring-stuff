import socket

machine = input("Enter the target Name or IP: ")
IPScanned = socket.gethostbyname(machine)

print("Scanning {} ({}) For Open Ports....".format(machine, IPScanned))

for port in range(12344, 12359):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((IPScanned, port))  # connect_ex return an error
    if result == 0:
        print("PORT {}: Open".format(port))
    else:
        print("PORT {}:".format(port))
    s.close()
