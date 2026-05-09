'''
2 options : 
- Aide normale: Révèle au hasard une case vide dans le sudoku 
- Aide puissante: Qui donne tous les emplacement d'un chiffre choisi par l'utilisateur
'''

import random
import etat_de_jeu 

#Aide normal: qui donne au hasard un nombre d'une case vide dans le sudoku 
def aide_normal():
    case_vide = []
    for i in range(9):
        for j in range(9):
            if etat_de_jeu.matrice[1][i][j] == "":
                case_vide.append((i,j))
    
    k = random.randint(0, len(case_vide) -1)
    i, j = case_vide[k]
    etat_de_jeu.matrice[1][i][j] = etat_de_jeu.matrice[0][i][j]


#Aide fort: qui donne tout les emplacements d'un chiffre demander dans la matrice
def aide_fort(nombre):
    for i in range(9):
        for j in range(9):
            if etat_de_jeu.matrice[0][i][j] == nombre:
                etat_de_jeu.matrice[1][i][j] = etat_de_jeu.matrice[0][i][j]
