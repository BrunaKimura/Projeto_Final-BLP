import numpy as np

class Jogo():

    def __init__(self):      
        self.Lista_Animais=["Cachorro", "Gato", "Arara", "Vaca", "Macaco", "Pato", "Cavalo", "Porco"] #Lista de animais, já contém os animais iniciais.
        self.Lista_Escolhida=[]
        self.Lista_Dobrada=[]
        self.Lista_Embaralhada=[]
        self.Tabuleiro=[]
        self.Lista_Jogada=[]
        self.Lista_Botão=[]        
        
    def embaralhar(self):
        self.Lista_Escolhida=np.random.choice(self.Lista_Animais, 8, replace=False)
        for e in self.Lista_Escolhida:
            self.Lista_Dobrada.append(e)
            self.Lista_Dobrada.append(e)
        self.Lista_Embaralhada=np.random.permutation(self.Lista_Dobrada)
        self.Tabuleiro=[[self.Lista_Embaralhada[0], self.Lista_Embaralhada[1], self.Lista_Embaralhada[2], self.Lista_Embaralhada[3]], [self.Lista_Embaralhada[4], self.Lista_Embaralhada[5], self.Lista_Embaralhada[6], self.Lista_Embaralhada[7]], [self.Lista_Embaralhada[8], self.Lista_Embaralhada[9], self.Lista_Embaralhada[10], self.Lista_Embaralhada[11]], [self.Lista_Embaralhada[12], self.Lista_Embaralhada[13], self.Lista_Embaralhada[14], self.Lista_Embaralhada[15]]]
        
    def recebe_jogada(self, linha, coluna):
        self.Lista_Jogada.append(self.Tabuleiro[linha][coluna])
        self.Lista_Botão.append([linha, coluna])
        if self.Tabuleiro[linha][coluna]=="Cachorro":
            return "Cachorro"
        elif self.Tabuleiro[linha][coluna]=="Gato":
            return "Gato"
        elif self.Tabuleiro[linha][coluna]=="Arara":
            return "Arara"
        elif self.Tabuleiro[linha][coluna]=="Vaca":
            return "Vaca"
        elif self.Tabuleiro[linha][coluna]=="Macaco":
            return "Macaco"
        elif self.Tabuleiro[linha][coluna]=="Pato":
            return "Pato"
        elif self.Tabuleiro[linha][coluna]=="Cavalo":
            return "Cavalo"
        elif self.Tabuleiro[linha][coluna]=="Porco":
            return "Porco"
            
    def verifica_jogada(self, Lista_Jogada):
        if len(self.Lista_Jogada)==0:
            return 0
        elif len(self.Lista_Jogada)==2: 
            if self.Lista_Jogada[0]==self.Lista_Jogada[1]: 
                for i in range(4):
                    for e in range(4):
                        if self.Tabuleiro[i][e]==self.Lista_Jogada[0]:
                            self.Tabuleiro[i][e]="z"
                        elif self.Tabuleiro[i][e]==self.Lista_Jogada[1]:
                            self.Tabuleiro[i][e]="z"
                return 1
            elif self.Lista_Jogada[0]!=self.Lista_Jogada[1]:
                return -1
        elif len(self.lista_Jogada)==1:
            return -2
    
    def verifica_fim(self):
        if (self.Tabuleiro[0][0]=="z" and self.Tabuleiro[0][1]=="z" and self.Tabuleiro[0][2]=="z" and self.Tabuleiro[0][3]=="z" and self.Tabuleiro[1][0]=="z" and self.Tabuleiro[1][1]=="z" and self.Tabuleiro[1][2]=="z" and self.Tabuleiro[1][3]=="z" and self.Tabuleiro[2][0]=="z" and self.Tabuleiro[2][1]=="z" and self.Tabuleiro[2][2]=="z" and self.Tabuleiro[2][3]=="z" and self.Tabuleiro[3][0]=="z" and self.Tabuleiro[3][1]=="z" and self.Tabuleiro[3][2]=="z" and self.Tabuleiro[3][3]=="z"):
            return 1
        else:
            return -1
    
    def limpa_jogada(self):
        self.Lista_Jogada=[]
        self.Lista_Botão=[]


