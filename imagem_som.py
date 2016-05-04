from tkinter import PhotoImage
import winsound as ws

class Imagens_sons:

    def __init__(self):
        
#8 animais principais:
        self.Icachorro = PhotoImage(file=".gif")
        self.Igato = PhotoImage(file=".gif")
        self.Iarara = PhotoImage(file=".gif")
        self.Ivaca = PhotoImage(file=".gif")
        self.Imacaco = PhotoImage(file=".gif")
        self.Ipato = PhotoImage(file=".gif")
        self.Icavalo = PhotoImage(file=".gif")
        self.Iporco = PhotoImage(file=".gif")

#8 sons dos animais principais        
        self.Scachorro = ws.PlaySound('latido.wav', ws.SND_FILENAME)
        self.Sgato =  ws.PlaySound('', ws.SND_FILENAME)
        self.Sarara =  ws.PlaySound('', ws.SND_FILENAME)
        self.Svaca =  ws.PlaySound('', ws.SND_FILENAME)
        self.Smacaco =  ws.PlaySound('', ws.SND_FILENAME)
        self.Spato =  ws.PlaySound('', ws.SND_FILENAME)
        self.Scavalo =  ws.PlaySound('', ws.SND_FILENAME)
        self.Sporco =  ws.PlaySound('', ws.SND_FILENAME)
        
#4 imagens dos animais da loja
        self.Ipanda = PhotoImage(file=".gif")
        self.Ileao = PhotoImage(file=".gif")
        self.Ielefante = PhotoImage(file=".gif")
        self.Igalo = PhotoImage(file=".gif")   
    
#4 sons dos animais principais        
        self.Spanda = ws.PlaySound('', ws.SND_FILENAME)
        self.Sleao =  ws.PlaySound('', ws.SND_FILENAME)
        self.Selefante =  ws.PlaySound('', ws.SND_FILENAME)
        self.Sgalo =  ws.PlaySound('', ws.SND_FILENAME)

        
        