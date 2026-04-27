"""
Fichier qui stocke la matrice.
Elle est créée une seule fois et tous les fichiers peuvent l'ouvrir.
"""

import generation_jeu_vide

def creer_matrice(niveau):
    global matrice, donnes_jeu
    # Tuple : (matrice remplie, matrice à moitié vide qui se remplie pendant le jeu)
    matrice = generation_jeu_vide.matrice(niveau)

    # Dans l'ordre : nombre d'erreurs, score, difficultee
    donnes_jeu = [0, 0, None]