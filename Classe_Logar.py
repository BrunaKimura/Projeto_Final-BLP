from Classe_Firebase import Firebase
from Classe_Jogar import Jogo

class Login():
    
    def __init__(self):
        self.firebase = Firebase()
        self.jogo=Jogo()
    
    def verifica(self, login, senha):
        if self.firebase.Checar_jogador(login, senha)==1:
            self.jogo.jogador=login
            return 1
        elif self.firebase.Checar_jogador(login, senha)==-1:
            return 0
        elif self.firebase.Checar_jogador(login, senha)==0:
            return -1
