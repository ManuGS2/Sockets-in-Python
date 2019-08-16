import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
    cl.connect((HOST, PORT))
    cl.sendall(b'Prueba de mensaje')

    data = cl.recv(1024)

print('Received', repr(data))
