#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def start_client():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hola, servidor!")
        data = s.recv(1024)

    print(f"[+] Mensaje recibido del servidor: {data.decode()}")


start_client()