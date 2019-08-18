import socket
from threading import Thread

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER = 1024

def msgFromServ(server, thread):
    while thread.is_alive():
        msg = server.recv(BUFFER).decode("utf-8")
        print("\nServer> "+msg)
    server.close()

def msgToServ(client):
    while True:
        msg = input("Client> ")
        client.send(bytes(msg,"utf-8"))
        if msg == "exit":
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
    cl.connect((HOST, PORT))
    
    toServ = Thread(target=msgToServ, args=(cl,))
    fromServ = Thread(target=msgFromServ, args=(cl,toServ))
    toServ.start()
    fromServ.start()

    toServ.join()
    print("to Serv")
    fromServ.join()
    print("frpm Seerv")
    
