import socket
from threading import Thread

HOST = '127.0.0.1'  #IP standar para el localhost
PORT = 65432        # Puerto válido para la conexion
BUFFER = 1024       # Tamaño del buffer para los mensajes



def connectToClient(serv):
    client, addr = serv.accept()    # Habilita las conexiones /se retoner un Objeto socket y una tupla con la direccion del cliente (host, port)
    print("Se ha conectado {}".format(addr))    # Accept devulve un socket (el del cliente) y su dir. de acuerdo a la AF
    
    thrCl = Thread(target=msgFromCl, args=(client,serv))
    thrSrv = Thread(target=msgToCl, args=(client,))
    thrCl.start()
    thrSrv.start()
    thrCl.join()
    thrSrv.join()


def msgFromCl(client, server):
    while True:
        msg = client.recv(BUFFER)
        if msg == "exit":
            break
        else:
            print("Client> " + str(msg))

def msgToCl(client):
    while True:
        client.send(bytes(input("Server> "), "utf-8"))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
        serv.bind((HOST, PORT))   # Asocia el puerto y la dirección a la iterfaz
        serv.listen()             # Pone el puerto a escuchar
        
        print("Esperando una conexion...")
        connectToClient(serv)
main()