import socket

HOST = "127.0.0.1"  # The Local IP for loopback
PORT = 12345  # The server's Port

with socket.socket(socket.AF_INET,
                   socket.SOCK_STREAM) as s:  # params: socket.AF_INET is the network protocol and socket.SOCK_STREAM is the type of socket (send and receive TCP packets)
    s.bind((HOST, PORT))  # binding the Host and Post after the Socket class were created
    s.listen()  # Open a listener for waiting for traffic
    print("[R]Ready")
    while True:  # This loop will keep the listener open and ready - which accept a key piece of information -> who sent the message
        client, addr = s.accept()  # Wait for a message using the accept function
        with client:
            print(f"[S] Incoming Message From: {addr}")
            data = client.recv(4096)  # recv function is called with a message size boundary
            if data == b"Disconnect":
                print("[E] End of Message From " + str(addr))
                break
