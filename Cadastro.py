import tkinter as tk

from Classe_Cadastrar import cadastrar

import tkinter.messagebox as tkm

from imagem_som import Imagens_sons

class Cadastro():
    def __init__(self):
        self.cadastro = tk.Toplevel()
        self.cadastro.title('Jogo da Memória ANIMAL')
        
        
        self.objeto_cadastro = cadastrar()
        
        self.imagem = Imagens_sons()
        
        self.label_fundo = tk.Label(self.cadastro, image = self.imagem.Icadastro)
        self.label_fundo.place(x = 0, y = 0)
               
    
        
#Local onde coloca o login a ser criado
        self.label_login = tk.Label(self.cadastro, text = 'Login:', bg = 'red')
        self.label_login.grid(row=0, column=0, )
        
        self.entry_login = tk.Entry(self.cadastro)
        self.entry_login.grid(row=1, column=0)
        
#Local onde coloca a senha a ser criada
        self.label_senha = tk.Label(self.cadastro, text = 'Senha:', bg = 'red')
        self.label_senha.grid(row=2, column=0, )
        
        self.entry_senha = tk.Entry(self.cadastro)
        self.entry_senha.grid(row=3, column=0)
        
#Local onde coloca o sexo do usuário
        self.label_sexo = tk.Label(self.cadastro, text = 'Sexo:', bg = 'red')
        self.label_sexo.grid(row=4, column=0, )        
        
        self.entry_sexo = tk.Entry(self.cadastro)
        self.entry_sexo.grid(row =5, column=0)
        
#Local onde coloca a idade do usuário
        self.label_idade = tk.Label(self.cadastro, text = 'Idade:', bg = 'red')
        self.label_idade.grid(row=7, column=0, )
        
        self.entry_idade = tk.Entry(self.cadastro)
        self.entry_idade.grid(row=8, )
        
        self.label_ajuste = tk.Label(self.cadastro, bg = 'green')
        self.label_ajuste.grid(row=9)
        
#botao que termina o cadastro
        self.botao_finalizar = tk.Button(self.cadastro, text = 'Finalizar', bg = 'yellow')
        self.botao_finalizar.configure(command = self.Cadastrar)
        self.botao_finalizar.grid(row=10, sticky=tk.W+tk.E+tk.S+tk.N)
        
    
        
    def Cadastrar(self):
        if self.objeto_cadastro.adicionar_cadastro(self.entry_login.get(), self.entry_senha.get(), self.entry_sexo.get(), self.entry_idade.get()) == 1:
            tkm.showinfo(title = "Login", message = "Você Foi Cadastrado")
            self.cadastro.destroy()            
            
        elif self.objeto_cadastro.adicionar_cadastro(self.entry_login.get(), self.entry_senha.get(), self.entry_sexo.get(), self.entry_idade.get()) == -1:
            tkm.showinfo(title = "Login", message = "O Usuário Já Existe")
                       
        elif self.objeto_cadastro.adicionar_cadastro(self.entry_login.get(), self.entry_senha.get(), self.entry_sexo.get(), self.entry_idade.get()) == 0:
            tkm.showinfo(title = "Login", message = "Informe o sexo corretamente. Use 'M' para masculino e 'F' para feminino.")
          
    def iniciar(self):
        self.cadastro.geometry('190x230')
        self.cadastro.mainloop()
        
