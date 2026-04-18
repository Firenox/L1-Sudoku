'''
Le programme suivant permet de générer la matrice du sudoku rempli et valide.
'''



import random

#création du brouillon de case
case_aléatoire = [1,2,3,4,5,6,7,8,9]
random.shuffle(case_aléatoire)

class Sudoku :
    #ligne = 9 cases
    def __init__(self):
        self.grille = []
        self.ligne1 = []
        self.ligne2 = []
        self.ligne3 = []
        self.grille = [self.ligne1, self.ligne2, self.ligne3]
        
        for i in range(3):
            self.ligne1.append([])
            self.ligne2.append([])
            self.ligne3.append([])
        self.grille = [self.ligne1, self.ligne2, self.ligne3]
    
    
    
    #création des 3 cases en diagonale + les 0 des autres cases
    def trois_case_en_diagonal(self):
        random.shuffle(case_aléatoire)
        self.ligne1[0] = list(case_aléatoire) 
        random.shuffle(case_aléatoire)
        self.ligne2[1] = list(case_aléatoire)
        random.shuffle(case_aléatoire)
        self.ligne3[2] = list(case_aléatoire)
        
        for i in range(len(self.grille)):
            for j in range(len(self.ligne1)):
                if self.grille[i][j] == [] :
                    self.grille[i][j] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                
                
    #affiche
    def affichage(self):
        for i in range(len(self.grille)):
            for j in range(len(self.ligne1)):
                if self.grille[i][j] == []:
                    print(0, end = "   ")
                else :
                    print(self.grille[i][j], end = "   ")
            print()    
            
    
    
    def est_valide(self, chiffre, i, j, k):
        if chiffre in self.grille[i][j]:
            return False
        
        # k//3 la position / vérife en ligne
        debut = (k // 3) * 3
        fin = debut + 3
        chiffres_ligne = self.grille[i][0][debut:fin] + self.grille[i][1][debut:fin] + self.grille[i][2][debut:fin]
        if chiffre in chiffres_ligne:
            return False

        # vérife en colonne
        col = k % 3
        chiffres_colonne = []
        for ligne_bloc in range(3):
            chiffres_colonne.append(self.grille[ligne_bloc][j][col])
            chiffres_colonne.append(self.grille[ligne_bloc][j][col + 3])
            chiffres_colonne.append(self.grille[ligne_bloc][j][col + 6])
        if chiffre in chiffres_colonne:
            return False
        
        return True



    def ajouter(self, i, j, k):
        if k == 9:
            j += 1 
            self.ajouter(i, j, 0)
        elif j == 3:
            i += 1
            self.ajouter(i, 0, 0)
            
        if self.grille[i][j][k] != 0:
            return self.ajouter(i, j, k)
        
        chiffres = random.randint(1, 10)
        if k in [0,1,2]:
            chiffres = random.randint(1, 10)
            if self.est_valide(chiffres, i, j, k):
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        if k in [3,4,5]:
            chiffres = random.randint(1, 10)
            if self.est_valide(chiffres, i, j, k):  
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        if k in [6,7,8] :
            chiffres = random.randint(1, 10)
            if self.est_valide(chiffres, i, j, k):
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        
    
    def ajouter1(self, i, j, k):
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
            return self.ajouter1(i, j, k + 1)
    
        # remplie la case
        for num in range(1, 10):
            if self.est_valide(num, i, j, k):
                self.grille[i][j][k] = num
                if self.ajouter1(i, j, k + 1):
                    return True
                # zéro si ça  marche pas 
                self.grille[i][j][k] = 0 
                
        return False

"""     
sudo = Sudoku()
sudo.trois_case_en_diagonal()
sudo.ajouter1(0,0,0)
sudo.affichage()
"""

def generer_grille():
    sudo = Sudoku()
    sudo.trois_case_en_diagonal()
    sudo.ajouter1(0, 0, 0)
    return sudo.grille