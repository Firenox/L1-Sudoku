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

#Aide normal: qui donne au hasard un nombre d'une case vide dans le sudoku 
def aide_normal():
    case_vide = []
    for i in range(9):
        for j in range(9):
            if etat_de_jeu.matrice[1][i][j] == "":
                case_vide.append((i,j))
    
    i = random.randint(0, len(case_vide) -1)
    print(case_vide)
    etat_de_jeu.matrice[1][case_vide[i][0]][case_vide[i][1]] == etat_de_jeu.matrice[0][case_vide[i][0]][case_vide[i][1]]
    
    etat_de_jeu.matrice[1][i][j] = etat_de_jeu.matrice[0][i][j]


#Aide fort: qui donne tout les emplacements d'un chiffre demander dans la matrice
def aide_fort():
    nombre = random.randint(1, 9)
    print(nombre)
    for i in range(9):
        for j in range(9):
            if etat_de_jeu.matrice[0][i][j] == nombre:
                etat_de_jeu.matrice[1][i][j] = etat_de_jeu.matrice[0][i][j]
