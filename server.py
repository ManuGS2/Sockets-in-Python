import socket
from threading import Thread
from sys import stdout

HOST = '127.0.0.1'  #IP standar para el localhost
PORT = 65432        # Puerto válido para la conexion
BUFFER = 1024       # Tamaño del buffer para los mensajes



def connectToClient(serv):
    client, addr = serv.accept()    # Habilita las conexiones /se retoner un Objeto socket y una tupla con la direccion del cliente (host, port)
    print("Se ha conectado {}".format(addr))    # Accept devulve un socket (el del cliente) y su dir. de acuerdo a la AF
    
    fromCl = Thread(target=msgFromCl, args=(client,))
    toCl = Thread(target=msgToCl, args=(client,fromCl))
    fromCl.start()
    toCl.start()
    
    fromCl.join()
    print("from CL")
    toCl.join()
    print("to Cl")


def msgFromCl(client):
    while True:
        msg = client.recv(BUFFER).decode("utf-8")
        if msg == "exit":
            stdout.flush()
            break
        else:
            print("\nClient> " + msg)

def msgToCl(client, thread):
    while True:
        if thread.is_alive():
            client.send(bytes(input("Server> "), "utf-8"))
        else:
            break
    client.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
        serv.bind((HOST, PORT))   # Asocia el puerto y la dirección a la iterfaz
        serv.listen()             # Pone el puerto a escuchar
        
        print("Esperando una conexion...")
        connectToClient(serv)
main()