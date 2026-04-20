'''
Fichier principal reliant tous les autres fichiers.
Pour ouvrir le jeu, il faut lancer ce programme.
'''

import fenetre_tkinter
import sauvegardes
import aide_au_jeu
import generation_jeu_vide

nombre_de_parties_jouees = 0
meilleur_temps = 0.0

matrice=(generation_jeu_vide.matrice())

def executer():
    fenetre_tkinter.lancer_fenetre_1()