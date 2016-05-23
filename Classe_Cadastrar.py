from Classe_Firebase import Firebase

class cadastrar():
    
    def __init__(self):
        self.firebase = Firebase()
        
    def adicionar_cadastro(self, login, senha, sexo, idade):
        if self.firebase.Checar_jogador(login, senha)== -1:  
            self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            return 1
        elif self.firebase.Checar_jogador(login,senha)== (1 or 0):
            return -1