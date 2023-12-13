import tkinter as tk
from PIL import Image, ImageTk

class RotatingCanvasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rotating Canvas")

        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()

        # Charger une image
        image = Image.open("C:\Users\coren\Documents\GitHub\Tarrot\Clients\assets\cartespetit.jpg")
        self.original_image = ImageTk.PhotoImage(image)

        # Afficher l'image sur le canvas
        self.image_item = self.canvas.create_image(150, 150, image=self.original_image)

        # Ajouter un bouton pour déclencher la rotation
        rotate_button = tk.Button(self.master, text="Rotation", command=self.rotate_image)
        rotate_button.pack()

    def rotate_image(self):
        # Appliquer une rotation de 45 degrés à l'image sur le canvas
        self.canvas.rotate(self.image_item, 45)

if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingCanvasApp(root)
    root.mainloop()
