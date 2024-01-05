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
        
        self.carte = []
        self.chien = []
        
        self.joueCarte = []
        self.joueurCarte = {}
        
        self.status = False
            
        
    def run(self):
        self.paquet_carte()
        print(self.carte)
    
    def stop(self, n):
        if n == 1:
            del self
    
    def paquet_carte(self):
        pac = Paquet()
        pac.fabriques() 
        self.carte = pac.get_jeu()
        shuffle(self.carte)
    