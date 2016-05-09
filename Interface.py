import tkinter as tk

from Loja import Loja

from Classe_Jogar import Jogo

class Tabuleiro(): 
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Memória ANIMAL")
        
        self.jogo = Jogo()
        
#Label com a imagem de um cifrão
        self.label_cifrao = tk.Label(self.tabuleiro, text = '$', font ='Arial')
        self.label_cifrao.grid(row=0, column=0)
        
#Label da contagem das moedas
        self.label_moeda = tk.Label(self.tabuleiro, text = 'Moedas')
        self.label_moeda.grid(row=0, column=1,sticky='w')

#Botão para ir à loja
        self.botao_loja = tk.Button(self.tabuleiro, text = 'LOJA', height = 3, width = 30, bg = 'purple')
        self.botao_loja.configure(command = self.abrir_janela)        
        self.botao_loja.grid(row=0, column=2, columnspan=2)
        
#Botões de jogo     
        self.botao1 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao1.configure(command = self.click1)
        self.botao1.grid(row=1, column=0)
        
        self.botao2 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao2.configure(command = self.click2)
        self.botao2.grid(row=1, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao3.configure(command = self.click3)
        self.botao3.grid(row=1, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao4.configure(command = self.click4)
        self.botao4.grid(row=1, column=3)
        
        self.botao5 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao5.configure(command = self.click5)
        self.botao5.grid(row=2, column=0)
        
        self.botao6 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao6.configure(command = self.click6)
        self.botao6.grid(row=2, column=1)
        
        self.botao7 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao7.configure(command = self.click7)
        self.botao7.grid(row=2, column=2)
        
        self.botao8 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao8.configure(command = self.click8)
        self.botao8.grid(row=2, column=3)
        
        self.botao9 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao9.configure(command = self.click9)
        self.botao9.grid(row=3, column=0)
        
        self.botao10 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao10.configure(command = self.click10)
        self.botao10.grid(row=3, column=1)
        
        self.botao11 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao11.configure(command = self.click11)
        self.botao11.grid(row=3, column=2)
        
        self.botao12 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao12.configure(command = self.click12)
        self.botao12.grid(row=3, column=3)
        
        self.botao13 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao13.configure(command = self.click13)
        self.botao13.grid(row=4, column=0)
        
        self.botao14 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao14.configure(command = self.click14)
        self.botao14.grid(row=4, column=1)
        
        self.botao15 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao15.configure(command = self.click15)
        self.botao15.grid(row=4, column=2)
        
        self.botao16 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao16.configure(command = self.click16)
        self.botao16.grid(row=4, column=3)
        
    def click1(self):
        self.jogo.recebe_jogada(0,0)
        print(self.jogo.Lista_Jogada)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click2(self):
        self.jogo.recebe_jogada(0,1)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()        
        
    def click3(self):
        self.jogo.recebe_jogada(0,2)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click4(self):
        self.jogo.recebe_jogada(0,3)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click5(self):
        self.jogo.recebe_jogada(1,0)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()        
        
    def click6(self):
        self.jogo.recebe_jogada(1,1)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click7(self):
        self.jogo.recebe_jogada(1,2)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()        
        
    def click8(self):
        self.jogo.recebe_jogada(1,3)
        self.jogo.verifica_jogada()     
        self.jogo.virifica_fim()
        
    def click9(self):
        self.jogo.recebe_jogada(2,0)
        self.jogo.verifica_jogada() 
        self.jogo.virifica_fim()
    
    def click10(self):
        self.jogo.recebe_jogada(2,1)
        self.jogo.verifica_jogada() 
        self.jogo.virifica_fim()
        
    def click11(self):
        self.jogo.recebe_jogada(2,2)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click12(self):
        self.jogo.recebe_jogada(2,3)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click13(self):
        self.jogo.recebe_jogada(3,0)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click14(self):
        self.jogo.recebe_jogada(3,1)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click15(self):
        self.jogo.recebe_jogada(3,2)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
        
    def click16(self):
        self.jogo.recebe_jogada(3,3)
        self.jogo.verifica_jogada()
        self.jogo.virifica_fim()
           
    def abrir_loja(self):
        self.lojinha = Loja()
        self.lojinha.iniciar()        
        
    def iniciar(self):
        self.tabuleiro.geometry('440x460')
        self.tabuleiro.mainloop()  
        
        

                