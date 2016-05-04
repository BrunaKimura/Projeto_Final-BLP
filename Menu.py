# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:29:25 2016

@author: Lucas
"""

import tkinter as tk

class Menu():
    def __init__(self):
        self.menu = tk.Tk()
        self.menu.title("Jogo da Memória ANIMAL")
        
        self.label1 = tk.Label(self.menu, text = 'Bem Vindo !!')
        self.label1.grid(row=0, column=0)
        
#Label de ajustes 
        self.label_ajuste1 = tk.Label(self.menu, text = '')
        self.label_ajuste1.grid(row=1, column=0)
        
        self.label_ajuste2 = tk.Label(self.menu, text = '')
        self.label_ajuste2.grid(row=7, column=0)
     
#Parte para colocar o login do usuário    
        self.label_login = tk.Label(self.menu, text = 'Login:')
        self.label_login.grid(row=2, column=0)
        
        self.entry_login = tk.Entry(self.menu)
        self.entry_login.grid(row=3, column=0)
        
#Parte para colocar a senha
        self.label_senha = tk.Label(self.menu, text = 'Senha:')
        self.label_senha.grid(row=4, column=0)
        
        self.entry_senha = tk.Entry(self.menu)
        self.entry_senha.grid(row=5, column=0)
        
#Botao para iniciar o jogo
        self.botao_jogar = tk.Button(self.menu, text = 'Jogar', bg = 'brown')
        self.botao_jogar.grid(row=6, column=0)
        
#Botao que leva o usuario ao cadastro
        self.label_cadastrar = tk.Label(self.menu, text = 'Não possui um cadastro ainda ? ')
        self.label_cadastrar.grid(row=8, column=0)
        
        self.botao_cadastrar = tk.Button(self.menu, text = 'Cadastrar', bg = 'gray')
        self.botao_cadastrar.grid(row=9, column=0)  
        
        
        
    def iniciar(self):
        self.menu.geometry('190x230')
        self.menu.mainloop()
        
entrada = Menu()
entrada.iniciar()
    