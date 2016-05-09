from imagem_som import Imagens_sons as IS

class Compras:
    
    def __init__(self):
        self.Is = IS() 
        self.moeda=0
        self.preco=50
        self.compras=[self.Is.Ipanda, self.Is.Ileao, self.Is.Ielefante, self.Is.Igalo]
    
    def comprar(self, linha, coluna):
        if self.preco<=self.moeda:
            self.moeda-=self.preco
            self.preco+=50
            if linha==2:
                if coluna==0:
                    self.compras.remove(self.Is.Ipanda)
                if coluna==2:
                    self.compras.remove(self.Is.Ileao)
            elif linha==4:
                if coluna==0:
                    self.compras.remove(self.Is.Ielefante)
                if coluna==2:
                    self.compras.remove(self.Is.Igalo)
            return 1
        else:
            return -1
        
v=Comprar()
print(v.compras)