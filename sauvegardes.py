'''
Ce fichier permet de Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue
'''
import etat_de_jeu

def sauvegarder(nombre_erreur, compteur_aide, temps, matrice_originale, fini):
    sauvegarde = open("sauvegarde.txt", "w")
    matrice = etat_de_jeu.matrice


    if fini == False :
        donnees = [matrice[0], matrice[1], nombre_erreur, compteur_aide, temps, fini]
    
    else :
        donnees = [matrice_originale, matrice[1], nombre_erreur,  compteur_aide, temps, fini]
        
    sauvegarde.write(str(donnees))
    sauvegarde.close()

def ouvrir():
    sauvegarde = open("sauvegarde.txt", "r")
    save = sauvegarde.readline()

    sauvegarde.close()
    return save