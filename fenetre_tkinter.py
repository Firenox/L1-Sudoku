'''
Placer image avec PhotoImage pour permettre superposition
https://openclassrooms.com/forum/sujet/creation-plusieurs-images-dans-tkinter-1
 
Enregistrer dans une variable 'canvas.create_image(...)' ou 'bouton_jouer.place(x=500, y=300)' pour pouvoir la supprimer avec canvas.delete(la variable)
https://stackoverflow.com/questions/68121138/python-tkinter-canvas-delete

Réduire taille image
https://stackoverflow.com/questions/3177969/how-to-resize-an-image-using-tkinter

On utilise .place pour mettre des widgets les uns sur les autres
'''


import tkinter as tk

racine = tk.Tk()
racine.title("Sudoku")
racine.geometry("1200x700")


canvas = tk.Canvas(racine, width=1200, height=700, bg="black")
fond = tk.PhotoImage(file="Medias/fond_1.png")
fond_id = canvas.create_image(0, 0, image=fond, anchor='nw')


def fond_supprimer():
    canvas.delete(fond_id)

# À CORRIGER
def apparition_menu_choix():
    print("ça marche :)")
    canvas.delete(bouton_jouer_id)
    canvas.update()

# Objectif | Faire apparaître le menu après l'annimation de lancement
def apparition_menu1():
    global logo, bouton_jouer_id

    # Logo en haut à droite
    logo = tk.PhotoImage(file='Medias/SVB Plays.png')
    logo = logo.subsample(12, 12)
    canvas.create_image(1100, 0, anchor="nw", image=logo) #Anchor >> _tkinter.TclError: bad anchor position "tkinter.NW": must be n, ne, e, se, s, sw, w, nw, or center
    
    # Texte d'essai
    titre = tk.Label(racine, bg="Green", text = "Sudoku",  font=("Helvetica", "50"))
    titre.place(x=480, y=50)

    # Bouton d'essai
    bouton_jouer = tk.Button(racine, bg="Green", text = "Jouer", font=("Helvetica", "20"), command=apparition_menu_choix)
    bouton_jouer_id = bouton_jouer.place(x=500, y=300)


# En lien avec la fonction animation_logo_ouverture
# Faire apparaître 15 fois l'image avec 10% d'opcaité pour faire un fondu
def apparition_15x(image):
    id_image = []
    for i in range(15):
        id_image.append(canvas.create_image(350,100,anchor="nw",image=image))
        racine.update()
        racine.after(20)
    return id_image


# Objectif | Ouverture programme : Annimation introduction
# Solution la plus facile mais sûrement pas la meilleure :
# Chaque lettres sont à 10% d'opcacité, on en fait apparaître 15 à la suite pour faire un fondu
# Le jeu n'est pas impacté par cette fonction, on peut donc la retirer à tout moment
def animation_logo_ouverture():
    global listes_id # Obligatoire pour faire apparaître le logo
    racine.after(150)

    # Images S, V, B et Plays à 10% d'opcacité
    logo_S = tk.PhotoImage(file='Medias/Logo par lettres/SVB Plays 10prct - S.png')
    logo_V = tk.PhotoImage(file='Medias/Logo par lettres/SVB Plays 10prct - V.png')
    logo_B = tk.PhotoImage(file='Medias/Logo par lettres/SVB Plays 10prct - B.png')
    logo_Plays = tk.PhotoImage(file='Medias/Logo par lettres/SVB Plays 10prct - Plays.png')

    logo_S, logo_V, logo_B, logo_Plays = logo_S.subsample(2, 2), logo_V.subsample(2, 2), logo_B.subsample(2, 2), logo_Plays.subsample(2, 2)

    listes_id = [apparition_15x(logo_S), apparition_15x(logo_V), apparition_15x(logo_B), apparition_15x(logo_Plays)]

    # Disparition progressive des lettres
    racine.after(150)
    for i in  range(len(listes_id[0])):
        for j in range(4):
            canvas.delete(listes_id[j][i])

        racine.update()
        racine.after(30)

    racine.after(100,apparition_menu1)

canvas.pack()
racine.after(100,animation_logo_ouverture)
racine.mainloop()