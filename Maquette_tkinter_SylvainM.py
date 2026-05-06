'''
Fenêtre du Sudoku
'''

import time # Source :https://docs.python.org/fr/3.8/library/time.html#time.time
global heure_debut

import tkinter as tk
from tkinter import PhotoImage, Label
import etat_de_jeu

cases = {}
solution = None
grille = None
selected_cell = None   # permet de savoir/stocker les cases selectionner
frame_chiffres = None # la ou les bouton en bas du sudoku sont stockée (en gros pour les manipuler , faire appelle a cette fonction)

diff = "Moyen"


def clear_window():    #permet la transition entre chaque fenêtre
    for widget in root.winfo_children():
        widget.destroy()


def fond():
    global bg 
    bg = PhotoImage(file="Medias/fond_1.png")
    label1 = Label(root, image=bg)
    label1.image = bg
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    label1.lower(belowThis=None) # Source https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html


def menu_principal():
    clear_window()
    fond()

    titre = tk.Label(root, text="SUDOKU", font=("Arial", 40, "bold"))
    titre.pack(pady=50)

    tk.Button(root, text="Jouer", font=("Arial", 18, "bold"),
              bg="#2196F3", fg="white",
              command=menu_difficulter).pack(pady=10)

    tk.Button(root, text="Charger", font=("Arial", 18, "bold"),
              bg="#16f154", fg="white").pack(pady=10)

    tk.Button(root, text="Quitter", font=("Arial", 18, "bold"),
              bg="#f44336", fg="white",
              command=root.quit).pack(pady=10)


def menu_difficulter():
    clear_window()
    fond()

    tk.Label(root, text="Choisir la difficulté",
             font=("Arial", 30, "bold")).pack(pady=50)

    tk.Button(root, text="Facile", font=("Arial", 18, "bold"),
              bg="#21F344", fg="white",
              command=lambda: lancer_sudoku(1)).pack(pady=10)

    tk.Button(root, text="Moyen", font=("Arial", 18, "bold"),
              bg="#F2FF00", fg="black",
              command=lambda: lancer_sudoku(2)).pack(pady=10)

    tk.Button(root, text="Difficile", font=("Arial", 18, "bold"),
              bg="#B70C0C", fg="white",
              command=lambda: lancer_sudoku(3)).pack(pady=10)

    tk.Button(root, text="Retour", command=menu_principal).pack(pady=20)


def lancer_sudoku(niveau):
    global solution, grille, diff, matrice_originale, heure_debut, nombre_erreur

    etat_de_jeu.creer_matrice(niveau)
    nombre_erreur = 0

    matrice_originale = etat_de_jeu.matrice[1]
    solution = etat_de_jeu.matrice[0]
    grille = etat_de_jeu.matrice[1]

    heure_debut = time.time()

    if niveau == 1:
        diff = "Facile"
    elif niveau == 2:
        diff = "Moyen"
    else:
        diff = "Difficile"

    afficher_sudoku()


def afficher_sudoku():
    global selected_cell, frame_chiffres, cases

    clear_window()

    taille_case = 60
    canvas_size = taille_case * 9

    fond()

    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size,
                       bg="white", highlightthickness=0)
    canvas.pack(pady=20)

    cases = {}

    for i in range(10):
        epaisseur = 4 if i % 3 == 0 else 1
        canvas.create_line(i * taille_case, 0,
                           i * taille_case, canvas_size,
                           width=epaisseur, fill="black")

    for i in range(10):
        epaisseur = 4 if i % 3 == 0 else 1
        canvas.create_line(0, i * taille_case,
                           canvas_size, i * taille_case,
                           width=epaisseur, fill="black")


    def afficher_chiffres():
        global frame_chiffres

        if frame_chiffres:
            frame_chiffres.destroy()

        frame_chiffres = tk.Frame(root, bg="#f0f0f0")
        frame_chiffres.pack(pady=10)
        for i in range(1, 10):
            tk.Button(
                frame_chiffres,
                text=str(i),
                font=("Arial", 16, "bold"),
                width=3,
                bg="white",
                command=lambda v=i: choisir_chiffre(v)
            ).grid(row=0, column=i-1, padx=4)


    def selection_case(row, col):
        global selected_cell

        case = cases[(row, col)]

        if diff == "Difficile":
            if case["text"] != "":
                return

        selected_cell = (case, row, col)
        afficher_chiffres()


    def choisir_chiffre(valeur):
        global selected_cell, frame_chiffres, nombre_erreur

        if not selected_cell:
            return

        case, row, col = selected_cell

        case.config(text=str(valeur))
        grille[row][col] = valeur

        if diff == "Facile":
            if valeur_correcte(row, col, valeur):
                case.config(bg="lightgreen")
            else:
                case.config(bg="red")
                nombre_erreur += 1

        elif diff == "Moyen":
            case.config(bg="white")

        if grille_complete():
            if grille_correcte():
                victoire()

        selected_cell = None

        if frame_chiffres:
            frame_chiffres.destroy()
            frame_chiffres = None


    for row in range(9):
        for col in range(9):
            case = tk.Button(
                root,
                text=grille[row][col],
                font=("Arial", 18, "bold"),
                width=2,
                height=1,
                bg="white",
                relief="flat",
                bd=0,
                command=lambda r=row, c=col: selection_case(r, c)
            )

            canvas.create_window(
                col * taille_case + taille_case // 2,
                row * taille_case + taille_case // 2,
                window=case
            )

            cases[(row, col)] = case


    tk.Button(root, text="Retour menu",
              command=menu_principal).pack(pady=10)


def grille_complete():
    for i in range(9):
        for j in range(9):
            if grille[i][j] in ("", 0, None):
                return False
    return True


def grille_correcte():
    for i in range(9):
        for j in range(9):
            if grille[i][j] != solution[i][j]:
                return False
    return True


def valeur_correcte(row, col, valeur):
    return valeur == solution[row][col]


def sauvegarde_jeu():
    global nombre_erreur, temps
    pass


def victoire():
    global heure_debut, temps

    clear_window()
    fond()

    tk.Label(root, text="VICTOIRE !",
             font=("Arial", 40, "bold"),
             fg="green").pack(pady=50)

    temps = int(time.time() - heure_debut) # heure actuelle moins le début

    tk.Label(root, text=f"Temps passé : {temps//60} minute{"s" if temps//60 > 1 else ''} et {temps%59} seconde{"s" if temps%59 > 1 else ""}", # Source du if et else : https://www.datacamp.com/tutorial/python-f-string | Aussi très intuitif
             font=("Arial", 20, "bold"),
             fg="green").pack()

    tk.Label(root, text=f"Nombre d'erreurs : {nombre_erreur}",
             font=("Arial", 20, "bold"),
             fg="green").pack()

    tk.Button(root, text="Sauvegarder le jeu",
              command=sauvegarde_jeu).pack(pady=20)

    tk.Button(root, text="Retour menu",
              command=menu_principal).pack(pady=20)


def execution_graphique():
    global root
    root = tk.Tk()
    root.title("Sudoku")
    root.geometry("1200x750")

    menu_principal()
    root.mainloop()