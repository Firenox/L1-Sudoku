import tkinter as tk

couleur_fond = "black"
couleur_text = "green"
counter = 0


def affichage():
    global counter
    counter += 1
    label1.config(text="Cookie Clicker : " + str(counter))


racine = tk.Tk()
racine.title("Sudoku")

#Texte : Titre
label = tk.Label(racine, bg=couleur_fond, fg = couleur_text, text = "Un texte", font=("Helvetica", "28"), padx = 20, pady = 20, borderwidth= 5, relief= "groove")
label.grid(column=0, row=0)

#Text : Cookie Clicker counter afficher
label1 = tk.Label(racine, bg=couleur_fond, fg = couleur_text, text = "Cookie Clicker", font=("Helvetica", "28"), padx = 20, pady = 20)
label1.grid(column=0, row=1)

#Bouton : Cookie Clicker counter +1
bouton = tk.Button(racine, text="Button", command = affichage, font = ("helvetica", "28"))
bouton.grid(row=2, column=0)

#Dessin : Rectangle
canvas = tk.Canvas(racine, bg = "#6D9BB6", height=500, width=500)
canvas.grid()

#Dessin : Trait
canvas.create_line((0,0), (200, 200), (200, 0), fill="blue", width = 5)
canvas.grid()


racine.mainloop()