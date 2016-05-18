from Classe_Jogar import Jogo
from Classe_Firebase import Firebase

class Compras:
    
    def __init__(self):
        self.jogo= Jogo()
        self.moeda=0
        self.preco=50
        self.compras=["Panda", "Leão", "Elefante", "Galo"]
        self.firebase=Firebase()     
        
    def comprar(self, linha, coluna):
        if self.preco<=self.moeda:
            self.moeda-=self.preco
            self.preco=len((self.jogo.Lista_Animais-8)*50+50) 
            if linha==2:
                if coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Panda")==1:                    
                        self.compras.remove("Panda")
                        self.jogo.Lista_Animais.append("Panda")
                        return "Panda"
                    else:
                        return 0
                elif coluna==2:
                    if self.firebase.Compras(self.jogo.jogador, "Leão")==1:
                        self.compras.remove("Leão")
                        self.jogo.Lista_Animais.append("Leão")
                        return "Leão"
                    else:
                        return 0
            elif linha==4:
                if coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Elefante")==1:
                        self.compras.remove("Elefante")
                        self.jogo.Lista_Animais.append("Elefante")
                        return "Elefante"
                    else:
                        return 0
                if coluna==2:
                    if self.firebase.Compras(self.jogo.jogador, "Galo")==1:
                        self.compras.remove("Galo")
                        self.jogo.Lista_Animais.append("Galo")
                        return "Galo"
                    else:
                        return 0
        else:
            return -1
            
    def somar_moeda(self):
        self.moeda+=50
            
            
            