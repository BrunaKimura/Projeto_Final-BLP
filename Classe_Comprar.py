class Comprar:
    
    def __init__(self):
        self.moeda=0
        self.preco=50
        self.compras=["Panda", "Leão", "Elefante", "Galo"]
    
    def comprar(self, linha, coluna):
        if self.preco<=self.moeda:
            self.moeda-=self.preco
            self.preco+=50
            if linha==2:
                if coluna==0:
                    self.compras.remove("panda")
                if coluna==2:
                    self.compras.remove("leão")
            elif linha==4:
                if coluna==0:
                    self.compras.remove("elefante")
                if coluna==2:
                    self.compras.remove("galo")
            return 1
        else:
            return -1
        
    