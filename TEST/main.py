import tkinter as tk
import tkinter as tk
from tkinter import *

fenetre = tk.Tk()
fenetre.title('Mon Joker')
largeur = 350
hauteur = 350
zone_graphique = tk.Canvas(fenetre, width=largeur, height=hauteur, bg='white')
zone_graphique.pack(padx=50, pady=50)
x = 130
y = 100
r = 20


zone_graphique.create_rectangle(
    x-r, y-r, x+r, y+r, outline='black', fill='green')

x = 230
y = 100
r = 20


zone_graphique.create_rectangle(
    x-r, y-r, x+r, y+r, outline='black', fill='green')
zone_graphique.create_oval(160, 190, 200, 150, outline='black', fill='red')
zone_graphique.create_line(125, 200, 185, 250, 245,
                           200, 185, 280, 125, 200, fill='red')
zone_graphique.grid()
fenetre.mainloop()

# sous form de classe


class application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        largeur = 350
        hauteur = 350
        zone_graphique = tk.Canvas(
            self, width=largeur, height=hauteur, bg='white')
        zone_graphique.pack(padx=50, pady=50)

        self.canvas = zone_graphique
        self.creer_kiri()


def creer_kiri(self):

    x = 130
    y = 100
    r = 20

    self.canvas.create_rectangle(
        x-r, y-r, x+r, y+r, outline='black', fill='green')

    x = 230
    y = 100
    r = 20

    self.canvas.create_rectangle(
        x-r, y-r, x+r, y+r, outline='black', fill='green')
    self.canvas.create_oval(160, 190, 200, 150, outline='black', fill='red')
    self.canvas.create_line(125, 200, 185, 250, 245, 200,
                            185, 280, 125, 200, fill='red')
    self.canvas.pack()


app = application()
app.title("monjoker")
app.mainloop()
