from Classe_Jogar import Jogo
from Classe_Firebase import Firebase

class Compras:
    
    def __init__(self, login):
        self.jogo= Jogo(login)
        self.firebase=Firebase() 
        self.cofre=self.firebase.moedas(self.jogo.jogador)
        self.preco=25
        self.compras=["Panda", "Leão", "Elefante", "Galo"] 
        
    def comprar(self, linha, coluna):
        if self.cofre>=self.preco:
            if linha==0:
                if coluna==1:
                    if self.firebase.Compras(self.jogo.jogador, "Panda")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Panda")
                        self.compras.remove("Panda")
                        self.jogo.Lista_Animais.append("Panda")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        self.preco+=500
                        return 1
                elif coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Leão")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Leão")
                        self.compras.remove("Leão")
                        self.jogo.Lista_Animais.append("Leão")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        self.preco+=500
                        return 1
            elif linha==1:
                if coluna==1:
                    if self.firebase.Compras(self.jogo.jogador, "Elefante")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Elefante")
                        self.compras.remove("Elefante")
                        self.jogo.Lista_Animais.append("Elefante")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        self.preco+=500
                        return 1
                if coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Galo")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Galo")
                        self.compras.remove("Galo")
                        self.jogo.Lista_Animais.append("Galo")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        self.preco+=500
                        return 1
        else:
            return -1
            
    def somar_moeda(self):
        self.firebase.somar_moedas(self.jogo.jogador, 50)
        self.cofre=self.firebase.moedas(self.jogo.jogador)
        
