# Objectif | Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue si l’usager le souhaite.
# Solution | Générer un fichier txt avec les données dedans.

# Essai
import time
def sauvegarder(matrice, donnes_jeu):
    sauvegarde = open("sauvegarde.txt", "w")

    # time.time() = Heure en bits toujours unique. Int pour garder jusqu'aux secondes
    sauvegarde.write("\n" + [matrice[0], matrice[1], donnes_jeu[0], donnes_jeu[1], donnes_jeu[2]])
    sauvegarde.close()

def ouvrir():
    sauvegarde = open("sauvegarde.txt", "w")
    liste = []

    line = sauvegarde.readline()

    while line != "":
        liste += line
        line = sauvegarde.readline()

    return liste