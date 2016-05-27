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
        self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/compras".format(login), data=["Cachorro", "Gato", "Arara", "Vaca", "Macaco", "Pato", "Cavalo", "Porco"])
        self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/moedas".format(login), data=0)
        
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
        
  #para que seja possivel mostrar a quantidade de moeda no jogo
    def moedas (self, login):
        a = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/moedas".format(login)))
        return a
        


   #armazenar moedas
    def somar_moedas(self, login, moeda):
        a = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/moedas".format(login)))
        eval(self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/moedas".format(login), data = a + moeda))
   
   #tirar moedas na compra
    def comprar (self, login, moeda, animal):
       a = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/moedas".format(login)))
       b = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/compras".format(login)))
       b.append(animal)
       eval(self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/moedas".format(login), data = a - moeda))
       eval(self.memoria_firecall.put_sync(point="/Dados_usuario/{0}/compras".format(login), data = b))
       
  
  #guardar a quantidade de vezes que o animal foi esclhido e por qual sexo.
    def Estatistica (self, login, animal):
        sexo = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/sexo".format(login)))
        a =eval(self.memoria_firecall.get_sync(point="/Animais/{0}/{1}".format(animal, sexo)))
        eval(self.memoria_firecall.put_sync(point="/animais ecolhidos/{0}/{1}".format(animal, sexo), data = a + 1))
        
    #guardar os animais já comprados
    def Compras (self, login, animal):
        A = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/compras".format(login)))
        if animal in A:
            return -1
        else:
            return 1
            
    #para saber qual animal já foi comprado
    def Animais (self, login,):
        A = eval(self.memoria_firecall.get_sync(point="/Dados_usuario/{0}/compras".format(login)))
        return A
        
        
    


        


        
        