import tkinter as tk

fenetre = tk.Tk ()

def Oval():
    canvas.create_oval(10, 10, 100, 100, outline='blue')

def Carre():
    canvas.create_rectangle(100, 100, 10, 10, outline="red")

def Croix():
    canvas.create_line((10, 100), (100, 10), fill='yellow')
    canvas.create_line((100, 100), (10, 10), fill= 'yellow')


fenetre.title("Mon dessin")

canvas = tk.Canvas(fenetre,width=300, height=300, bg= 'black')
button_couleur= tk.Button(fenetre,text="Choisir une couleur", bg='salmon')
button_cercle = tk.Button(fenetre, text="Cercle", bg='yellow', command=Oval)
button_carre = tk.Button(fenetre, text="Carré", bg='DarkSeaGreen1', command=Carre)
button_croix = tk.Button(fenetre, text="Croix", bg='cyan', command=Croix)



canvas.grid(row=1, column=1, rowspan=4, columnspan=1)
button_couleur.grid(row=0,column=1)
button_cercle.grid(row=1, column=0)
button_carre.grid(row=2,column=0)
button_croix.grid(row=3,column=0)


fenetre.mainloop()