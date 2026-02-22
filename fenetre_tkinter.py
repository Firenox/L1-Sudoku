import tkinter as tk

racine = tk.Tk()
racine.title("Sudoku")
racine.geometry("1200x700")
racine.resizable(0, 0) # https://stackoverflow.com/questions/36575890/how-to-set-a-tkinter-window-to-a-constant-size

'''
Placer image avec PhotoImage pour permettre superposition
https://openclassrooms.com/forum/sujet/creation-plusieurs-images-dans-tkinter-1

Ajouter fond_id avant 'canvas.create_image(...)' pour pouvoir la supprimer
https://stackoverflow.com/questions/68121138/python-tkinter-canvas-delete

'''

canvas = tk.Canvas(racine, width=1200, height=700, bg="black")

fond = tk.PhotoImage(file='Medias/fond_1.png')
fond_id = canvas.create_image(0, 0, image=fond, anchor='nw')

def fond_supprimer():
    canvas.delete(fond_id)

def apparition_menu():      # Faire apparaître le menu après l'annimation de lancement
    # Texte, boutons...
    pass

def intencite():            # Source : Mon talent    # Lent et coûteux, doit être optimisé si problématique

    global l, logo, l_id    # Cours

    l, l_id = [], []

    for i in range(10):
        logo = tk.PhotoImage(file='Medias/SVB Plays_15prct.png') # Image avec 15% d'opacité
        logo = logo.subsample(2, 2)

        l.append(logo)
        l_id.append(canvas.create_image(300, 100, anchor="nw", image=l[i-1]))

        racine.update()

    racine.after(2000)

    for v in l_id:

        canvas.delete(v)
        racine.update()
        racine.after(30)
# Logo
# logo = tk.PhotoImage(file='Medias/SVB Plays_15prct.png')
# logo = logo.subsample(2, 2)
#canvas.create_image(300, 100, anchor="nw", image=logo) # Anchor >> _tkinter.TclError: bad anchor position "tkinter.NW": must be n, ne, e, se, s, sw, w, nw, or center

canvas.pack()
#racine.after(300,fond_supprimer)
racine.after(100,intencite)
racine.mainloop()