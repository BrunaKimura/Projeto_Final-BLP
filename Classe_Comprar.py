from Classe_Jogar import Jogo
from Classe_Firebase import Firebase

class Compras:
    
    def __init__(self, login, lista):
        self.jogo= Jogo(login, lista)
        self.firebase=Firebase() 
        self.cofre=self.firebase.moedas(self.jogo.jogador)
        if len(self.jogo.Lista_Animais)==8:
            self.preco=100
        elif len(self.jogo.Lista_Animais)==9:
            self.preco=200
        elif len(self.jogo.Lista_Animais)==10:
            self.preco=400
        elif len(self.jogo.Lista_Animais)==11:
            self.preco=1000
        elif len(self.jogo.Lista_Animais)==10:
            self.preco=2000

#função utilizada no ato da comprar, recebendo a posição do animal, adicionando ele na lista de animais do usuario, fazendo a estatistica de comra e atualizando a moeda     
    def comprar(self, linha, coluna):
        if self.cofre>=self.preco:
            if linha==0:
                if coluna==1:
                    if self.firebase.Compras(self.jogo.jogador, "Panda")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Panda")
                        self.jogo.Lista_Animais.append("Panda")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        return 1
                elif coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Leão")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Leão")
                        self.jogo.Lista_Animais.append("Leão")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        return 1
            elif linha==1:
                if coluna==1:
                    if self.firebase.Compras(self.jogo.jogador, "Elefante")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Elefante")
                        self.jogo.Lista_Animais.append("Elefante")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        return 1
                if coluna==0:
                    if self.firebase.Compras(self.jogo.jogador, "Galo")==1:
                        self.firebase.comprar(self.jogo.jogador, self.preco, "Galo")
                        self.jogo.Lista_Animais.append("Galo")
                        if len(self.jogo.Lista_Animais)==9:
                            self.firebase.Estatistica(self.jogo.jogador, self.jogo.Lista_Animais[8])
                        self.cofre-=self.preco
                        return 1
        else:
            return -1

#Função que soma as moedas para o usuario e atualiza o cofre do jogo            
    def somar_moeda(self):
        self.firebase.somar_moedas(self.jogo.jogador, 50)
        self.cofre=self.firebase.moedas(self.jogo.jogador)
        
