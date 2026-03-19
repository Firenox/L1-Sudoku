# Objectif | Sauvegarder l’état de jeu d’une grille et refaire une grille déjà résolue si l’usager le souhaite.
# Solution | Générer un fichier txt avec les données dedans.

# Essai
def sauvegarder(grille):
    f_output = open("sauvegarde.txt", "w")
    
    for ligne in grille:
        for valeur in ligne:
            f_output.write(str(valeur) + " ")
        f_output.write("\n")
    
    f_output.close()