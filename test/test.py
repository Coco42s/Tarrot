import tkinter as tk

def on_enter_pressed(event):
    # Cette fonction sera appelée lorsque la touche Entrée est pressée
    value = entry.get()
    label.config(text=f"Vous avez appuyé sur Entrée avec la valeur : {value}")
    # Supprimer le contenu de l'Entry après traitement
    entry.delete(0, 'end')

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter")

# Création d'un widget Entry
entry = tk.Entry(root)
entry.pack(pady=10)

# Création d'une étiquette pour afficher le résultat
label = tk.Label(root, text="")
label.pack()

# Liaison de la fonction on_enter_pressed à l'événement 'KeyPress' pour la touche Entrée
entry.bind("<Return>", on_enter_pressed)

# Exécution de la boucle principale
root.mainloop()
