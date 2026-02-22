import tkinter as tk
import os
import winsound

def play_sound():
    winsound.PlaySound(os.path.join("Medias\son.wav"), winsound.SND_ASYNC)

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

# Objectif | Faire apparaître le menu après l'annimation de lancement
def apparition_menu():
    # Texte, boutons...
    pass

# Objectif | Ouverture programme : Annimation introduction
# Solution la plus facile mais sûrement pas la meilleure
def intencite():            # Source : Mon talent

    global listes, listes_id, logo  # Cours 
    play_sound()
    racine.after(150)

    # Des listes de listes
    listes=[[None]*15 for i in range(4)]
    listes_id=[[None]*15 for i in range(4)]

    # Sorti de la boucle = infiniment plus rapide
    logo_S = tk.PhotoImage(file='Medias\Logo par lettres\SVB Plays 10prct - S.png') # le S du logo avec 10% d'opacité
    logo_V = tk.PhotoImage(file='Medias\Logo par lettres\SVB Plays 10prct - V.png') # le V du logo avec 10% d'opacité
    logo_B = tk.PhotoImage(file='Medias\Logo par lettres\SVB Plays 10prct - B.png') # le B du logo avec 10% d'opacité
    logo_Plays = tk.PhotoImage(file='Medias\Logo par lettres\SVB Plays 10prct - Plays.png') # le Plays du logo avec 10% d'opacité

    logo_S, logo_V, logo_B, logo_Plays = logo_S.subsample(2, 2), logo_V.subsample(2, 2), logo_B.subsample(2, 2), logo_Plays.subsample(2, 2)

    for i in range(15):

        listes[0][i]= logo_S
        listes_id[0][i]=(canvas.create_image(350, 100, anchor="nw", image=listes[0][i-1]))

        racine.update()
        racine.after(20)

    racine.after(600)

    for i in range(15):

        listes[1][i]= logo_V
        listes_id[1][i]=(canvas.create_image(350, 100, anchor="nw", image=listes[1][i-1]))

        racine.update()
        racine.after(20)

    racine.after(500)

    for i in range(15):

        listes[2][i]=(logo_B)
        listes_id[2][i]=(canvas.create_image(350, 100, anchor="nw", image=listes[2][i-1]))

        racine.update()
        racine.after(20)

    racine.after(400)

    for i in range(15):

        listes[3][i]=(logo_Plays)
        listes_id[3][i]=(canvas.create_image(350, 100, anchor="nw", image=listes[3][i-1]))

        racine.update()
        racine.after(20)

    racine.after(300)

    # Disparition progressive des lettres
    for i in  range(len(listes[0])):
        for j in range(4):
            canvas.delete(listes_id[j][i])

        racine.update()
        racine.after(30)

    # Logo définitif ( ?? )
    logo = tk.PhotoImage(file='Medias/SVB Plays.png')
    logo = logo.subsample(12, 12)
    canvas.create_image(1100, 0, anchor="nw", image=logo) # Anchor >> _tkinter.TclError: bad anchor position "tkinter.NW": must be n, ne, e, se, s, sw, w, nw, or center

canvas.pack()
racine.after(100,intencite)
racine.mainloop()