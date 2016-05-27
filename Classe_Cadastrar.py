from Classe_Firebase import Firebase

class cadastrar():
    
    def __init__(self):
        self.firebase = Firebase()
        
    def adicionar_cadastro(self, login, senha, sexo, idade):
        if self.firebase.Checar_jogador(login, senha)== -1:  
            if type(idade)==str:
                return 2
            if (sexo=="Masculino" or sexo=="masculino" or sexo=="MASCULINO" or sexo=="m" or sexo=="M"):
                sexo="M"
                self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            elif (sexo=="Feminino" or sexo=="feminino" or sexo=="FEMININO" or sexo=="f" or sexo=="F"):
                sexo="F"
                self.firebase.Salvar_cadastro(login, senha, sexo, idade)
            else:
                return 0
            return 1
        elif self.firebase.Checar_jogador(login,senha)==1 or self.firebase.Checar_jogador(login,senha)==0:
            return -1