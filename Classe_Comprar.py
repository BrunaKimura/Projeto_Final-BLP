from imagem_som import Imagens_sons as IS


class Compras:
    
    def __init__(self):
        self.Is = IS() 
        self.moeda=0
        self.preco=50
        self.compras=["Panda", "Leão", "Elefante", "Galo"]
    
    def comprar(self, linha, coluna):
        if self.preco<=self.moeda:
            self.moeda-=self.preco
            self.preco+=50
            if linha==2:
                if coluna==0:
                    self.compras.remove("Panda")
                    return "Panda"                    
                if coluna==2:
                    self.compras.remove("Leão")
                    return "Leão"
            elif linha==4:
                if coluna==0:
                    self.compras.remove("Elefante")
                    return "Elefante"
                if coluna==2:
                    self.compras.remove("Galo")
                    return "Galo"
        else:
            return -1
