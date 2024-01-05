import socket
import threading
import json
import pickle
import time
from Class.Client import *
from Class.Paquet import Paquet
from Class.Partie import Partie

#---Send Message

def tchat_msg_send(message, lst):
    for client in lst:
        try:
            client.send_tchat(message)
        except:
            # En cas d'erreur, le client peut être retiré de la liste
            clients.remove(client)

def broadcast_message(message):
    for client in clients:
        try:
            client.send_message(message)
        except:
            # En cas d'erreur, le client peut être retiré de la liste
            clients.remove(client)


#---Acpet conection
            
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Nouvelle connexion de {client_address}")

        # Création d'une instance Client pour gérer le client
        client = Client(client_socket, client_address)

        # Demander le nom d'utilisateur au client
        client.send_message("Hello !\nVas Voir le chanel Serveur !")
        username = client.receive_message()
        client.username = username

        # Ajouter le client à la liste
        clients.append(client)

        # Envoyer un message de bienvenue
        client.send_server(f"Bienvenue, {username}!\nVous voulez jouer dans une partie a 3, 4 ou 5 joueur ?")
        
        
        while True:
            choix = client.receive_message_serv()
            if choix == '3':
                partie3.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 3 joueur !\nLe tchat de la partie est disponible !")
                client_tchat_thread = threading.Thread(target=tchat_p3, args=(client,))
                client_tchat_thread.start()
                break
            if choix == '4':
                partie4.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 4 joueur !\nLe tchat de la partie est disponible !")
                client_tchat_thread = threading.Thread(target=tchat_p4, args=(client,))
                client_tchat_thread.start()
                break
            if choix == '5':
                partie5.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 5 joueur !\nLe tchat de la partie est disponible !")
                client_tchat_thread = threading.Thread(target=tchat_p5, args=(client,))
                client_tchat_thread.start()
                break
            client.send_server(f"\nVous devez choisire 3, 4 ou 5 ?")
        
        
        time.sleep(0.1)


#---Partie Vérif

def verifPartie():
    global partie3
    while True:
        if len(partie3) == 1:
            if ptt3.status == False:
                ptt3.status = True
                ptt3.nbJoueur = 1
                ptt3.joueur = [partie3[0]]
                partie3 = partie3[1:]
                ptt3.run()
            pass
            
        if len(partie4) == 4:
            pass
        if len(partie4) == 5:
            pass
        
        time.sleep(1)


#---Partie 3

def tchat_p3(client:Client):
    while True:
        try:
            message = client.receive_message_tchat()
            
            tchat_msg_send(f"{client.username} : {message}", partie3)
                 
        except Exception as e:
            print(f"Erreur de traitement pour {client.address}: {str(e)}")
            break
    # Si le client se déconnecte, le retirer de la liste
    clients.remove(client)
    broadcast_message(f"{client.username} s'est déconnecté.")
    client.socket.close()



#---Partie 4

def tchat_p4(client:Client):
    while True:
        try:
            message = client.receive_message_tchat()
            
            tchat_msg_send(f"{client.username} : {message}", partie4)
                 
        except Exception as e:
            print(f"Erreur de traitement pour {client.address}: {str(e)}")
            break
    # Si le client se déconnecte, le retirer de la liste
    clients.remove(client)
    broadcast_message(f"{client.username} s'est déconnecté.")
    client.socket.close()



#---Partie 5

def tchat_p5(client:Client):
    while True:
        try:
            message = client.receive_message_tchat()
            
            tchat_msg_send(f"{client.username} : {message}", partie5)
                 
        except Exception as e:
            print(f"Erreur de traitement pour {client.address}: {str(e)}")
            break
    # Si le client se déconnecte, le retirer de la liste
    clients.remove(client)
    broadcast_message(f"{client.username} s'est déconnecté.")
    client.socket.close()





#---Main

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
    
    partie3 = []
    partie4 = []
    partie5 = []
    
    ptt3 = Partie()
    ptt4 = Partie()
    ptt5 = Partie()
    
    # Thread pour vérif partie
    PartVerf = threading.Thread(target=verifPartie)
    PartVerf.start()

    # Thread pour accepter les connexions
    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()
    
