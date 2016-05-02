# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:50:26 2016

@author: Lucas
"""

import tkinter as tk

class Tabuleiro(): 
    def __init__(self):
        self.tabuleiro = tk.Tk()
        self.tabuleiro.title("Jogo da Memória ANIMAL")
        
#Botões de jogo     
        self.botao1 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao1.grid(row=1, column=0)
        
        self.botao2 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao2.grid(row=1, column=1)
        
        self.botao3 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao3.grid(row=1, column=2)
        
        self.botao4 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao4.grid(row=1, column=3)
        
        self.botao5 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao5.grid(row=2, column=0)
        
        self.botao6 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao6.grid(row=2, column=1)
        
        self.botao7 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao7.grid(row=2, column=2)
        
        self.botao8 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao8.grid(row=2, column=3)
        
        self.botao9 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao9.grid(row=3, column=0)
        
        self.botao10 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao10.grid(row=3, column=1)
        
        self.botao11 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao11.grid(row=3, column=2)
        
        self.botao12 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao12.grid(row=3, column=3)
        
        self.botao13 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao13.grid(row=4, column=0)
        
        self.botao14 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao14.grid(row=4, column=1)
        
        self.botao15 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao15.grid(row=4, column=2)
        
        self.botao16 = tk.Button(self.tabuleiro, height = 6, width = 14)
        self.botao16.grid(row=4, column=3)
        
        
    def iniciar(self):
        self.tabuleiro.geometry('600x600')
        self.tabuleiro.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
memoria = Tabuleiro()
memoria.iniciar()
