from Classe_Firebase import Firebase

class cadastrar():
    
    def __init__(self):
        self.firebase = Firebase()
        
    def adicionar_cadastro(self, login, senha, sexo, idade):
        if self.firebase.Checar_jogador(login, 1)==-1:        
            self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            return 1
        
        else:
            return -1