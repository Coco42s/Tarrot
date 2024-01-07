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
            msg = pickle.dumps({'afficher': True, 'affich': message})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")

    def send_data(self, obj, data):
        try:
            msg = pickle.dumps({'obj':obj, 'data': data})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    def send_tchat(self, message):
        try:
            msg = pickle.dumps({'tchat':message})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    def send_server(self, message):
        try:
            msg = pickle.dumps({'serv':message})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    
    def receive_message_serv(self):
        while True:
            try:
                if self.socket.fileno() == -1:
                    # Le socket n'est plus valide, fermez proprement la connexion
                    self.socket.close()
                    break
                data = self.socket.recv(1024)
                message = pickle.loads(data)
                try:
                    if message["serv"]:
                        return message["serv"]
                except:
                    pass
            except socket.error as e:
                print(e)
                break
            
    
    def receive_message_tchat(self):
        data = self.socket.recv(1024)
        message = pickle.loads(data)
        try:
            if message['tchat']:
                return message['tchat']
        except socket.error as e:
            pass
    
    def receive_data_serv(self):
        data = self.socket.recv(1024)
        message = pickle.loads(data)
        try:
            if message['data']:
                return message['data']
        except socket.error as e:
            pass
    
    def receive_message(self):
        return self.socket.recv(1024).decode()
 
    
    def libéré_carte(self):
        try:
            msg = pickle.dumps({'obj':"cAct", 'data': str(True)})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    def bloced_carte(self):
        try:
            msg = pickle.dumps({'obj':"cAct", 'data': str(False)})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    
    