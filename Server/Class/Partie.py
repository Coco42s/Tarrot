from Class.Client import *
from Class.Paquet  import * 
from random import *


class Partie:
    
    
    def __init__(self):
        self.nbJoueur = 0
        self.joueur = []
        
        self.valeurPris = 0
        
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
            
        
    def run(self):
        self.paquet_carte()
        
        if self.nbJoueur == 5:
            self.nbChien = 3
        
        self.distribut(self.nbChien)
        
        print(self.joueurCarte[str(self.joueur[0].username)])
        print(self.chien)
    
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
            self.joueur[i].send_data("carteDist","aaaa")
        
        