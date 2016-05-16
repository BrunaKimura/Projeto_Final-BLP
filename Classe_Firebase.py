import firecall

class Firebase:

    def __init__(self):
        #chamar o endereço do firebase        
        self.memoria_firecall = firecall.Firebase("https://estatistica-animal.firebaseio.com/")
        
    #Criar local de armazenamento de dados
    def Salvar_cadastro(self, login, senha, sexo, idade):
        self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/senha".format(login), data=senha)
        self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/sexo".format(login), data=sexo)
        self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/idade".format(login), data=idade)
        
    #Checar se o usuário já existe e se sim se sua senha está correta
    def Checar_jogador(self, login, senha):
        C = eval(self.memoria_firecall.get_sync(point="/Dados_usuario"))
        if login in C:
            D = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/senha".format(login)))
            if D == senha:
                return 1
            else:
                return 0              
        else:
            return -1
        
    


        


        
        