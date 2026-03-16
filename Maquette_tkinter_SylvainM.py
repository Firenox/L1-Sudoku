import tkinter as tk

def clear_window():             #permet la transition entre chaque fenêtre
    for widget in root.winfo_children():
        widget.destroy()

def afficher_sudoku(): #affichage du sudoku ( prototype)
    clear_window()

    frame = tk.Frame(root)
    frame.pack(pady=20)

    # création de la grille
    for row in range(9):
        for col in range(9):
            case = tk.Entry(
                frame,
                width=2,
                font=("Arial", 20),
                justify="center"
            )
            case.grid(row=row, column=col, padx=2, pady=2)

    # bouton retour menu
    bouton_retour = tk.Button(
        root,
        text="Retour au menu",
        font=("Arial", 12),
        command=menu_principal
    )
    bouton_retour.pack(pady=20)


def menu_principal(): #affiche le menu principale (complet a 50% , manque bouton paramètre et peux être une interface plus styliser)
    clear_window()

    titre = tk.Label(root, text="SUDOKU", font=("Arial", 30))
    titre.pack(pady=40)

    bouton_jouer = tk.Button(
        root,
        text="Jouer",
        font=("Arial", 15),
        width=10,
        command=afficher_sudoku
    )
    bouton_jouer.pack(pady=20)

    bouton_quitter = tk.Button(
        root,
        text="Quitter",
        font=("Arial", 15),
        width=10,
        command=root.quit
    )
    bouton_quitter.pack(pady=10)


root = tk.Tk()
root.title("Sudoku")
root.geometry("400x500")

menu_principal()

root.mainloop()