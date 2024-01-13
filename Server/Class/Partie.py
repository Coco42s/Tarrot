from os import abort
from Class.Client import *
from Class.Paquet  import * 
from random import *


class Partie:
    
    def __init__(self):
        self.nbJoueur = 0
        self.joueur = []
        
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
        
        self.status = False

        
# Status

    def attent(self):
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"Vous etes dans une partie a {self.nbJoueur} joueurs !\n Les joueur sont :")
            for i in range(self.nbJoueur):
                self.joueur[i].send_message(f"{self.joueur[i].username}")
            self.joueur[i].send_message("\n\nAppuiller sur pres pour commencer.")
                
    def rl(self, st = True):
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
        self.paquet_carte()
        
        if self.nbJoueur == 5:
            self.nbChien = 3
        
        self.distribut(self.nbChien)
        
        self.prend()

# Comm
        
    def broadcast_player(self, message):
        for client in self.joueur:
            try:
                client.send_message(message)
            except:
                pass

    def broadcast_tchat(self, message):
        for client in self.joueur:
            try:
                client.send_tchat(message)
            except:
                print("Brod error")

    def tchat(self, client:Client):
        while True:
            try:
                message = client.receive_message_tchat()
                self.broadcast_tchat(f"{client.username} : {message}")   
            except:
                print("Tchat error")

    def tchatStart(self):
        for i in range(self.nbJoueur):
            client_tchat_thread = threading.Thread(target=self.tchat, args=(self.joueur[i],))
            client_tchat_thread.start()
            
        
# Jeux
   
    def paquet_carte(self):
        pac = Paquet()
        pac.fabriques() 
        self.carte = pac.get_jeu()
        shuffle(self.carte)
    
    def distribut(self, ch):
        carteDistri = self.carte
        
        for i in range(self.nbJoueur):
            self.joueurCarte[str(self.joueur[i].username)] = []
        
        for i in range(1,int(((78-ch)/3)/3+1)):
            for i in range(self.nbJoueur):
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[i])
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[i+1])
                self.joueurCarte[str(self.joueur[i].username)].append(carteDistri[i+2])
                carteDistri = carteDistri[3:]
        
        self.chien = carteDistri
        
        #for i in range(self.nbJoueur):
        #    self.joueur[i].send_message(str(self.joueurCarte[str(self.joueur[i].username)]))
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_data("carteDist",str(self.joueurCarte[str(self.joueur[i].username)]))
        
        time.sleep(5)
        
        for i in range(self.nbJoueur):
            self.joueur[i].bloced_carte()

    def prend(self):
        temp = []
        for i in range(self.nbJoueur):
            self.joueur[i].send_message("\n0 : Passe\n1 : Petit\n2 : Garde\n3 : Garde Sans\n4 : Garde Contre\n\nVeuiller écrire votre choix dans le chanel serveur\n")
            ta = True
            while ta:
                print("85")
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
            time.sleep(0.5)
            
        if all(x == "0" for x in temp):
            self.broadcast_player(f"Tout le monde passe on recomence !")
        
        else: 
            for i in range(len(temp)):
                if temp[i]==max(temp):
                    self.broadcast_player(f"Le joueur {self.joueur[i].username} a pris !")
                    self.valeurPris = max(temp)
                    self.joueurPris = self.joueur[i]
                    break
                
                
                
                
        