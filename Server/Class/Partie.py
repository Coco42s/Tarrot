from tracemalloc import stop
from Client import *
from Paquet  import * 



class Partie:
    
    
    def __init__(self):
        self.nbJoueur = 0
        self.joueur = ""
        
        self.valeurPris = 0
        
        self.pointPris = 0
        self.pointAutre = 0
        
        self.apelRoix = ""
        
        self.carte = []
        self.chien = []
        
        self.joueCarte = []
        self.joueurCarte = {}
        
        self.status = True
            
        
    def run(self):
        self.paquet_carte()
        print(self.carte)
    
    def stop(self, n):
        if n == 1:
            del self
    
    def paquet_carte(self):
        pac = Paquet()
        pac.fabriques() 
        self.carte = pac.get_jeu
    