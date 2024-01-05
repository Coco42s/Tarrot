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
        
        self.joueurCarte[str(self.joueur[0].username)] = []
        self.joueurCarte[str(self.joueur[1].username)] = []
        self.joueurCarte[str(self.joueur[2].username)] = []
        
        for i in range(1,int(((78-ch)/3)/3+1)):
            self.joueurCarte[str(self.joueur[0].username)].append(carteDistri[0])
            self.joueurCarte[str(self.joueur[1].username)].append(carteDistri[1])
            self.joueurCarte[str(self.joueur[2].username)].append(carteDistri[2])
            carteDistri = carteDistri[3:]
            
            self.joueurCarte[str(self.joueur[0].username)].append(carteDistri[0])
            self.joueurCarte[str(self.joueur[1].username)].append(carteDistri[1])
            self.joueurCarte[str(self.joueur[2].username)].append(carteDistri[2])
            carteDistri = carteDistri[3:]
            
            self.joueurCarte[str(self.joueur[0].username)].append(carteDistri[0])
            self.joueurCarte[str(self.joueur[1].username)].append(carteDistri[1])
            self.joueurCarte[str(self.joueur[2].username)].append(carteDistri[2])
            carteDistri = carteDistri[3:]
        
        self.chien = carteDistri