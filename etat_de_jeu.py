"""
Fichier qui stocke la matrice.
Elle est créée une seule fois et tous les fichiers peuvent l'ouvrir.
"""

import generation_jeu_vide

def creer_matrice(niveau):
    global matrice
    matrice = generation_jeu_vide.matrice(niveau)
    # Dans l'ordre : nombre d'erreurs, score, difficultee
    donnes_jeu = [0, 0]
