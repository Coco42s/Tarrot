class Carte:
    """ Cette classe représente une carte
    atributs : 
        - couleurs(str) : Couleur de la carte 
        - valeurs(int) : valeur de la carte
        - honneurs(dic) : dictionère avec les honneur
    
    methode : 
        - asséseur : accédé a vouleur et valeur
        - calculer_point : renvoit un int qui est la valeur en point de la carte
        - __str__ : str
        - __rper__ :
    
    """
    def __init__(self, couleur, valeur):
        self.__couleur = couleur
        self.__valeur = valeur
        self.__honneurs = {1:"As",11:"Valet",12:"Cavalier",13:"Dame",14:"Roi"}
    
    def get_valeur(self):
        return self.__valeur
    
    def get_couleur(self):
        return self.__couleur
    
    def calcul_points(self):
        if self.__couleur != "Atout" and self.__couleur != "Excuse":
            print("Bonjour")
            for i in self.__honneurs:
                if (i == self.__valeur) and (i != 1) :
                    return i-10+0.5
            return 0.5
        else: 
            if self.__valeur == 1 or 21 or 42:
                return 4.5
            else:
                return 0.5
    
    def __str__(self):
        return "0"
    
    def __repr__(self):
        if self.__couleur == "Atout":
            return f"{self.__couleur} {self.__valeur}"
        if self.__couleur == "Excuse":
            return f"{self.__couleur}"
        if self.__valeur <= 10 and self.__couleur != "Atout" and self.__couleur != "Excuse":
            return f"{self.__couleur} {self.__valeur}"
        if self.__valeur >= 10 and self.__couleur != "Atout" and self.__couleur != "Excuse":
            for i in self.__honneurs:
                if i != 1:
                    return f"{self.__honneurs[self.__valeur]} de {self.__couleur}"
        return "0"