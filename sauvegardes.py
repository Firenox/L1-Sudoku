'''
Ce fichier permet de Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue
'''
import json
import etat_de_jeu

def sauvegarder(nombre_erreur, compteur_aide, temps, matrice_originale, fini):
    sauvegarde = open("sauvegarde.json", "w")
    matrice = etat_de_jeu.matrice

    # Si le jeu est terminée, on enregistre la matrice au début et les compteurs à 0
    if fini == False :
        donnees = [matrice[0], matrice[1], nombre_erreur, compteur_aide, temps, matrice_originale, False]
    
    else :
        donnees = [matrice[0], matrice_originale, 0,  0, 0, matrice_originale, True, nombre_erreur, compteur_aide, temps]
        
    json.dump(donnees, sauvegarde)
    sauvegarde.close()


def ouvrir(): # On a vu comment sauvegarder mais pas comment lire. Source : https://www.geeksforgeeks.org/python/json-load-in-python/
    # Try et Except essentiels pour pas d'erreur si vide, Source : https://www.docstring.fr/formations/faq/resolution-derreurs/que-signifie-une-erreur-de-type-filenotfounderror/
    try :
        sauvegarde = open("sauvegarde.json", "r")
    except FileNotFoundError :
        return None

    save = json.load(sauvegarde)
    sauvegarde.close()
    return save