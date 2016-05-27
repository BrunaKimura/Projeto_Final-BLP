import tkinter as tk

from Loja import Loja

from Classe_Jogar import Jogo

from Classe_Comprar import Compras

from imagem_som import Imagens_sons

import tkinter.messagebox as tkm

from time import sleep

from classe_som import *


class Tabuleiro(): 
    def __init__(self, login, lista):
        self.login = login
        self.lista = lista
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Memória ANIMAL")
        self.tabuleiro.resizable ( 0 ,  0 )
        
        self.jogo = Jogo(self.login, self.lista)
        self.jogo.embaralhar()
        
        self.imagens = Imagens_sons()
        
        self.compra = Compras(self.login, self.lista)
           

#Botão para ir à loja
        self.botao_loja = tk.Button(self.tabuleiro, text = 'LOJA', height = 3, width = 30, bg = 'purple')
        self.botao_loja.configure(command = self.abrir_loja)        
        self.botao_loja.grid(row=0, column=0, columnspan=4, sticky = tk.W+tk.E+tk.S+tk.N)
        
#Botões de jogo     
        self.botao1 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao1.configure(command = self.click1)
        self.botao1.grid(row=1, column=0)
        
        self.botao2 = tk.Button(self.tabuleiro, height = 95, width = 102,  image = self.imagens.Icarta)
        self.botao2.configure(command = self.click2)
        self.botao2.grid(row=1, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao3.configure(command = self.click3)
        self.botao3.grid(row=1, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao4.configure(command = self.click4)
        self.botao4.grid(row=1, column=3)
        
        self.botao5 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao5.configure(command = self.click5)
        self.botao5.grid(row=2, column=0)
        
        self.botao6 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao6.configure(command = self.click6)
        self.botao6.grid(row=2, column=1)
        
        self.botao7 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao7.configure(command = self.click7)
        self.botao7.grid(row=2, column=2)
        
        self.botao8 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao8.configure(command = self.click8)
        self.botao8.grid(row=2, column=3)
        
        self.botao9 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao9.configure(command = self.click9)
        self.botao9.grid(row=3, column=0)
        
        self.botao10 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao10.configure(command = self.click10)
        self.botao10.grid(row=3, column=1)
        
        self.botao11 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao11.configure(command = self.click11)
        self.botao11.grid(row=3, column=2)
        
        self.botao12 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao12.configure(command = self.click12)
        self.botao12.grid(row=3, column=3)
        
        self.botao13 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao13.configure(command = self.click13)
        self.botao13.grid(row=4, column=0)
        
        self.botao14 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao14.configure(command = self.click14)
        self.botao14.grid(row=4, column=1)
        
        self.botao15 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao15.configure(command = self.click15)
        self.botao15.grid(row=4, column=2)
        
        self.botao16 = tk.Button(self.tabuleiro, height = 95, width = 102, image = self.imagens.Icarta)
        self.botao16.configure(command = self.click16)
        self.botao16.grid(row=4, column=3)
        
    def click1(self):        
        self.jogo.recebe_jogada(0,0)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 
                       

#Código para aparecer a imagem no botão        
        if self.jogo.Lista_Embaralhada[0]== "Cachorro":
            self.botao1.configure(image = self.imagens.Icachorro, state = "disabled", width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Gato":
            self.botao1.configure(image = self.imagens.Igato, state = "disabled", width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Arara":
            self.botao1.configure(image = self.imagens.Iarara, state = "disabled", width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Vaca":
            self.botao1.configure(image = self.imagens.Ivaca, state = "disabled", width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[0]== "Macaco":
            self.botao1.configure(image = self.imagens.Imacaco, state = "disabled", width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Pato":
            self.botao1.configure(image = self.imagens.Ipato, state = "disabled", width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[0]== "Cavalo":
            self.botao1.configure(image = self.imagens.Icavalo, state = "disabled", width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[0] == "Porco":
            self.botao1.configure(image = self.imagens.Iporco, state = "disabled", width = 102, height = 95)
            Som.play_music(Sporco.play)
        
        elif self.jogo.Lista_Embaralhada[0] == "Elefante":
            self.botao1.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Leão":
            self.botao1.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Panda":
            self.botao1.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[0] == "Galo":
            self.botao1.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)
                    
        
#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1: # -1 é quando a figura esta diferente 
            self.tabuleiro.update()
            sleep(1)          
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
        
    def click2(self):
        self.jogo.recebe_jogada(0,1)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()   
        
#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[1]== "Cachorro":
            self.botao2.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Gato":
            self.botao2.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Arara":
            self.botao2.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Vaca":
            self.botao2.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[1]== "Macaco":
            self.botao2.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Pato":
            self.botao2.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[1]== "Cavalo":
            self.botao2.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[1] == "Porco":
            self.botao2.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Elefante":
            self.botao2.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Leão":
            self.botao2.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Panda":
            self.botao2.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[1] == "Galo":
            self.botao2.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)
 
            
        
#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
                        
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
        
    def click3(self):
        self.jogo.recebe_jogada(0,2)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()
        
        
#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[2]== "Cachorro":
            self.botao3.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Gato":
            self.botao3.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Arara":
            self.botao3.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Vaca":
            self.botao3.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[2]== "Macaco":
            self.botao3.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Pato":
            self.botao3.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[2]== "Cavalo":
            self.botao3.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[2] == "Porco":
            self.botao3.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95) 
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Elefante":
            self.botao3.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Leão":
            self.botao3.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Panda":
            self.botao3.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[2] == "Galo":
            self.botao3.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)
            

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            #chique ou nem ???
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click4(self):
        self.jogo.recebe_jogada(0,3)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[3]== "Cachorro":
            self.botao4.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Gato":
            self.botao4.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Arara":
            self.botao4.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Vaca":
            self.botao4.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[3]== "Macaco":
            self.botao4.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Pato":
            self.botao4.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[3]== "Cavalo":
            self.botao4.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[3] == "Porco":
            self.botao4.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Elefante":
            self.botao4.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Leão":
            self.botao4.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Panda":
            self.botao4.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[3] == "Galo":
            self.botao4.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)
            

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
                        
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click5(self):
        self.jogo.recebe_jogada(1,0)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[4]== "Cachorro":
            self.botao5.configure(image = self.imagens.Icachorro, state = "disabled" ,width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Gato":
            self.botao5.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Arara":
            self.botao5.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Vaca":
            self.botao5.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[4]== "Macaco":
            self.botao5.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Pato":
            self.botao5.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[4]== "Cavalo":
            self.botao5.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[4] == "Porco":
            self.botao5.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Elefante":
            self.botao5.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Leão":
            self.botao5.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Panda":
            self.botao5.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[4] == "Galo":
            self.botao5.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()   
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()

        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou") 
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click6(self):
        self.jogo.recebe_jogada(1,1)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão          
        if self.jogo.Lista_Embaralhada[5]== "Cachorro":
            self.botao6.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Gato":
            self.botao6.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Arara":
            self.botao6.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Vaca":
            self.botao6.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[5]== "Macaco":
            self.botao6.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Pato":
            self.botao6.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[5]== "Cavalo":
            self.botao6.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[5] == "Porco":
            self.botao6.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Elefante":
            self.botao6.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Leão":
            self.botao6.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Panda":
            self.botao6.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[5] == "Galo":
            self.botao6.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click7(self):
        self.jogo.recebe_jogada(1,2)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[6]== "Cachorro":
            self.botao7.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Gato":
            self.botao7.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Arara":
            self.botao7.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Vaca":
            self.botao7.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[6]== "Macaco":
            self.botao7.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Pato":
            self.botao7.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[6]== "Cavalo":
            self.botao7.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[6] == "Porco":
            self.botao7.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Elefante":
            self.botao7.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Leão":
            self.botao7.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Panda":
            self.botao7.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[6] == "Galo":
            self.botao7.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click8(self):
        self.jogo.recebe_jogada(1,3)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)     
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[7]== "Cachorro":
            self.botao8.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Gato":
            self.botao8.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Arara":
            self.botao8.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Vaca":
            self.botao8.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[7]== "Macaco":
            self.botao8.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Pato":
            self.botao8.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[7]== "Cavalo":
            self.botao8.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[7] == "Porco":
            self.botao8.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Elefante":
            self.botao8.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Leão":
            self.botao8.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Panda":
            self.botao8.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[7] == "Galo":
            self.botao8.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
                    
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click9(self):
        self.jogo.recebe_jogada(2,0)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada) 
        self.jogo.verifica_fim()   

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[8]== "Cachorro":
            self.botao9.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Gato":
            self.botao9.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Arara":
            self.botao9.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Vaca":
            self.botao9.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[8]== "Macaco":
            self.botao9.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Pato":
            self.botao9.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[8]== "Cavalo":
            self.botao9.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[8] == "Porco":
            self.botao9.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
        
        elif self.jogo.Lista_Embaralhada[8] == "Elefante":
            self.botao9.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Leão":
            self.botao9.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Panda":
            self.botao9.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[8] == "Galo":
            self.botao9.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click10(self):
        self.jogo.recebe_jogada(2,1)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada) 
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[9]== "Cachorro":
            self.botao10.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Gato":
            self.botao10.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Arara":
            self.botao10.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Vaca":
            self.botao10.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[9]== "Macaco":
            self.botao10.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Pato":
            self.botao10.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[9]== "Cavalo":
            self.botao10.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[9] == "Porco":
            self.botao10.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Elefante":
            self.botao10.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Leão":
            self.botao10.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Panda":
            self.botao10.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[9] == "Galo":
            self.botao10.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click11(self):
        self.jogo.recebe_jogada(2,2)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[10]== "Cachorro":
            self.botao11.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Gato":
            self.botao11.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Arara":
            self.botao11.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Vaca":
            self.botao11.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[10]== "Macaco":
            self.botao11.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Pato":
            self.botao11.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[10]== "Cavalo":
            self.botao11.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[10] == "Porco":
            self.botao11.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Elefante":
            self.botao11.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Leão":
            self.botao11.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Panda":
            self.botao11.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[10] == "Galo":
            self.botao11.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)


#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click12(self):
        self.jogo.recebe_jogada(2,3)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()  

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[11]== "Cachorro":
            self.botao12.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Gato":
            self.botao12.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Arara":
            self.botao12.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Vaca":
            self.botao12.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[11]== "Macaco":
            self.botao12.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Pato":
            self.botao12.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[11]== "Cavalo":
            self.botao12.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[11] == "Porco":
            self.botao12.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Elefante":
            self.botao12.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Leão":
            self.botao12.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Panda":
            self.botao12.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[11] == "Galo":
            self.botao12.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click13(self):
        self.jogo.recebe_jogada(3,0)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[12]== "Cachorro":
            self.botao13.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Gato":
            self.botao13.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Arara":
            self.botao13.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Vaca":
            self.botao13.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[12]== "Macaco":
            self.botao13.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Pato":
            self.botao13.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[12]== "Cavalo":
            self.botao13.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[12] == "Porco":
            self.botao13.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Elefante":
            self.botao13.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Leão":
            self.botao13.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Panda":
            self.botao13.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[12] == "Galo":
            self.botao13.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
            
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
                    
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click14(self):
        self.jogo.recebe_jogada(3,1)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim() 

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[13]== "Cachorro":
            self.botao14.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Gato":
            self.botao14.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Arara":
            self.botao14.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Vaca":
            self.botao14.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[13]== "Macaco":
            self.botao14.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Pato":
            self.botao14.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[13]== "Cavalo":
            self.botao14.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[13] == "Porco":
            self.botao14.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Elefante":
            self.botao14.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Leão":
            self.botao14.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Panda":
            self.botao14.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[13] == "Galo":
            self.botao14.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
        
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
    def click15(self):
        self.jogo.recebe_jogada(3,2)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()

#Código para aparecer a imagem no botão  
        if self.jogo.Lista_Embaralhada[14]== "Cachorro":
            self.botao15.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Gato":
            self.botao15.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Arara":
            self.botao15.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Vaca":
            self.botao15.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[14]== "Macaco":
            self.botao15.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Pato":
            self.botao15.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[14]== "Cavalo":
            self.botao15.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[14] == "Porco":
            self.botao15.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Elefante":
            self.botao15.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Leão":
            self.botao15.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Panda":
            self.botao15.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[14] == "Galo":
            self.botao15.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()  
            self.jogo.limpa_jogada()
        
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
            
            
    def click16(self):
        self.jogo.recebe_jogada(3,3)
        self.jogo.verifica_jogada(self.jogo.Lista_Jogada)
        self.jogo.verifica_fim()

#Código para aparecer a imagem no botão       
        if self.jogo.Lista_Embaralhada[15]== "Cachorro":
            self.botao16.configure(image = self.imagens.Icachorro, state = "disabled",width = 102, height = 95)
            Som.play_music(Scachorro.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Gato":
            self.botao16.configure(image = self.imagens.Igato, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgato.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Arara":
            self.botao16.configure(image = self.imagens.Iarara, state = "disabled",width = 102, height = 95)
            Som.play_music(Sarara.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Vaca":
            self.botao16.configure(image = self.imagens.Ivaca, state = "disabled",width = 102, height = 95)
            Som.play_music(Svaca.play)
            
        elif self.jogo.Lista_Embaralhada[15]== "Macaco":
            self.botao16.configure(image = self.imagens.Imacaco, state = "disabled",width = 102, height = 95)
            Som.play_music(Smacaco.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Pato":
            self.botao16.configure(image = self.imagens.Ipato, state = "disabled",width = 102, height = 95)
            Som.play_music(Spato.play)
            
        elif self.jogo.Lista_Embaralhada[15]== "Cavalo":
            self.botao16.configure(image = self.imagens.Icavalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Scavalo.play)
       
        elif self.jogo.Lista_Embaralhada[15] == "Porco":
            self.botao16.configure(image = self.imagens.Iporco, state = "disabled",width = 102, height = 95)
            Som.play_music(Sporco.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Elefante":
            self.botao16.configure(image = self.imagens.Ielefante, state = "disabled",width = 102, height = 95)
            Som.play_music(Selefante.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Leão":
            self.botao16.configure(image = self.imagens.Ileao, state = "disabled",width = 102, height = 95)
            Som.play_music(Sleao.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Panda":
            self.botao16.configure(image = self.imagens.Ipanda, state = "disabled",width = 102, height = 95)
            Som.play_music(Spanda.play)
            
        elif self.jogo.Lista_Embaralhada[15] == "Galo":
            self.botao16.configure(image = self.imagens.Igalo, state = "disabled",width = 102, height = 95)
            Som.play_music(Sgalo.play)

                    
#Código para verificar se as duas imagens são iguais
        if self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == -1:
            self.tabuleiro.update()
            sleep(1)
            self.virar_imagens()
            self.jogo.limpa_jogada()
        
        elif self.jogo.verifica_jogada(self.jogo.Lista_Jogada) == 1:
            self.jogo.limpa_jogada()
        
            
        if self.jogo.verifica_fim() == 1:
            tkm.showinfo(title = "Game Over", message = "O Jogo Acabou")
            self.compra.somar_moeda()
            self.limpar_painel()
            self.jogo.limpa_jogada()
            self.jogo.limpa_jogo()
            self.jogo.embaralhar()
           
            
    def limpar_painel(self):
        self.botao1.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao2.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao3.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao4.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao5.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao6.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao7.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao8.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao9.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao10.configure(image= self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao11.configure(image = self.imagens.Icarta, state="normal", height = 96, width = 102)
        self.botao12.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao13.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao14.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao15.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        self.botao16.configure(image = self.imagens.Icarta, state="normal", height = 95, width = 102)
        
    def virar_imagens(self):
        
#combinação com o botao 1
    
        if self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao2'or self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao3'or self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao4'or self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao5'or self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao6'or self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
    
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao1' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao1':
            self.botao1.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
#combinação para o segundo botao
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao3'or self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao4'or self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao5'or self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao6'or self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao2' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao2':
            self.botao2.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação com o batao 3
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao4'or self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao5'or self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao6'or self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao3' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao3':
            self.botao3.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 4
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao5'or self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao6'or self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image =self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao4' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao4':
            self.botao4.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 5
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao6'or self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao5' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao5':
            self.botao5.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 6 
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao7'or self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image =self.imagens.Icarta,  state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao6' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao6':
            self.botao6.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 7
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao8'or self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao7' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao7':
            self.botao7.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 8
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao9'or self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao8' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao8':
            self.botao8.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 9
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao10'or self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
        
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao9' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao9':
            self.botao9.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 10
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao11'or self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao10' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao10':
            self.botao10.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinção para o botao 11
            
        elif self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao12'or self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao11':
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao11':
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta , state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao11':
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao11':
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao11' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao11':
            self.botao11.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 12
            
        elif self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao13'or self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao12':
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao12':
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao12':
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao12' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao12':
            self.botao12.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 13
            
        elif self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao14'or self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao13':
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao13':
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao13' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao13':
            self.botao13.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 14
            
        elif self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao15'or self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao14':
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
        elif self.jogo.Lista_Botão[0] == 'botao14' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao14':
            self.botao14.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
#combinação para o botao 15
            
        elif self.jogo.Lista_Botão[0] == 'botao15' and self.jogo.Lista_Botão[1] == 'botao16'or self.jogo.Lista_Botão[0] == 'botao16' and self.jogo.Lista_Botão[1] == 'botao15':
            self.botao15.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            self.botao16.configure(image = self.imagens.Icarta, state = "normal", height = 95, width = 102)
            
            
        
            
    def abrir_loja(self):
        self.lojinha = Loja(self.login, self.lista)
        self.lojinha.iniciar()        
        
    def iniciar(self):
        self.tabuleiro.geometry('440x460')
        self.tabuleiro.mainloop()
        


            