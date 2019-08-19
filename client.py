import socket
from threading import Thread

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER = 1024

def msgFromServ(server):
    while True:
        msg = server.recv(BUFFER)
        print("Server> "+str(msg))

def msgToServ(client):
    while True:
        msg = input("Client> ")
        client.send(bytes(msg,"utf-8"))
        if msg == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
    cl.connect((HOST, PORT))
    thrCl = Thread(target=msgFromServ, args=(cl,))
    thrSrv = Thread(target=msgToServ, args=(cl,))
    thrCl.start()
    thrSrv.start()
    thrCl.join()
    thrSrv.join()

    while True:
        msg = input()
        
    data = cl.recv(1024)

print('Received', repr(data))
