# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:26:58 2016

@author: Lucas
"""
import tkinter as tk

class Cadastro():
    def __init__(self):
        self.cadastro = tk.Tk()
        self.cadastro.title('Jogo da Memória ANIMAL')
        
#Local onde coloca o login a ser criado
        self.label_login = tk.Label(self.cadastro, text = 'Login:')
        self.label_login.grid(row=0, column=0, sticky='w')
        
        self.entry_login = tk.Entry(self.cadastro)
        self.entry_login.grid(row=1, column=0)
        
#Local onde coloca a senha a ser criada
        self.label_senha = tk.Label(self.cadastro, text = 'Senha:')
        self.label_senha.grid(row=2, column=0, sticky='w')
        
        self.entry_senha = tk.Entry(self.cadastro)
        self.entry_senha.grid(row=3, column=0)
        
#Local onde coloca o sexo do usuário
        self.label_sexo = tk.Label(self.cadastro, text = 'Sexo:')
        self.label_sexo.grid(row=4, column=0, sticky='w')        
        
        self.botao_masculino = tk.Button(self.cadastro, text = 'Masculino', bg = 'blue')
        self.botao_masculino.grid(row=5, column=0, sticky='w')
        
        self.botao_feminino = tk.Button(self.cadastro, text = 'Feminino', bg = 'red')
        self.botao_feminino.grid(row=5, column=0, sticky='e')
        
#Local onde coloca a idade do usuário
        self.label_idade = tk.Label(self.cadastro, text = 'Idade:')
        self.label_idade.grid(row=7, column=0, sticky='w')
        
        self.entry_idade = tk.Entry(self.cadastro)
        self.entry_idade.grid(row=8, sticky='w')
        
#botao que termina o cadastro
        self.botao_finalizar = tk.Button(self.cadastro, text = 'Finalizar', bg = 'yellow')
        self.botao_finalizar.grid(row=9)
                

        
    def iniciar(self):
        self.cadastro.geometry('190x230')
        self.cadastro.mainloop()
        

    