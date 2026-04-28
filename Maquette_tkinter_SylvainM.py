import tkinter as tk
from tkinter import PhotoImage, Label
import etat_de_jeu

selected_cell = None   # permet de savoir/stocker les cases selectionner
frame_chiffres = None # la ou les bouton en bas du sudoku sont stockée (en gros pour les manipuler , faire appelle a cette fonction)

def clear_window():    #permet la transition entre chaque fenêtre
    for widget in root.winfo_children():
        widget.destroy()

def diff_Facile():
    global diff 
    diff = "Facile"

def diff_Moyen():
    global diff 
    diff = "Moyen"

def diff_Difficile():
    global diff 
    diff = "Difficile"

def menu_difficulter():
    clear_window()
    fond()

    tk.Label(root, text="Choisir la difficulté", font=("Arial", 30, "bold")).pack(pady=50)

    #la  partie ajouter de la nouvelle version 

    tk.Button(root,text="Facile",font=("Arial", 18, "bold"),
              bg="#21F344",fg="white",
              command=lambda: lancer_sudoku(1)).pack(pady=10)

    tk.Button(root,text="Moyen",font=("Arial", 18, "bold"),
              bg="#F2FF00",fg="black",
              command=lambda: lancer_sudoku(2)).pack(pady=10)

    tk.Button(root,text="Difficile",font=("Arial", 18, "bold"),
              bg="#B70C0C",fg="white",
              command=lambda: lancer_sudoku(3)).pack(pady=10)

    tk.Button(root, text="Retour", command=menu_principal).pack(pady=20)


def afficher_sudoku(): # Affichage du sudoku (prototype, V2, avec les lignes)
    global selected_cell, frame_chiffres
    clear_window()

    
    taille_case = 60 
    canvas_size = taille_case * 9

    fond()

    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white", highlightthickness=0)  #canvas propre
    canvas.pack(pady=20)

    cases = {}  

    # on fait les ligne noirs que en verticale
    for i in range(10):
        epaisseur = 4 if i % 3 == 0 else 1  #lignes plus propres
        canvas.create_line(
            i * taille_case, 0,
            i * taille_case, 9 * taille_case,
            width=epaisseur,
            fill="black"
        )

    # cette foix on fait les horizontales
    for i in range(10):
        epaisseur = 4 if i % 3 == 0 else 1  
        canvas.create_line(
            0, i * taille_case,
            9 * taille_case, i * taille_case,
            width=epaisseur,
            fill="black"
        )

    # On affiche les boutons 1 a 9 seulement quand on clique sur une case
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
                relief="raised",
                bd=2,
                command=lambda v=i: choisir_chiffre(v)
            ).grid(row=0, column=i-1, padx=4, pady=4)

    
    def selection_case(row, col):
        global selected_cell

        case = cases[(row, col)]

        if case["text"] != "":  # on block l'acces a la case deja remplie
            return

        selected_cell = case
        afficher_chiffres()

    
    def choisir_chiffre(valeur):
        global selected_cell, frame_chiffres

        # ici je gère les cases avec lequelle on a deja interagie pour que l'utilisateur sache qu'il ne peux plus interagire avec
        if selected_cell and selected_cell["text"] == "":
            selected_cell.config(
                text=str(valeur),
                bg="#d3d3d3",   
                relief="sunken" 
            )
            
            # Sauvegarde dans la matrice, v = bouton_(entre 1 et 83). On cherche la valeur c de selected_cell
            for c, v in cases.items():
                if v == selected_cell:
                    etat_de_jeu.matrice[1][c[0]][c[1]] = valeur
            # On mets à jour etat_de_jeu.matrice[1] pour que ça soit à jour pour tous les autres fichiers

        selected_cell = None

        if frame_chiffres:
            frame_chiffres.destroy()
            frame_chiffres = None

    # on fait attention au plan a laquelle apparait les case ( sinon les lignes passent par dessus)+ création de la grille
    for row in range(9):
        for col in range(9):
            case = tk.Button(   # il s'agie d'un façon plus avancée du bouton que avant 
                root,
                text=etat_de_jeu.matrice[1][row][col],
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

            cases[(row, col)] = case  #on sauvegarde la case 

    
    bouton_retour = tk.Button(
        root,
        text="Retour au menu",
        font=("Arial", 14, "bold"),   
        bg="#4CAF50",
        fg="white",
        command=menu_principal
    )
    bouton_retour.pack(pady=10)

# affiche le menu principale (partiellement complet , manque bouton paramètre et peux être une interface plus styliser)
def menu_principal():
    clear_window()
    fond()
    titre = tk.Label(root, text="SUDOKU", font=("Arial", 40, "bold"))  # NOUVEAU : plus gros
    titre.pack(pady=50)

    #on a colorée les bouton affin que l'interface sois plus styliser , il manque encore le bouton parametre et l'arrière plan a faire

    tk.Button(root, text="Jouer", font=("Arial", 18, "bold"),
          bg="#2196F3", fg="white",  
          command=menu_difficulter).pack(pady=10)

    tk.Button(root,text="Charger",font=("Arial", 18, "bold"),
              bg="#16f154",fg="white").pack(pady=10)

    tk.Button(root, text="Quitter", font=("Arial", 18, "bold"),
              bg="#f44336", fg="white",  
              command=root.quit).pack(pady=10)
    
def lancer_sudoku(niveau):
    etat_de_jeu.creer_matrice(niveau)  #cette partie j'ai un doute car c'est avec ce que tu ma demandée
    afficher_sudoku()
    
# Eviter les répétitions   
def fond():
    global bg 
    bg = PhotoImage(file = "Medias/fond_1.png")
    label1 = Label(root, image = bg)
    label1.image = bg
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    label1.lower(belowThis=None) # Source https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/universal.html

def execution_graphique() :
    global root
    root = tk.Tk()
    root.title("Sudoku")
    root.geometry("1200x750") 

    menu_principal()
    root.mainloop()

