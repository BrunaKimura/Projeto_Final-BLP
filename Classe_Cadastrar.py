class cadastrar():
    
    def __init__(self):
        self.cadastros=dict
        
    def adicionar_cadastro(self, login, senha, sexo, idade):
        if not login in self.cadastros:        
            self.cadastros[login]=[senha, sexo, idade]
        else:
            return -1
