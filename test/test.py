import tkinter as tk

def on_canvas_click(canvas_id):
    print(f"Canvas {canvas_id} clicked!")

def main():
    root = tk.Tk()
    root.title("Superposer deux Canvas")

    # Premier Canvas
    canvas1 = tk.Canvas(root, width=200, height=200, bg='blue')
    canvas1.pack()

    # Deuxième Canvas
    canvas2 = tk.Canvas(root, width=150, height=150, bg='red')
    canvas2.pack()

    # Superposer le deuxième Canvas sur le premier
    canvas2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Lier la fonction on_canvas_click à l'événement de clic sur les deux canvas
    canvas1.bind("<Button-1>", lambda event: on_canvas_click(1))
    canvas2.bind("<Button-1>", lambda event: on_canvas_click(2))

    root.mainloop()

if __name__ == "__main__":
    main()
