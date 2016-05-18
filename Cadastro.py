import tkinter as tk

from Classe_Cadastrar import cadastrar


import tkinter.messagebox as tkm

class Cadastro():
    def __init__(self):
        self.cadastro = tk.Tk()
        self.cadastro.title('Jogo da Memória ANIMAL')
        
        self.objeto_cadastro = cadastrar()
        
        
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
        
        self.entry_sexo = tk.Entry(self.cadastro)
        self.entry_sexo.grid(row =5, column=0)
        
#Local onde coloca a idade do usuário
        self.label_idade = tk.Label(self.cadastro, text = 'Idade:')
        self.label_idade.grid(row=7, column=0, sticky='w')
        
        self.entry_idade = tk.Entry(self.cadastro)
        self.entry_idade.grid(row=8, sticky='w')
        
#botao que termina o cadastro
        self.botao_finalizar = tk.Button(self.cadastro, text = 'Finalizar', bg = 'yellow')
        self.botao_finalizar.configure(command = self.Cadastrar)
        self.botao_finalizar.grid(row=9)
        
    
        
    def Cadastrar(self):
        self.objeto_cadastro.adicionar_cadastro(self.entry_login.get(), self.entry_senha.get(), self.entry_sexo.get(), self.entry_idade.get())
        
        if self.objeto_cadastro.adicionar_cadastro(self.entry_login.get(), self.entry_senha.get(), self.entry_sexo.get(), self.entry_idade.get()) == 1:
            tkm.showinfo(title = "Login", message = "Você Foi Cadastrado")
            self.cadastro.destroy()            
            
        else:
            tkm.showinfo(title = "Login", message = "O Usuário Já Existe")
                       
        
        
    def iniciar(self):
        self.cadastro.geometry('190x230')
        self.cadastro.mainloop()
        

    