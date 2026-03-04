#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# af inet = ipv4, sock stream = tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
server_socket.bind(server_address)

# Limitar el límite de conexiones
server_socket.listen(1)

while True:

    client_socket, client_address =  server_socket.accept()
    data = client_socket.recv(1024)
    
    print(f"\n[+] Mensaje recibido del cliente: {data.decode()}")
    print(f"\n[+] Información del cliente que se ha comunicado con nosotros: {client_address}")

    client_socket.sendall(f"Un saludo crack\n".encode())
    client_socket.close()