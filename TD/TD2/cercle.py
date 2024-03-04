import tkinter as tk

fenetre = tk.Tk
fenetre.geometry("300x300")
fenetre.title("La Cible")

canvas = tk.Canvas(fenetre,width=300, height=300, bg= 'black')
button_quitter = tk.Button(fenetre, text='quitter', command=lambda:fenetre.destroy())

couleur = ['blue', 'green', 'black', 'yellow', 'magenta', 'red']


x1=5
y1=5
x2=295
y2=295

def Cible():
    canvas.create_oval(x1, y1, x2, y2, width=5, outline='blue')

fenetre.mainloop()