import firecall

class Firebase:

    def __init__(self):
        #chamar o endereço do firebase        
        self.memoria_firecall = firecall.Firebase("https://estatistica-animal.firebaseio.com/")
        
    #Criar local de armazenamento de dados
    def Salvar_cadastro(self, Dicionario):
        self.memoria_firecall.put_sync(point="/Dados_usuario", data=Dicionario)
        
    #Retonar o jogador para teste
    def Checar_jogador(self, login):
        C = eval(self.memoria_firecall.get_sync(point="/Dados_usuario"))
        if login in C:
            return 1
        else:
            return -1
        
    


        


        
        