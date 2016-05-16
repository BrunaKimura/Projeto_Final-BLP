from Classe_Firebase import Firebase

class Login():
    
    def __init__(self):
        self.firebase = Firebase()
    
    def verifica(self, login, senha):
        if self.firebase.Checar_jogador(login, senha)==1:
            return 1
        elif self.firebase.Checar_jogador(login, senha)==-1:
            return 0
        elif self.firebase.Checar_jogador(login, senha)==0:
            return -1