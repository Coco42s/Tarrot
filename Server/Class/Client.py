import socket
import threading
import json
import pickle
import time


class Client:
    def __init__(self, socket:socket.socket, address):
        self.socket = socket
        self.address = address
        self.username = None
    
    def send_message(self, message):
        try:
            msg = pickle.dumps({'afficher': True, 'data': message})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")

    def send_data(self, data):
        try:
            msg = pickle.dumps({'afficher': False, 'data': data})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    def receive_message(self):
        return self.socket.recv(1024).decode()