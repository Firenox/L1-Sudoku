'''
Le programme ci dessou permet de générer la matrice du sudoku remplie et valide,
à partir de la matrice de generation_jeu.py.
'''
import generation_jeu
from random import randint


def matrice_jeu(matrice, niveau):
    matrice2 = [v[:] for v in matrice]
    if niveau == 1:
        n = 35
    if niveau == 2:
        n = 30
    if niveau == 3:
        n = 25

    i = 0
    while i != n:
        a, b = randint(0,8), randint(0,8)
        if matrice2[a][b] != "":
            temporaire = matrice2[a][b]
            matrice2[a][b] = ""
            if matrice_valide(matrice2) == False:
                matrice2[a][b] = temporaire
            else :
                i+=1
    return matrice2

'''
Avant de supprimer une valeur avec matrice_jeu(), il faut vérifier que le Sudoku
est toujours faisable et qu'il y a uniquement une seule solution,
pour ne pas avoir de fausses mauvaisses réponses.

A FINIR
'''

# Cette fonction vérifie que la case 
def entre_valide(matrice, i, j, valeur):
    #3x3
    bloc_i = 3*(i//3)
    bloc_j = 3*(j// 3)
    for k in range(3):
        for l in range(3):
            if matrice[bloc_i + k][bloc_j + l] == valeur:
                return False
    
    #colonne
    if valeur in matrice[i]:
        return False

    #ligne
    for y in range(9):
        if matrice[y][j] == valeur:
            return False
    
    return True


# Cette fonction est importante pour compter le nombre de solutions possibles
def matrice_valide(matrice):
    compteur = 0
    matrice3 = [v[:] for v in matrice]
    for i in range(9):
        for j in range(9):
            if matrice3[i][j] == "":
                valeur = 0
                while entre_valide(matrice3, i ,j, valeur) == False and valeur < 9:
                    valeur += 1
                if valeur > 8 :
                    return False
                
    return True


def x_y_to_valeur(x,y,valeur, matrice): #On place la valeur dans la liste
    matrice[3*(y//3)+(x//3)][3*(y%3)+(x%3)] = valeur

def matrice():
    matrice_temp1 = (generation_jeu.generer_grille())
    # On passe en une liste de sous listes # Note : essayer de faire sans
    matrice_temp2=[matrice_temp1[i][j] for i in range(3) for j in range(3)]
    # On pace en listes de sous listes mais dans un ordre plus simple avec (x, y)
    matrice = [['']*9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            x_y_to_valeur(j, i, matrice_temp2[i][j], matrice)
    return((matrice,matrice_jeu(matrice, 1)))