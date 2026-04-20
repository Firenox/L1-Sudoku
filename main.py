'''
Fichier principal reliant tous les autres fichiers.
Pour ouvrir le jeu, il faut lancer ce programme.
'''
import etat_de_jeu
import fenetre_tkinter

# Créer la matrice une seule fois
etat_de_jeu.creer_matrice(1)
fenetre_tkinter.lancer_fenetre_1()