import firecall

class Firebase:
    
    def __init__(self):
        self.memoria_firecall = firecall.Firebase("https://estatistica-animal.firebaseio.com/")
        
    def Salvar_cadastro(self, Dicionario):
        self.memoria_firecall.put_sync(point="/Dados_usuario", data=Dicionario)