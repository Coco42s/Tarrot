from Client import *



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
        