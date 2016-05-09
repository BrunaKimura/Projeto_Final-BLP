class Login():
    
    def __init__(self):
        self.usuarios=dict

    
    def verifica(self, login, senha):
        if (login and senha) in self.usuarios:
            return 1
        else:
            return -1