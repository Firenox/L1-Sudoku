'''
Fenêtre du Sudoku
Code majoritairement fait par Sylvain
Code par Vahé: le fond, la sauvegarde et l'importation, et correction de codes pas vérifiés et non fonctionnels
'''

import time # Utilisé pour chronomètre, Source :https://docs.python.org/fr/3.8/library/time.html#time.time
import tkinter as tk
from tkinter import PhotoImage, Label

import etat_de_jeu
import aide_au_jeu
import sauvegardes

global heure_debut

compteur_aide = 0
cases = {}
solution = None
grille = None
selected_cell = None   # permet de savoir/stocker les cases selectionner
frame_chiffres = None # la ou les bouton en bas du sudoku sont stockée (en gros pour les manipuler , faire appelle a cette fonction)
temps = 0
fini = False
jeu_importe = None
case_probleme = None
case_bleu = None
diff = "Moyen"


def entre_valide(i, j, valeur):
    #3x3
    bloc_i = 3*(i//3)
    bloc_j = 3*(j// 3)
    for k in range(3):
        for l in range(3):
            if etat_de_jeu.matrice[1][bloc_i + k][bloc_j + l] == valeur:
                return ((bloc_i + k, bloc_j + l))
    
    #ligne
    for x in range(9):
        if valeur == etat_de_jeu.matrice[1][i][x]:
            return ((i,x))

    #colonne
    for y in range(9):
        if etat_de_jeu.matrice[1][y][j] == valeur:
            return ((y,j))
    
    return None


def clear_window():    #permet la transition entre chaque fenêtre
    for widget in root.winfo_children():
        widget.destroy()


def fond():
    global bg
    bg = PhotoImage(file="Medias/fond_1.png")

    # Seul moyen trouvé pour zoomer un peu dans Pillow
    bg = bg.zoom(6,6)
    bg = bg.subsample(5, 5) # Contraire du zoom
    label1 = Label(root, image=bg)
    label1.image = bg
    label1.place(x=-5, y=0) # Éviter bord blanc à gauche : x = -5
    label1.lower(belowThis=None) # Source https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html


def menu_principal():
    global fini
    fini = False
    clear_window()
    fond()

    titre = tk.Label(root, text="SUDOKU", font=("Arial", 40, "bold"))
    titre.pack(pady=50)

    tk.Button(root, text="Jouer", font=("Arial", 18, "bold"),
              bg="#2196F3", fg="white",
              command=menu_difficulter).pack(pady=10)

    tk.Button(root, text="Charger", font=("Arial", 18, "bold"),
              bg="#16f154", fg="white", command=importer_jeu).pack(pady=10)

    tk.Button(root, text="Quitter", font=("Arial", 18, "bold"),
              bg="#f44336", fg="white",
              command=root.quit).pack(pady=10)


def menu_difficulter():
    # On annule jeu_importee pour générer une nouvelle matrice
    global jeu_importe
    jeu_importe = None

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
    global solution, grille, diff, matrice_originale, heure_debut, nombre_erreur , compteur_aide, temps, jeu_importe, case_probleme, case_bleu

    case_probleme = None
    case_bleu = None

    if jeu_importe == None :
        etat_de_jeu.creer_matrice(niveau)
        nombre_erreur = 0
        compteur_aide = 0
        temps = 0
        matrice_originale = [v[:] for v in etat_de_jeu.matrice[1]] # Copie sans le problème avec la mémoire

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

    taille_case = 50
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
        global selected_cell, frame_chiffres, nombre_erreur, case_probleme, case_bleu
        if not selected_cell:
            return

        case, row, col = selected_cell

        # Coordonnées de la case qui cause l'erreur
        case_probleme = entre_valide(row, col, valeur) # Avant de rentrer la valeur dans le Sudoku juste en dessous

        case.config(text=str(valeur))
        grille[row][col] = valeur

        if diff == "Difficile":
            if not valeur_correcte(row, col, valeur):
                defaite()
                return

        if diff == "Facile":
            if valeur_correcte(row, col, valeur):
                case.config(bg="lightgreen")
            else:
                # Case qui causse l'erreur suite du code
                if case_bleu != None :
                    case_bleu.config(bg="white") # On enlève l'ancien bleu
                case_bleu = cases[case_probleme] # Entrée Valide renvoie un tuple (x, y)
                case_bleu.config(bg="lightblue") 

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

    tk.Label(
    root,
    text=f"Aides utilisées : {compteur_aide}",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="blue"
    ).pack()

    tk.Button(root, text="Retour menu", command=menu_principal).pack()
    
    tk.Button(
    root,
    text="Aide_normal",
    command=lambda: [
        utiliser_aide(),
        aide_au_jeu.aide_normal(),
        afficher_sudoku(),
        victoire() if grille_complete() and grille_correcte() else None
        ]
        ).pack()

    tk.Button(
    root,
    text="Aide_forte",
    command=ouvrir_aide_forte
    ).pack()

    save = tk.Button(root, text="Sauvegarder", command=sauvegarde_jeu)
    save.pack()

def utiliser_aide():
    global case_bleu, case_probleme
    case_bleu = None
    case_probleme = None
    global compteur_aide

    compteur_aide += 1

def ouvrir_aide_forte():
    global case_bleu, case_probleme
    case_bleu = None
    case_probleme = None
    
    fenetre = tk.Toplevel(root)
    fenetre.title("Choisir un chiffre")

    tk.Label(
        fenetre,
        text="Choisir un chiffre",
        font=("Arial", 18, "bold")
    ).pack()

    frame = tk.Frame(fenetre)
    frame.pack(pady=10)

    for i in range(1, 10):

        tk.Button(
            frame,
            text=str(i),
            font=("Arial", 16, "bold"),
            width=3,

            command=lambda v=i: choisir_aide_forte(v, fenetre)

        ).grid(row=0, column=i-1, padx=4)

def choisir_aide_forte(nombre, fenetre):

    utiliser_aide()

    aide_au_jeu.aide_fort(nombre)

    fenetre.destroy()

    afficher_sudoku()

    if grille_complete() and grille_correcte():
        victoire()

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
    global nombre_erreur, temps, compteur_aide, matrice_originale, fini
    if fini == False :
        temps += int(time.time() - heure_debut)
    sauvegardes.sauvegarder(nombre_erreur, compteur_aide, temps, matrice_originale, fini)

def importer_jeu():
    global jeu_importe, nombre_erreur, temps, compteur_aide, matrice_originale, fini, heure_debut
    jeu_importe = sauvegardes.ouvrir()

    if jeu_importe != None :
        etat_de_jeu.creer_matrice(1) # On crée le tuple matrice pour pouvoir le remplacer avec les lignes du dessous
        if jeu_importe[6] == True : # Si on a sauvegardé une matrice finie
            etat_de_jeu.matrice = (jeu_importe[0] , jeu_importe[5])

        else :                      # Sinon, on recommence et on créer un nouveau tuple
            etat_de_jeu.matrice = (jeu_importe[0] , jeu_importe[1]) # Le premier = matrice originale

        nombre_erreur = jeu_importe[2]
        compteur_aide = jeu_importe[3]
        temps = jeu_importe[4]
        matrice_originale = jeu_importe[5]
        fini = False

        lancer_sudoku(1)


def defaite():
    clear_window()
    fond()

    tk.Label(
        root,
        text="PERDU !",
        font=("Arial", 40, "bold"),
        fg="red"
    ).pack(pady=50)

    tk.Label(
        root,
        text="Vous avez fait une erreur en mode difficile",
        font=("Arial", 20)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Retour menu",
        command=menu_principal
    ).pack(pady=20)


def victoire():
    global heure_debut, temps, fini
    fini = True
    clear_window()
    fond()

    tk.Label(root, text="VICTOIRE !",
             font=("Arial", 40, "bold"),
             fg="green").pack(pady=50)

    temps += int(time.time() - heure_debut) # heure actuelle moins le début

    tk.Label(
    root,
    text=f"Temps passé : {temps//60} minute{'s' if temps//60 > 1 else ''} et {temps%60} seconde{'s' if temps%60 > 1 else ''}", # Source du if et else : https://www.datacamp.com/tutorial/python-f-string | Aussi très intuitif
    font=("Arial", 20, "bold"),
    fg="green"
    ).pack()

    tk.Label(root, text=f"Nombre d'erreurs : {nombre_erreur}",
             font=("Arial", 20, "bold"),
             fg="green").pack()


    tk.Label(root, text=f"Nombre d'aides utilisées : {compteur_aide}", font=("Arial", 20, "bold"), fg="green").pack()

    tk.Button(root, text="Sauvegarder le jeu",
              command=sauvegarde_jeu).pack(pady=20)

    tk.Button(root, text="Retour menu",
              command=menu_principal).pack(pady=20)


def execution_graphique():
    global root
    root = tk.Tk()
    root.title("Sudoku")
    root.geometry("1350x800")

    menu_principal()
    root.mainloop()