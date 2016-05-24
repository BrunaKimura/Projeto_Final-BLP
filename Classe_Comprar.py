from Classe_Jogar import Jogo
from Classe_Firebase import Firebase

class Compras:
    
    def __init__(self, login):
        self.jogo= Jogo(login)
        self.firebase=Firebase() 
        self.cofre=0
        self.preco=500
        self.ganho=50
        self.compras=["Panda", "Leão", "Elefante", "Galo"]   
        
    def comprar(self, linha, coluna):
        if self.preco<=self.cofre:
            self.cofre-=self.preco
            self.preco+=500
            if linha==0:
                if coluna==1:
                    self.compras.remove("Panda")
                    self.jogo.Lista_Animais.append("Panda")
                    return 1
                elif coluna==0:
                    self.compras.remove("Leão")
                    self.jogo.Lista_Animais.append("Leão")
                    return 1
            elif linha==1:
                if coluna==1:
                    self.compras.remove("Elefante")
                    self.jogo.Lista_Animais.append("Elefante")
                    return 1
                if coluna==0:
                    self.compras.remove("Galo")
                    self.jogo.Lista_Animais.append("Galo")
                    return 1
        else:
            return -1
            
    def somar_moeda(self):
        print(self.cofre)
        self.cofre+=50
     
