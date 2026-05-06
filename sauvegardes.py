'''
Ce fichier permet de Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue
'''

def sauvegarder(matrice, donnes_jeu):
    sauvegarde = open("sauvegarde.txt", "w")

    # time.time() = Heure en bits toujours unique. Int pour garder jusqu'aux secondes
    donnees = [matrice[0], matrice[1], donnes_jeu[0], donnes_jeu[1], donnes_jeu[2]]
    sauvegarde.write("\n" + str(donnees))
    sauvegarde.close()

def ouvrir():
    sauvegarde = open("sauvegarde.txt", "r")
    liste = []

    line = sauvegarde.readline()

    while line != "":
        liste += line
        line = sauvegarde.readline()

    return liste