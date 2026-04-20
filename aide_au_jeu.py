# HEAD
#Ici, on créer une "IA" qui aide le joueur quand il en a besoin
#Si un nombre est trouvable de manière logique : On essaye de l'expliquer


"""
2 option : 
- Un bouton aide avec lequel l'utilisateur interagie, il doit choisir une case avec laquelle il veut l'aide.
- Si l'utilisateur s'est trompé : on lui indique l'erreur, on compte ces erreurs, et on choisi une case
du bloc/colone/ligne de la case par laquelle on remplace par un des nombres 

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