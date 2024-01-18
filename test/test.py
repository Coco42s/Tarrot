import time
a = []
b = []
c = []

carteDistri = [1,2,3,4,5,6,7,8,9,
               10,11,12,13,14,15,16,17,18,19,
               20,21,22,23,24,25,26,27,28,29,
               30,31,32,33,34,35,36,37,38,39,
               40,41,42,43,44,45,46,47,48,49,
               50,51,52,53,54,55,56,57,58,59,
               60,61,62,63,64,65,66,67,68,69,
               70,71,72,73,74,75,76,77,78]

ch = 6
n = 3
for i in range(1,int(((78-ch)/3)/3+1)):
    for i in range(n):
        a.append(carteDistri[0])
        b.append(carteDistri[1])
        c.append(carteDistri[i+2])
        carteDistri = carteDistri[3:]
        time.sleep(0.5)
        
print(a,len(a))
print(b,len(b))
print(c,len(c))

print(carteDistri)




C:\Users\coren\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\customtkinter\windows\widgets\core_widget_classes\ctk_base_class.py:179: UserWarning: CTkButton Warning: Given image is not CTkImage but <class 'PIL.ImageTk.PhotoImage'>. Image can not be scaled on HighDPI displays, use CTkImage instead.

  warnings.warn(f"{type(self).__name__} Warning: Given image is not CTkImage but {type(image)}. Image can not be scaled on HighDPI displays, use CTkImage instead.\n")
Connecting
Connect
b'\x80\x04\x95I\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8c,Hello Coco42s !\nVas Voir le chanel Serveur !\x94u.'
b'\x80\x04\x95Y\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04serv\x94\x8cKBienvenue, Coco42s!\nVous voulez jouer dans une partie a 3, 4 ou 5 joueur ?\n\x94s.'
b'\x80\x04\x95\x7f\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04serv\x94\x8cq\nVous avez \xc3\xa9t\xc3\xa9 mis en attent dans une partie a 3 joueur !\n\nLe tchat sera disponible une foix dans une partie !\n\x94s.'
b'\x80\x04\x95\x19\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8c\xfc[Tr\xc3\xa8fle 9, Tr\xc3\xa8fle 6, Pique 10, Tr\xc3\xa8fle 10, Carreau 1, Excuse 42, Coeur 9, Carreau 11, Carreau 3, Carreau 10, Coeur 5, Atout 20, Tr\xc3\xa8fle 1, Atout 2, Atout 4, Carreau 12, Atout 14, Carreau 2, Tr\xc3\xa8fle 14, Coeur 14, Pique 5, Pique 13, Atout 15, Atout 19]\x94u.'
b'\x80\x04\x95\x1d\x01\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03obj\x94\x8c\tcarteDist\x94\x8c\x04data\x94\x8c\xfc[Tr\xc3\xa8fle 9, Tr\xc3\xa8fle 6, Pique 10, Tr\xc3\xa8fle 10, Carreau 1, Excuse 42, Coeur 9, Carreau 11, Carreau 3, Carreau 10, Coeur 5, Atout 20, Tr\xc3\xa8fle 1, Atout 2, Atout 4, Carreau 12, Atout 14, Carreau 2, Tr\xc3\xa8fle 14, Coeur 14, Pique 5, Pique 13, Atout 15, Atout 19]\x94u.'
b'\x80\x04\x95!\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03obj\x94\x8c\x04cAct\x94\x8c\x04data\x94\x8c\x05False\x94u.'
<class 'bool'>
b'\x80\x04\x95\x91\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8ct\n0 : Passe\n1 : Petit\n2 : Garde\n3 : Garde Sans\n4 : Garde Contre\n\nVeuiller \xc3\xa9crire votre choix dans le chanel serveur\n\x94u.'
b'\x80\x04\x953\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8c\x16A Coco42s de choisire.\x94u.'
b'\x80\x04\x95"\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x04serv\x94\x8c\x14Vous avez choisie 1\n\x94s.'
b"\x80\x04\x95D\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8c'Le joueur Coco42s a choisi une Petit !\n\x94u."
b'\x80\x04\x958\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8c\x1bLe joueur Coco42s a pris !\n\x94u.'
b"\x80\x04\x95L\x02\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94X,\x02\x00\x00Le chien est : [Coeur 7, Tr\xc3\xa8fle 7, Carreau 4, Coeur 13, Atout 5, Coeur 6, Atout 9, Tr\xc3\xa8fle 8, Tr\xc3\xa8fle 13, Pique 7, Atout 8, Pique 1, Atout 21, Coeur 11, Carreau 6, Atout 18, Pique 11, Carreau 8, Atout 12, Tr\xc3\xa8fle 3, Atout 10, Pique 8, Carreau 7, Coeur 3, Coeur 10, Tr\xc3\xa8fle 5, Atout 3, Coeur 1, Atout 16, Coeur 2, Atout 13, Pique 14, Pique 4, Atout 17, Coeur 8, Pique 2, Pique 12, Atout 7, Tr\xc3\xa8fle 11, Coeur 12, Carreau 13, Atout 11, Tr\xc3\xa8fle 2, Atout 1, Carreau 14, Carreau 9, Pique 9, Pique 6, Atout 6, Coeur 4, Carreau 5, Tr\xc3\xa8fle 12, Tr\xc3\xa8fle 4, Pique 3]\n\x94u.\x80\x04\x95`\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08afficher\x94\x88\x8c\x06affich\x94\x8cCOn attent que le preneur fasse sont chien dans le chanel serveur !\n\x94u.\x80\x04\x95E\x01\x00\x00\x00\x00\x00\x00}\x94\x8c\x04serv\x94X4\x01\x00\x00Veuiler rentr\xc3\xa9 les carte choisie pour le chien une a une sour le forma 'couleur + valeur' Exemple : 'Excuse 42'\n(ne pas m\xc3\xa8tre les '')\nLes couleur possible sont (Pique,Tr\xc3\xa8fle,Coeur,Carreau,Atout,Excuse)\n Les valeur vont de 1 a 14 pour les carte ordinaire pour les atout sa vas de 1 a 21 et l"
b"'excuse sais 42\x94s."