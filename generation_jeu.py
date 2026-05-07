'''
Le programme suivant permet de générer une classe pour créer la matrice du sudoku
1er étape : créer la classe et son constructeur
2eme étape : créer les 3 grandes cases en diagonales 
3eme étape : remplir le reste des cases en tenant compte de toute les restrictions du jeu de sudoku
'''


import random

#création d'un brouillon de case
case_aléatoire = [1,2,3,4,5,6,7,8,9]
#mélange 
random.shuffle(case_aléatoire)

class Sudoku :
    #une ligne à 9 cases
    def __init__(self):
        self.grille = []
        self.ligne1 = []
        self.ligne2 = []
        self.ligne3 = []
        #on met d'abord les 3 lignes pour avoir 1/3 de la matrice
        self.grille = [self.ligne1, self.ligne2, self.ligne3]
        
        #on rajoute les lignes restant à la matrice
        for i in range(3):
            self.ligne1.append([])
            self.ligne2.append([])
            self.ligne3.append([])
        self.grille = [self.ligne1, self.ligne2, self.ligne3]
    
    
    #création des 3 cases en diagonale 
    def trois_case_en_diagonal(self):
        random.shuffle(case_aléatoire)
        self.ligne1[0] = list(case_aléatoire) 
        random.shuffle(case_aléatoire)
        self.ligne2[1] = list(case_aléatoire)
        random.shuffle(case_aléatoire)
        self.ligne3[2] = list(case_aléatoire)
        
        #transformation du vide en 0 pour pouvoir mieux la manipuler
        for i in range(len(self.grille)):
            for j in range(len(self.ligne1)):
                if self.grille[i][j] == [] :
                    self.grille[i][j] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                
                
    #affiche dans le terminale pour mieux visualiser
    def affichage(self):
        for i in range(len(self.grille)):
            for j in range(len(self.ligne1)):
                if self.grille[i][j] == []:
                    print(0, end = "   ")
                else :
                    print(self.grille[i][j], end = "   ")
            print()    
            
    # voir si le chiffre peux ce mettre dans la case donner 
    def est_valide(self, chiffre, i, j, k):
        # il faut pas que le chiffre soit dans la grande case 
        if chiffre in self.grille[i][j]:
            return False
        
        # k//3 la position + vérifie si il y a le meme nombre dans la ligne
        debut = (k // 3) * 3
        fin = debut + 3
        chiffres_ligne = self.grille[i][0][debut:fin] + self.grille[i][1][debut:fin] + self.grille[i][2][debut:fin]
        if chiffre in chiffres_ligne:
            return False

        # vérifie si il y a le meme nombre dans la colonne
        col = k % 3
        chiffres_colonne = []
        for ligne_bloc in range(3):
            chiffres_colonne.append(self.grille[ligne_bloc][j][col])
            chiffres_colonne.append(self.grille[ligne_bloc][j][col + 3])
            chiffres_colonne.append(self.grille[ligne_bloc][j][col + 6])
        if chiffre in chiffres_colonne:
            return False
        
        #si il n'existe nul par alors c'est bon
        return True

    #remplie la matrice
    def ajouter(self, i, j, k):
        # k = case, si fin de case, alors passer colonne suivante et case = 0
        if k == 9:
            k = 0
            j += 1
        if j == 3:
            j = 0
            i += 1
        #fin 
        if i == 3:
            return True 
    
        # vérif si la case est déjà remplie (Diagonales)
        if self.grille[i][j][k] != 0:
            return self.ajouter(i, j, k + 1)
    
        # remplie la case 
        for num in range(1, 10):
            if self.est_valide(num, i, j, k):
                self.grille[i][j][k] = num
                if self.ajouter(i, j, k + 1):
                    return True
                # zéro si ça  marche pas 
                self.grille[i][j][k] = 0 
                
        return False

    
    # choix des difficulter du jeu
    # et enleve un certains nombre de case 
    def difficulter(self):
        # dans les for on peut enlever une case qui est déjà enlever 
        difficulté = input("choisissez entre super easy, easy, normal, hard")
        # diificulter pour teste rapidement 
        if difficulté == "super easy":
            for i in range(2):
                chiffres = random.randint(0, 2)
                chiffres2 = random.randint(0, 2)
                chiffres3 = random.randint(2, 7)
                self.grille[chiffres][chiffres2][chiffres3] = 0
        elif difficulté == "easy" :
            for i in range(10):
                chiffres = random.randint(0, 2)
                chiffres2 = random.randint(0, 2)
                chiffres3 = random.randint(0, 8)
                self.grille[chiffres][chiffres2][chiffres3] = 0
        elif difficulté == "normal" :
            for i in range(20):
                chiffres = random.randint(0, 2)
                chiffres2 = random.randint(0, 2)
                chiffres3 = random.randint(0, 8)
                self.grille[chiffres][chiffres2][chiffres3] = 0
        else : 
            for i in range(30):
                chiffres = random.randint(0, 2)
                chiffres2 = random.randint(0, 2)
                chiffres3 = random.randint(0, 8)
                self.grille[chiffres][chiffres2][chiffres3] = 0
        print(chiffres, chiffres ,chiffres2)

# pour tester
def generer_grille():
    sudo = Sudoku()
    sudo.trois_case_en_diagonal()
    sudo.ajouter(0, 0, 0)

    return sudo.grille
