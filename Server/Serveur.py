import socket
import threading
import json
import pickle
import time
from Class.Client import *




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

def runGame():
    print("boubou")

def handle_client(client:Client):
    p=[]
    while True:
        try:
            message = client.receive_message()
            
            if not message:
                break
            
            if str(message) == "pret":
                broadcast_message(f"{client.username}: {message}")
                client.send_data({"pret":True})
                p.append(client)
            
            
            if len(p)==2:
                print("aa")
                return
            
                 
        except Exception as e:
            print(f"Erreur de traitement pour {client.address}: {str(e)}")
            break
    
        
    
    # Si le client se déconnecte, le retirer de la liste
    clients.remove(client)
    broadcast_message(f"{client.username} s'est déconnecté.")
    client.socket.close()





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
