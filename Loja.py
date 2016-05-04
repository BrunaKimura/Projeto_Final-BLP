# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:22:39 2016

@author: Lucas
"""
import tkinter as tk

class Loja():
    def __init__(self):
        self.loja = tk.Tk()
        self.loja.title("Jogo da Memória ANIMAL")
        
#Label com a imagem de um cifrão
        self.label_cifrao = tk.Label(self.loja, text = '$')
        self.label_cifrao.grid(row=0, column=0)
        
#Label da contagem das moedas
        self.label_moeda = tk.Label(self.loja, text = 'Moedas')
        self.label_moeda.grid(row=0, column=1, sticky ='w')   
        
#Botão para voltar ao jogo
        self.botao_voltar = tk.Button(self.loja, text = 'Voltar', height = 3, width = 8, bg = 'orange')
        self.botao_voltar.grid(row=0, column=2, columnspan=2)
        
#Label para ajustar os espaçamentos dos botões
        self.label_ajuste1 = tk.Label(self.loja, text = '')
        self.label_ajuste1.grid(row=1, column=0, columnspan=3)
        
        self.label_ajuste2 = tk.Label(self.loja, text = '')
        self.label_ajuste2.grid(row=3, column=0, columnspan=3 )
                
#Botões para comprar
        self.botao1 = tk.Button(self.loja, height = 8, width = 16)
        self.botao1.grid(row=2, column=0 )
        
        self.botao2 = tk.Button(self.loja, height = 8, width = 16)
        self.botao2.grid(row=2, column=2 )
        
        self.botao3 = tk.Button(self.loja, height = 8, width = 16)
        self.botao3.grid(row=4, column=0 )
        
        self.botao4 = tk.Button(self.loja, height = 8, width = 16)
        self.botao4.grid(row=4, column=2 )
        

        
        
        
        
        
        
    def iniciar(self):
        self.loja.geometry('294x364')
        self.loja.mainloop()
        
