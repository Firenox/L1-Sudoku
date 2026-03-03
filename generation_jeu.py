
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
        
        # k//3 la position 
        debut = (k // 3) 
        fin = debut + 3
        chiffres_ligne = [self.grille[i][0][debut:fin], self.grille[i][1][debut:fin], self.grille[i][2][debut:fin]]
        if chiffre in chiffres_ligne:
            return False

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
        chiffres = random.randint(1, 9)
        if k in [1,2,3]:
            chiffres = random.randint(1, 9)
            if chiffres not in self.grille[i][j+1][:3] and chiffres not in self.grille[i][j+3][:3] and chiffres not in self.grille[i][j+6][:3]:
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        if k in [4,5,6]:
            chiffres = random.randint(1, 9)
            if chiffres not in self.grille[i][j+1][3:7] and chiffres not in self.grille[i][j+3][3:7] and chiffres not in self.grille[i][j+6][3:7]:
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        if k in [7,8,9] :
            chiffres = random.randint(1, 9)
            if chiffres not in self.grille[i][j+1][7:] and chiffres not in self.grille[i][j+3][7:] and chiffres not in self.grille[i][j+6][7:]:
                self.grille[i][j][k] = chiffres
                self.ajouter(i, j, k+1)
            else :
                self.ajouter(i, j, k)
        if k == 9:
            j += 1 
            self.ajouter(i, j, 0)
        if j == 3 :
            i += 1
            self.ajouter(i, 0, 0)
            
        
sudo = Sudoku()
sudo.trois_case_en_diagonal()
sudo.ajouter(0,0,0)

sudo.affichage()

