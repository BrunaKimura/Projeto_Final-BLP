import tkinter as tk

from imagem_som import Imagens_sons

from Classe_Comprar import Compras

import tkinter.messagebox as tkm

class Loja():
    def __init__(self, login):
        self.login = login        
        self.loja = tk.Toplevel()
        self.loja.title("Jogo da Memória ANIMAL")
        self.loja.resizable ( 0 ,  0 )
        
        self.imagem = Imagens_sons()
        self.compras = Compras(login)
#Label com a imagem de um cifrão
        self.label_cifrao = tk.Label(self.loja, text = '$', font ='Arial')
        self.label_cifrao.grid(row=0, column=0)
        
#Label da contagem das moedas
        self.label_moeda = tk.Label(self.loja, text = self.compras.cofre)
        self.label_moeda.grid(row=0, column=1, sticky ='w')   
        
#Botão para voltar ao jogo
        self.botao_voltar = tk.Button(self.loja, text = 'Voltar', height = 3, width = 8, bg = 'orange')
        self.botao_voltar.configure(command = self.fechar_janela)
        self.botao_voltar.grid(row=0, column=2, columnspan=2)
        
#Label para ajustar os espaçamentos dos botões
        self.label_ajuste1 = tk.Label(self.loja, text = '')
        self.label_ajuste1.grid(row=1, column=0, columnspan=3)
        
        self.label_preco1 = tk.Label(self.loja, text = self.compras.preco)
        self.label_preco1.grid(row=3, column=0, columnspan=1 )
        
        self.label_preco2 = tk.Label(self.loja, text = self.compras.preco)
        self.label_preco2.grid(row=3, column=2, columnspan=1 )
        
        self.label_preco3 = tk.Label(self.loja, text = self.compras.preco)
        self.label_preco3.grid(row=5, column=0, columnspan=1 )
        
        self.label_preco4 = tk.Label(self.loja, text = self.compras.preco)
        self.label_preco4.grid(row=5, column=2, columnspan=1 )
                
#Botões para comprar
        self.botao1 = tk.Button(self.loja, image = self.imagem.Ileao, height = 102, width = 95)
        self.botao1.configure(command = self.click1)
        self.botao1.grid(row=2, column=0 )
        
        
        self.botao2 = tk.Button(self.loja, image = self.imagem.Ipanda, height = 102, width = 95) 
        self.botao2.configure(command = self.click2)
        self.botao2.grid(row=2, column=2 )
        
        self.botao3 = tk.Button(self.loja, image = self.imagem.Igalo, height = 102, width = 95)
        self.botao3.configure(command = self.click3)        
        self.botao3.grid(row=4, column=0 )
        
        self.botao4 = tk.Button(self.loja, image = self.imagem.Ielefante, height = 102, width = 95)
        self.botao4.configure(command = self.click4)        
        self.botao4.grid(row=4, column=2 )
        
    def click1(self):
        if self.compras.comprar(0,0) == 1:
            self.botao1.configure(state = 'disabled') 
            
            self.label_preco1.configure(text = self.compras.preco)
            self.label_preco2.configure(text = self.compras.preco)
            self.label_preco3.configure(text = self.compras.preco)
            self.label_preco4.configure(text = self.compras.preco)
            
            self.label_moeda.configure(text = self.compras.cofre)
            tkm.showinfo(title = "Loja", message = "Você Efetuou Uma Compra")
            self.loja.destroy()
            
        else: 
            tkm.showinfo(title = "Loja", message = "Você Não Possui Dinheiro Suficiente")
            self.loja.destroy()
            
        
    def click2(self):
        if self.compras.comprar(0,1) == 1:
            self.botao2.configure(state = 'disabled')
                
            self.label_preco1.configure(text = self.compras.preco)
            self.label_preco2.configure(text = self.compras.preco)
            self.label_preco3.configure(text = self.compras.preco)
            self.label_preco4.configure(text = self.compras.preco)
            
            self.label_moeda.configure(text = self.compras.cofre)
            tkm.showinfo(title = "Loja", message = "Você Efetuou Uma Compra")
            self.loja.destroy()
            
        else: 
            tkm.showinfo(title = "Loja", message = "Você Não Possui Dinheiro Suficiente")
            self.loja.destroy()
        
    def click3(self):
        if self.compras.comprar(1,0) == 1:
            self.botao3.configure(state = 'disabled') 
            
            self.label_preco1.configure(text = self.compras.preco)
            self.label_preco2.configure(text = self.compras.preco)
            self.label_preco3.configure(text = self.compras.preco)
            self.label_preco4.configure(text = self.compras.preco)
            
            self.label_moeda.configure(text = self.compras.cofre)
            tkm.showinfo(title = "Loja", message = "Você Efetuou Uma Compra")
            self.loja.destroy()
            
        else: 
            tkm.showinfo(title = "Loja", message = "Você Não Possui Dinheiro Suficiente")
            self.loja.destroy()
        
    def click4(self):
        if self.compras.comprar(1,1) == 1:
            self.botao4.configure(state = 'disabled')  
            
            self.label_preco1.configure(text = self.compras.preco)
            self.label_preco2.configure(text = self.compras.preco)
            self.label_preco3.configure(text = self.compras.preco)
            self.label_preco4.configure(text = self.compras.preco)
            
            self.label_moeda.configure(text = self.compras.cofre)
            tkm.showinfo(title = "Loja", message = "Você Efetuou Uma Compra")
            self.loja.destroy()
            
        else: 
            tkm.showinfo(title = "Loja", message = "Você Não Possui Dinheiro Suficiente")
            self.loja.destroy()
    
        
    def fechar_janela(self):
        self.loja.destroy()      
        
        
    def iniciar(self):
        self.loja.geometry('220x340')
        self.loja.mainloop()
