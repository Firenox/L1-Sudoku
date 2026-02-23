"""
Les fonctions ci dessous permettent de convertir les actions de l'interface graphique à la matrice générée
"""

def x_y_valeur(x,y): #On relie des coordonées à la bonne valeure dans la liste
    return l[x*y]

def x_y_to_valeur(x,y,valeur): #On relie des coordonées à la bonne valeure dans la liste
    l[x*y] = valeur