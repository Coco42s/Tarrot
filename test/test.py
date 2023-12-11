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
            msg = pickle.dumps({'afficher': True, 'data': data})
            self.socket.sendall(msg)
        except socket.error as e:
            print(f"Erreur lors de l'envoi du message à {self.address}: {str(e)}")
    
    def receive_message(self):
        return self.socket.recv(1024).decode()

def handle_client(client:Client):
    while True:
        try:
            message = client.receive_message()
            if not message:
                break

            # Traitement du message
            broadcast_message(f"{client.username}: {message}")
        except Exception as e:
            print(f"Erreur de traitement pour {client.address}: {str(e)}")
            break

    # Si le client se déconnecte, le retirer de la liste
    clients.remove(client)
    broadcast_message(f"{client.username} s'est déconnecté.")
    client.socket.close()

def broadcast_message(message):
    for client in clients:
        try:
            client.send_message(message)
        except:
            # En cas d'erreur, le client peut être retiré de la liste
            clients.remove(client)
            
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Nouvelle connexion de {client_address}")

        # Création d'une instance Client pour gérer le client
        client = Client(client_socket, client_address)

        # Demander le nom d'utilisateur au client
        client.send_message("Hello !")
        username = client.receive_message()
        client.username = username

        # Ajouter le client à la liste
        clients.append(client)

        # Envoyer un message de bienvenue
        client.send_message(f"Bienvenue, {username}!\n")

        time.sleep(0.1)
        
        # Informer tout le monde de la nouvelle connexion
        broadcast_message(f"{username} s'est connecté.")

        # Démarrer un thread pour gérer le client
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()

if __name__ == "__main__":
    # Configuration du serveur
    host = "127.0.0.1"
    port = 5566

    # Création du socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur en attente de connexions sur {host}:{port}")

    # Liste des clients connectés
    clients = []

    # Thread pour accepter les connexions
    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()
