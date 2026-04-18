'''
Les fonctions ci dessous permettent de convertir les actions de l'interface graphique à la matrice générée.
'''

def x_y_valeur(x,y, matrice): #On relie des coordonées à la bonne valeure dans la liste
    return matrice[3*(y//3)+(x//3)][3*(y%3)+(x%3)]

def x_y_to_valeur(x,y,valeur, matrice): #On place la valeur dans la liste
    matrice[3*(y//3)+(y//3)][3*(y%3)+(x%3)] = valeur