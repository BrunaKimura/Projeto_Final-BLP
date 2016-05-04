import numpy as np

class jogo():

    def __init__(self):
        self.Lista_Animais=["Cachorro","Gato","Arara","Vaca","Hamster","Pato","Cavalo","Porco"] #Lista de animais, já contém os animais iniciais.
        self.Lista_Escolhida=[]
        self.Lista_Dobrada=[]
        self.Lista_Embaralhada=[]
        self.Tabuleiro=[]
        self.Lista_Jogada=[]
        self.Dinheiro=0     
        
    def embaralhar(self):
        self.Lista_Escolhida=np.random.choice(self.Lista_Animais, 8, replace=False)
        for e in self.Lista_Escolhida:
            self.Lista_Dobrada.append(e)
            self.Lista_Dobrada.append(e)
        self.Lista_Embaralhada=np.random.permutation(self.Lista_Dobrada)
        self.Tabuleiro=[[self.Lista_Embaralhada[0], self.Lista_Embaralhada[1], self.Lista_Embaralhada[2], self.Lista_Embaralhada[3]], [self.Lista_Embaralhada[4], self.Lista_Embaralhada[5], self.Lista_Embaralhada[6], self.Lista_Embaralhada[7]], [self.Lista_Embaralhada[8], self.Lista_Embaralhada[9], self.Lista_Embaralhada[10], self.Lista_Embaralhada[11]], [self.Lista_Embaralhada[12], self.Lista_Embaralhada[13], self.Lista_Embaralhada[14], self.Lista_Embaralhada[15]]]
    
    def recebe_jogada(self, linha, coluna):
        self.Lista_Jogada.append(self.Tabuleiro[linha][coluna])
    
    def verifica_jogada(self, Lista_Jogada):
        if len(self.Lista_Jogada)==0:
            return 0
        elif self.Lista_Jogada[0]==self.Lista_Jogada[1]: 
            return 1
        elif self.Lista_Jogada[0]!=self.Lista_Jogada[1]:
             return -1

        
    def limpa_jogada(self):
        self.Lista_Jogada=[]
    

        
        
v=jogo()

v.embaralhar()
v.recebe_jogada(3,2)
v.recebe_jogada(1,2)
v.verifica_jogada(v.Lista_Jogada)


print(v.verifica_jogada(v.Lista_Jogada))
print(v.Lista_Jogada)
print(v.Tabuleiro)