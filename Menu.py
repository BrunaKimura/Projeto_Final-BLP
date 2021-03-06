from Classe_Firebase import Firebase

import tkinter as tk

from Interface import Tabuleiro

from Cadastro import Cadastro

from Classe_Logar import Login

import tkinter.messagebox as tkm


from imagem_som import Imagens_sons
 


class Menu():
    def __init__(self, login, lista):
        self.login= login
        self.lista= lista
        self.firebase=Firebase()
        self.menu = tk.Tk()
        self.menu.title("Jogo da Memória ANIMAL")
        self.menu.resizable ( 0 ,  0 )
               
        self.Login = Login(login, lista)
        
        self.imagem = Imagens_sons()
        
        self.label_fundo = tk.Label(self.menu, image = self.imagem.Imenu)
        self.label_fundo.place(x = 0, y = 0)
        
#Label de boas vindas
        self.label1 = tk.Label(self.menu, text = 'Bem Vindo !!', bg = 'pink')
        self.label1.grid(row=0, column=0)
        
#Label de ajustes 
        self.label_ajuste1 = tk.Label(self.menu, text = '')
        self.label_ajuste1.grid(row=1, column=0)
        
        self.label_ajuste2 = tk.Label(self.menu, text = '')
        self.label_ajuste2.grid(row=7, column=0)
             
#Parte para colocar o login do usuário    
        self.label_login = tk.Label(self.menu, text = 'Login:', bg = 'pink')
        self.label_login.grid(row=2, column=0)
        
        self.entry_login = tk.Entry(self.menu)
        self.entry_login.grid(row=3, column=0)
        
#Parte para colocar a senha
        self.label_senha = tk.Label(self.menu, text = 'Senha:', bg = 'pink')
        self.label_senha.grid(row=4, column=0)
        
        self.entry_senha = tk.Entry(self.menu)
        self.entry_senha.grid(row=5, column=0)
        
#Botao para iniciar o jogo
        self.botao_jogar = tk.Button(self.menu, text = 'Jogar', bg = 'brown', )
        self.botao_jogar.configure(command = self.verificar_login)
        self.botao_jogar.grid(row=6, column=0)
        
#Botao que leva o usuario ao cadastro
        self.label_cadastrar = tk.Label(self.menu, text = 'Não possui um cadastro ainda ? ', bg = 'pink')
        self.label_cadastrar.grid(row=8, column=0)
        
        self.botao_cadastrar = tk.Button(self.menu, text = 'Cadastrar', bg = 'gray')
        self.botao_cadastrar.configure(command = self.abrir_cadastro)
        self.botao_cadastrar.grid(row=9, column=0)
        
        
    def verificar_login(self):
        self.login = self.entry_login.get()
        self.senha = self.entry_senha.get()
        
        if self.Login.verifica(self.login, self.senha) == 0:
            tkm.showinfo(title = "Login", message = "O Usuário Não Existe")
            

        elif self.Login.verifica(self.login, self.senha) == -1:
            tkm.showinfo(title = "Login", message = "Senha Incorreta")
            
        
        elif self.Login.verifica(self.login, self.senha) == 1:
            self.abrir_jogo()      
            self.lista=self.firebase.Animais(self.login)
        
        
    def abrir_jogo(self):
        self.lista=self.firebase.Animais(self.login)
        self.menu.destroy()
        self.joguinho = Tabuleiro(self.login, self.lista)
        self.joguinho.iniciar() 
                   
    def abrir_cadastro(self):
        self.cadastrinho = Cadastro()
        self.cadastrinho.iniciar()
                
    def iniciar(self):
        self.menu.geometry('180x230')
        self.menu.mainloop()
        
entrada = Menu("start", [])
entrada.iniciar()
    