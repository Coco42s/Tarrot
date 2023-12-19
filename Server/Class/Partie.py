from tracemalloc import stop
from Client import *
from Paquet  import * 



class Partie:
    
    
    def __init__(self, nb_joueur, joueur):
        self.nbJoueur = nb_joueur
        self.joueur = joueur
        
        self.valeurPris = 0
        
        self.pointPris = 0
        self.pointAutre = 0
        
        self.apelRoix = ""
        
        self.carte = []
        self.chien = []
        
        self.joueCarte = []
        self.joueurCarte = {}
        
        if len(joueur) != nb_joueur:
            self.stop(1)
            
        self.paquet_carte()
        print(self.carte)
        
    def run(self, nb_joueur, joueur):
        pass
    
    def stop(self, n):
        if n == 1:
            del self
    
    def paquet_carte(self):
        pac = Paquet()
        pac.fabriques() 
        self.carte = pac.get_jeu
    