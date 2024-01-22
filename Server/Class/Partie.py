import re
from os import abort
from Class.Client import *
from Class.Paquet  import * 
from random import *


class Partie:
    """Permet de géré un partie
    """
    
    def __init__(self,nb_joueur:int):
        """init class
        """
        self.nbJoueur = nb_joueur
        self.joueur = []
        
        self.valeurPris = 0
        self.joueurPris = ""
        
        self.pointPris = 0
        self.cartePris =[]
        
        self.pointAutre = 0
        self.carteAutre = []
        
        self.apelRoix = ""
        
        if nb_joueur == 5:
            self.nbChien = 6
        else:
            self.nbChien = 3
            
        
        self.carte = []
        self.chien = []
        
        self.joueCarte = []
        self.joueurCarte = {}
        
        self.nbToure = int(((78-self.nbChien)/3)/self.nbJoueur)
        
        self.status = False

        
# Status

    def attent(self):
        """Attent tout les joueur et annonce certaine chose, (nes pas utiliser)
        """
        tchat_thread = threading.Thread(target=self.tchat_gestion, args=())
        tchat_thread.start()
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_tchat(f"BPB")
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"Vous etes dans une partie a {self.nbJoueur} joueurs !\n")
                          
    def rl(self, st = True):
        """Un relise non fonctionel

        Args:
            st (bool, optional): por savoir le type de rel. Defaults to True.
        """
        if st:
            self.__init__()
        else:
            
            self.valeurPris = 0
            self.joueurPris = ""
            
            self.pointPris = 0
            self.cartePris =[]
            
            self.pointAutre = 0
            self.carteAutre = []
            
            self.apelRoix = ""
            self.nbChien = 6
            
            self.carte = []
            self.chien = []
            
            self.joueCarte = []
            self.joueurCarte = {}
            
            self.run()
        
    def run(self):
        """Run  la game
        """
        #self.attent()
        
        self.paquet_carte()
        
        if self.nbJoueur == 5:
            self.nbChien = 3
        
        self.distribut(self.nbChien)
        
        self.prend()

# Comm
        
    def broadcast_player(self, message):
        """Envoi a tout les joueur

        Args:
            message (str): message
        """
        for client in self.joueur:
            try:
                client.send_message(message)
            except:
                pass

    def tchat(self, client:Client):
        """non utiliser

        Args:
            client (Client): socket client
        """
        while True:
            try:
                message = client.receive_message_tchat()
                for client in self.joueur:
                    try:
                        client.send_tchat(message)
                    except:
                        print("Brod error") 
            except:
                print("Tchat error")

    def tchatStart(self):
        """start le tchat, (non utiliser)
        """
        for i in range(self.nbJoueur):
            client_tchat_thread = threading.Thread(target=self.tchat, args=(self.joueur[i],))
            client_tchat_thread.start()

    def tchat_gestion(self):
        """non utiliser, gestion du tchat
        """
        # Configuration du serveur tchat
        host = "127.0.0.1"
        port = 5567

        # Création du socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"Serveur tchat en attente de connexions sur {host}:{port}")
        
        clients_t = []
        while len(clients_t) != self.nbJoueur:
            client_socket, client_address = server_socket.accept()
            print(f"Nouvelle connexion de {client_address}")

            # Création d'une instance Client pour gérer le client
            client = Client(client_socket, client_address)
            
            clients_t.append(client)
        
        for i in range(self.nbJoueur):
            client_tchat_thread = threading.Thread(target=self.tchat, args=(clients_t[i],))
            client_tchat_thread.start()
        
        
        pass

            
        
# Jeux
   
    def paquet_carte(self):
        """créé le packet de carte et le mélenge
        """
        pac = Paquet()
        pac.fabriques() 
        self.carte = pac.get_jeu()
        shuffle(self.carte)
    
    def distribut(self, ch):
        """Distribut les carte

        Args:
            ch (int): nombre de carte au chien
        """
        carteDistri = self.carte
        
        for i in range(self.nbJoueur):
            self.joueurCarte[str(self.joueur[i].username)] = []
        
        for i in range(1,int(((78-ch)/3)/3+1)):
            for i in range(self.nbJoueur):
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[0])
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[1])
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[2])
                carteDistri = carteDistri[3:]
        
        self.chien = carteDistri
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(str(self.joueurCarte[str(self.joueur[i].username)]))
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_data("carteDist",str(self.joueurCarte[str(self.joueur[i].username)]))
        
        #time.sleep(5)
        
        for i in range(self.nbJoueur):
            self.joueur[i].bloced_carte()

    def prend(self):
        """Savoir qui prent
        """
        temp = []
        for i in range(self.nbJoueur):
            self.joueur[i].send_message("\n0 : Passe\n1 : Petit\n2 : Garde\n3 : Garde Sans\n4 : Garde Contre\n\nVeuiller écrire votre choix dans le chanel serveur\n")
        for i in range(self.nbJoueur):
            ta = True
            while ta:
                print("85")
                self.broadcast_player(f"A {self.joueur[i].username} de choisire.")
                choix = self.joueur[i].receive_message_serv()
                if choix != "0" and choix != "1" and choix != "2" and choix != "3" and choix != "4":
                    self.joueur[i].send_server("Veuiller choisir un chifre entre 0 et 4 !\n")
                else:
                    temp.append(choix)
                    self.joueur[i].send_server(f"Vous avez choisie {choix}\n")
                    ta = False
            if choix == "0": self.broadcast_player(f"Le joueur {self.joueur[i].username} a choisi de passer !\n")
            if choix == "1": self.broadcast_player(f"Le joueur {self.joueur[i].username} a choisi une Petit !\n")
            if choix == "2": self.broadcast_player(f"Le joueur {self.joueur[i].username} a choisi une Garde !\n")
            if choix == "3": self.broadcast_player(f"Le joueur {self.joueur[i].username} a choisi une Garde Sans \n!")
            if choix == "4": self.broadcast_player(f"Le joueur {self.joueur[i].username} a choisi une Garde Contre !\n")
            #time.sleep(0.5)
            
        if all(x == "0" for x in temp):
            self.broadcast_player(f"Tout le monde passe on recomence !\n")
        
        else: 
            for i in range(len(temp)):
                if temp[i]==max(temp):
                    self.broadcast_player(f"Le joueur {self.joueur[i].username} a pris !\n")
                    self.valeurPris = max(temp)
                    self.joueurPris = i
                    break
                
        self.chien__creation()
        return
                
    def chien__creation(self):
        """permet de créé son chien
        """
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"Le chien est : {self.chien}\n") 
            
        #time.sleep(5)
            
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"On attent que le preneur fasse sont chien dans le chanel serveur !\n")   
        
        self.joueur[int(self.joueurPris)].send_server(f"Veuiler rentré les carte choisie pour le chien une a une sour le forma 'couleur + valeur'\nExemple : 'Excuse 42'\n\nLes couleur possible sont (Pique, Trèfle, Coeur, Carreau, Atout, Excuse)\nLes valeur vont de 1 a 14 pour les carte ordinaire pour les atout sa vas de 1 a 21 et l'excuse sais 42")
        
        
        
        carte_chien = []
        carte_valide = self.joueurCarte[self.joueur[int(self.joueurPris)].username] + self.chien
        r_in_c = False
        for i in range(self.nbChien):
            ta = True
            while ta:
                choix = self.joueur[int(self.joueurPris)].receive_message_serv()
                if not re.match(r"^(Excuse|Atout)\s(42|21|1)$", choix):
                    for objet in carte_valide:
                        if str(objet) == choix:
                            if re.match(r"^(Pique|Trèfle|Coeur|Carreau)\s(14)$", choix):
                                r_in_c = True
                            carte_chien.append(choix)
                            self.joueur[int(self.joueurPris)].send_server(carte_chien)
                            ta = False
                        else:
                            self.joueur[int(self.joueurPris)].send_server("Error")
                else:
                    self.joueur[int(self.joueurPris)].send_server("Error Vous pouver pas utiliser cette carte !")
        
        self.joueur[int(self.joueurPris)].send_server(f"Ton chien est : {carte_chien}")
        
        for i in carte_chien:
            carte_valide.revove(i)
        
        self.joueurCarte[self.joueur[int(self.joueurPris)].username] = carte_valide
        
        self.joueur[int(self.joueurPris)].send_data("carteDist",str(self.joueurCarte[self.joueur[int(self.joueurPris)].username]))
        
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"Le prenneur a Terminer sont chien !\n")  
            
        if r_in_c:
            for i in range(self.nbJoueur):
                self.joueur[i].send_message(f"Roix au Chien !!!\n")  
                   
                
                #if re.match(r"^(Pique|Trèfle|Coeur|Carreau|Excuse|Atout)\s(42|2[0-1]|1[0-9]|[1-9])$", choix):
                #    if re.match(r"^(Atout)\s(2[]|1[0-9]|[1-9])$", choix):
                #        pass
                #    
                #    if re.match(r"^(Excuse)\s(42)$", choix):
                #        pass
                #    
                #    if re.match(r"^(Pique|Trèfle|Coeur|Carreau)\s(1[0-4]|[1-9])$", choix):
                #        pass
                #else:
                #    self.joueur[int(self.joueurPris)].send_server(f"Erreur de Forma (le forma est 'Atout 10')")
        
        return
    
    def jeux(self):
        """boucle du jeux
        """
        for i in range(self.nbToure):
            pass
        pass             
                
                
        