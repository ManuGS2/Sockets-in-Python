import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv:
    serv.bind((HOST, PORT))       # Asocia el socket a la interfaz y la dirección
    serv.listen()                 # Pone el puerto a escuchar
    conn, addr = serv.accept()    # Habilita las conexiones /se retoner un Objeto socket y una tupla con la direccion del cliente (host, port)
                                  # Accept devulve un socket (el del cliente) y su dir. de acuerdo a la AF
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)