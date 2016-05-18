from Classe_Firebase import Firebase

class cadastrar():
    
    def __init__(self):
        self.firebase = Firebase()
        
    def adicionar_cadastro(self, login, senha, sexo, idade):
        if self.firebase.Checar_jogador(login, 1)==-1:  
            if sexo=="masculino" or sexo=="Masculino" or sexo=="MASCULINO":
                sexo="M"
                self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            elif sexo=="feminino" or sexo=="Feminino" or sexo=="FEMININO":
                sexo="F"
                self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            else:
                self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            return 1
        else:
            return -1