import numpy as np

class jogo():

    def __init__(self):
        self.Lista_Animais=["Cachorro","Gato","Arara","Vaca","Hamster","Pato","Cavalo","Porco"] #Lista de animais, já contém os animais iniciais.
        self.Lista_Escolhida=[]
        self.Lista_Dobrada=[]
        self.Lista_Embaralhada=[]
        self.Tabuleiro=[]
        
    def embaralhar(self):
        self.Lista_Escolhida=np.random.choice(self.Lista_Animais, 8, replace=False)
        for e in self.Lista_Escolhida:
            self.Lista_Dobrada.append(e)
            self.Lista_Dobrada.append(e)
        self.Lista_Embaralhada=np.random.permutation(self.Lista_Dobrada)
        self.Tabuleiro=[[self.Lista_Embaralhada[0], self.Lista_Embaralhada[1], self.Lista_Embaralhada[2], self.Lista_Embaralhada[3]], [self.Lista_Embaralhada[4], self.Lista_Embaralhada[5], self.Lista_Embaralhada[6], self.Lista_Embaralhada[7]], [self.Lista_Embaralhada[8], self.Lista_Embaralhada[9], self.Lista_Embaralhada[10], self.Lista_Embaralhada[11]], [self.Lista_Embaralhada[12], self.Lista_Embaralhada[13], self.Lista_Embaralhada[14], self.Lista_Embaralhada[15]]]

v=jogo()

v.embaralhar()

print(v.Tabuleiro)