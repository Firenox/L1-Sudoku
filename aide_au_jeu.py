# HEAD
#Ici, on créer une "IA" qui aide le joueur quand il en a besoin
#Si un nombre est trouvable de manière logique : On essaye de l'expliquer


"""
2 option : 
- un bouton aide avec lequel l'utilisateur interagie , il doit choisire une case avec lequelle il veut l'aide.
- si l'utilisateur c'est trompée : on lui indique l'erreur ,on compte ces erreurs ,et on choisie 1 case 
du bloc/colone/ligne de la case par lequelle on remplace par 1 des chiffres 

"""

'''
Ici, on créer une "IA" qui aide le joueur quand il en a besoin
Si un nombre est trouvable de manière logique : On essaye de l'expliquer
'''

import random
import main
main.matrice


def aide(sudo):
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