'''
Le programme ci dessou permet de générer la matrice du sudoku remplie et valide,
à partir de la matrice de generation_jeu.py.
'''
from random import randint
def matrice_jeu(matrice, niveau):
    matrice2 = [v[:] for v in matrice]
    if niveau == 1:
        n = 40
    if niveau == 2:
        n = 35
    if niveau == 3:
        n = 30

    i = 0
    while i != n:
        a, b = randint(0,8), randint(0,8)
        if matrice2[a][b] != "":
            matrice2[a][b] = ""
            i+=1

        
#matrice_jeu([[4],[3]], "simple")
