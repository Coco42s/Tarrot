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

    def attent(self):
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(f"Vous etes dans une partie a {self.nbJoueur} joueurs !\n Les joueur sont :")
            for i in range(self.nbJoueur):
                self.joueur[i].send_message(f"{self.joueur[i].username}")
            self.joueur[i].send_message("\n\nAppuiller sur pres pour commencer.")
        
                
            
        
    def run(self):
        self.paquet_carte()
        
        if self.nbJoueur == 5:
            self.nbChien = 3
        
        self.distribut(self.nbChien)
        
        self.prend()
        
    def broadcast_player(self, message):
        for client in self.joueur:
            try:
                client.send_message(message)
            except:
                pass
        
        
    def stop(self, n):
        if n == 1:
            del self
    
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
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_message(str(self.joueurCarte[str(self.joueur[i].username)]))
        
        for i in range(self.nbJoueur):
            self.joueur[i].send_data("carteDist",str(self.joueurCarte[str(self.joueur[i].username)]))
        
        time.sleep(2)
        
        for i in range(self.nbJoueur):
            self.joueur[i].bloced_carte()

    def prend(self):
        temp = []
        for i in range(self.nbJoueur):
            self.joueur[i].send_message("0 : Passe\n1 : Petit\n2 : Garde\n3 : Garde Sans\n4 : Garde Contre\n\nVeuiller écrire votre choix dans le chanel serveur")
            while True:
                choix = self.joueur[i].receive_message_serv()
                if choix != 0 and choix != 1 and choix != 2 and choix != 3 and choix != 4:
                    self.joueur[i].send_server("Veuiller choisir un chifre entre 0 et 4")
                else:
                    temp.append(choix)
                    break
        for i in range(len(temp)):
            if temp[i]==max(temp):
                self.broadcast_player(f"Le joueur {self.joueur[i].username} a pris !")
                self.valeurPris = max(temp)
                self.joueurPris = self.joueur[i]
                break
                
                
                
                
        