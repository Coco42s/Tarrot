import socket
import threading
import json
import pickle
import time
from Class.Client import *
from Class.Paquet import Paquet
from Class.Partie import Partie

#---Send Message

def broadcast_message(message):
    """envoi un message a tout les client

    Args:
        message (_str_): message
    """
    for client in clients:
        try:
            client.send_message(message)
        except:
            # En cas d'erreur, le client peut être retiré de la liste
            clients.remove(client)


#---Acpet conection
            
def accept_connections():
    """Permai d'accépter les conection et géré ou elle vont
    """
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Nouvelle connexion de {client_address}")

        # Création d'une instance Client pour gérer le client
        client = Client(client_socket, client_address)

        # Demander le nom d'utilisateur au client
        username = client.receive_message()
        client.username = username
        client.send_message(f"Hello {username} !\nVas Voir le chanel Serveur !")

        # Ajouter le client à la liste
        clients.append(client)

        # Envoyer un message de bienvenue
        client.send_server(f"Bienvenue, {username}!\nVous voulez jouer dans une partie a 3, 4 ou 5 joueur ?\n")
        
        at = True
        while at:
            choix = client.receive_message_serv()
            if choix == '3':
                partie3.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 3 joueur !\n\nLe tchat sera disponible une foix dans une partie !\n")
                #client_tchat_thread = threading.Thread(target=tchat_p3, args=(client,))
                #client_tchat_thread.start()
                at = False
            if choix == '4':
                partie4.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 4 joueur !\n\nLe tchat d'attante des partie a quatre joueur est disponible !\n")
                client_tchat_thread = threading.Thread(target=tchat_p4, args=(client,))
                client_tchat_thread.start()
                at = False
            if choix == '5':
                partie5.append(client)
                client.send_server(f"\nVous avez été mis en attent dans une partie a 5 joueur !\n\nLe tchat d'attante des partie a cinq joueur est disponible !\n")
                client_tchat_thread = threading.Thread(target=tchat_p5, args=(client,))
                client_tchat_thread.start()
                at = False
            if choix != '3' and choix != '4' and choix != '5':
                client.send_server(f"Vous devez choisire 3, 4 ou 5 ?\n")
        
        
        time.sleep(0.1)


#---Partie Vérif

def verifPartie():
    """Vérifit les partie pou les remplire
    """
    global partie3
    while True:
        if len(partie3) == 1:
            if ptt3.status == False:
                ptt3.status = True
                ptt3.nbJoueur = 1
                ptt3.joueur = [partie3[0]]
                partie3 = partie3[3:]
                #ptt3.tchatStart()
                ptt3.run()
            pass
        #if len(partie3) == 3:
        #    if ptt3.status == False:
        #        ptt3.status = True
        #        ptt3.nbJoueur = 3
        #        ptt3.joueur = [partie3[0],partie3[1],partie3[2]]
        #        partie3 = partie3[3:]
        #        #ptt3.tchatStart()
        #        ptt3.run()
        #    pass
            
        if len(partie4) == 4:
            if len(partie3) == 4:
                if ptt3.status == False:
                    ptt3.status = True
                    ptt3.nbJoueur = 4
                    ptt3.joueur = [partie4[0],partie4[1],partie4[2],partie4[3]]
                    partie3 = partie3[4:]
                    #ptt3.tchatStart()
                    ptt3.run()
                pass
        if len(partie4) == 5:
            if len(partie3) == 5:
                if ptt3.status == False:
                    ptt3.status = True
                    ptt3.nbJoueur = 5
                    ptt3.joueur = [partie5[0],partie5[1],partie5[2],partie5[3],partie5[4]]
                    partie3 = partie3[5:]
                    #ptt3.tchatStart()
                    ptt3.run()
                pass
        
        time.sleep(1)

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
    
