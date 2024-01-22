from Class.Paquet import *

pac = Paquet()
pac.fabriques() 
carte = pac.get_jeu()

print(carte)
print("\n\n")
print(carte[0],type(carte[0]))