'''
Fichier principal reliant tous les autres fichiers.
Pour ouvrir le jeu, il faut lancer ce programme.
'''

import fenetre_tkinter
import sauvegardes
import conversion_matrice
import aide_au_jeu
import generation_jeu


nombre_de_parties_jouees = 0
meilleur_temps = 0.0

matrice1 = (generation_jeu.generer_grille())
matrice=[matrice1[i][j] for i in range(3) for j in range(3)]
print(matrice)

fenetre_tkinter.lancer_fenetre_1()
