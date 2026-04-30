'''
Ici, on créer une "IA" qui aide le joueur quand il en a besoin.
Si un nombre est trouvable de manière logique : On essaye de l'expliquer.

2 options : 
- Aide normal: qui donne au hasard un nombre d'une case vide dans le sudoku 
- Aide puissant: qui donne tout les emplacements d'un chiffre demander dans la matrice
'''

import random
# on utilise etat_de_jeu.matrice au lieu de main.matrice :
import etat_de_jeu 
print(etat_de_jeu.matrice)

def aide_normal(sudo):
    case_vide = []
    for i in range(9):
        for j in range(9):
            if sudo[1][i][j] == " ":
                case_vide.append(i,j)
    random.random(case_vide)
    sudo[1][i][j] = sudo[0][i][j]
                    
def aide_fort(sudo, nombre):
    for i in range(9):
        for j in range(9):
            if sudo[1][i][j] == nombre:
                sudo[1][i][j] = sudo[0][i][j]