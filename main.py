import fenetre_tkinter
import generation_jeu
import sauvegardes
import conversion_matrice
import aide_au_jeu


nombre_de_parties_jouees = 0
meilleur_temps = 0.0

matrice1 = (generation_jeu.generer_grille())
matrice=[]
for i in range(3):
    for j in range(3):
        matrice.append(matrice1[i][j])
print(matrice)

fenetre_tkinter.lancer_fenetre_1()
