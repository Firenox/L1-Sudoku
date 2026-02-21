
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
    
    #création des 3 cases en diagonale
    def trois_case_en_diagonal(self):
        random.shuffle(case_aléatoire)
        self.ligne1[0] = list(case_aléatoire) 
        random.shuffle(case_aléatoire)
        self.ligne2[1] = list(case_aléatoire)
        random.shuffle(case_aléatoire)
        self.ligne3[2] = list(case_aléatoire)
    
    def affichage(self):
        for i in range(len(self.grille)):
            for j in range(len(self.ligne1)):
                if self.grille[i][j] == []:
                    print(0, end = "   ")
                else :
                    print(self.grille[i][j], end = "   ")
            print()    
    
    def ajout_des_trois(self):
        chiffres = random.randint(1, 9)
        for i in range(3):
            for j in range(3):
                for k in range(9):
                    if k in [1, 2, 3]:
                        if chiffres not in self.grille[i][j+1][:3]:
                                self.grille[i][j][k].append(chiffres)
                        else:
                            
    
    
    
    
sudo = Sudoku()
sudo.trois_case_en_diagonal()
sudo.affichage()