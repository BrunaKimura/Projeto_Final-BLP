from tkinter import PhotoImage
import winsound as ws

class Imagens_sons:

    def __init__(self):
        
#8 animais principais:
        self.Icachorro = PhotoImage(file="Icachorro.gif")
        self.Igato = PhotoImage(file="Igato.gif")
        self.Iarara = PhotoImage(file="Iarara.gif")
        self.Ivaca = PhotoImage(file="Ivaca.gif")
        self.Imacaco = PhotoImage(file="Imacaco.gif")
        self.Ipato = PhotoImage(file="Ipato.gif")
        self.Icavalo = PhotoImage(file="Icavalo.gif")
        self.Iporco = PhotoImage(file="Iporco.gif")

#8 sons dos animais principais        
        self.Scachorro = ws.PlaySound('scachorro.wav', ws.SND_ASYNC)
        self.Sgato =  ws.PlaySound('sgato.wav', ws.SND_ASYNC)
        self.Sarara =  ws.PlaySound('sarara.wav', ws.SND_ASYNC)
        self.Svaca =  ws.PlaySound('svaca.wav', ws.SND_ASYNC)
        self.Smacaco =  ws.PlaySound('smacaco.wav', ws.SND_ASYNC)
        self.Spato =  ws.PlaySound('spato.wav', ws.SND_ASYNC)
        self.Scavalo =  ws.PlaySound('scavalo.wav', ws.SND_ASYNC)
        self.Sporco =  ws.PlaySound('sporco.wav', ws.SND_ASYNC)
        
#4 imagens dos animais da loja
        self.Ipanda = PhotoImage(file="Ipanda.gif")
        self.Ileao = PhotoImage(file="Ileao.gif")
        self.Ielefante = PhotoImage(file="Ielefante.gif")
        self.Igalo = PhotoImage(file="Igalo.gif")   
    
#4 sons dos animais principais        
        self.Spanda = ws.PlaySound('spanda.wav', ws.SND_ASYNC)
        self.Sleao =  ws.PlaySound('sleao.wav', ws.SND_ASYNC)
        self.Selefante =  ws.PlaySound('selefante.wav', ws.SND_ASYNC)
        self.Sgalo =  ws.PlaySound('sgalo.wav', ws.SND_ASYNC)
        
#Fundo das telas!
        self.Imenu = PhotoImage(file="fundo_menu.gif")
        self.Icadastro = PhotoImage(file = "fundo_cadastro.gif")
        self.Iinterface = PhotoImage(file = "fundo_interface.gif")
        self.Iloja = PhotoImage(file = "fundo_loja.gif")
        self.Icarta = PhotoImage(file = "fundo_carta.gif")
        

        
        