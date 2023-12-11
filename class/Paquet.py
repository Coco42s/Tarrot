from Carte import *
class Paquet:
    """ Sette class représente un paquet
    
    attribut : 
        - jeu(list) : paquet
        - couleur(list) : liste des couleur
    metode :
        - fabrique
        - init
    """
    def __init__(self):
        self.__jeu = []
        self.__couleurs = ["Carreau","Coeur","Pique","Trèfle"]
        
    def fabriques(self):
        if self.__jeu == []:
            paquet = [Carte("Excuse",42)]
            for c in self.__couleurs:
                for v in range(1,15):
                    paquet.append(Carte(c,v))
            for i in range(1,22):
                paquet.append(Carte("Atout",i))
                self.__jeu = paquet
            return 
        return "Paquet déga fais"
                
    def get_jeu(self):
        return self.__jeu
    
    def melanger(self):
        return 0