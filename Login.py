from tkinter import *
from Principal import *

def entrar(event):
    arquivo = open("Login.txt", 'r')
    linhas = arquivo.readlines()
    arquivo.close()
    login = str(loginWindow.usuario.get())
    senha = str(loginWindow.senha.get())
    if login == linhas[0].split(" ")[1].split("\n")[0] and senha == linhas[1].split(" ")[1]:
        loginWindow.window.destroy()
        principalJanela = Principal
        principalJanela.__init__(principalJanela)

def modificar(event):
    if app.usuario.get() == "NadiaMaria" and app.senha.get() == "21020320":
        arquivo = open("Login.txt", "w")
        arquivo.write("")
        arquivo.close()

class loginWindow:

    def __init__(self, window):
        self.window = window
        frame = Frame(self.window)
        frame.pack()

        self.nome = Label(frame, text="Usuario:")
        self.nome.grid_anchor(anchor=CENTER)
        self.nome.grid(row=0)

        self.usuario = Entry(frame)
        self.usuario.grid_anchor(anchor=CENTER)
        self.usuario.grid(row=0, column=1)

        self.senhaLabel = Label(frame, text="Senha:")
        self.senhaLabel.grid_anchor(anchor=CENTER)
        self.senhaLabel.grid(row=1, sticky=W)

        self.senha = Entry(frame, show="*")
        self.senha.grid_anchor(anchor=CENTER)
        self.senha.grid(row=1, column=1)

        self.entra = Button(frame, text="Entrar")
        self.entra.bind("<Button-1>", entrar)
        self.entra.bind("<Button-3>", modificar)
        self.entra.grid(row=3, column=1)

        self.window.title("Login")
        self.window.resizable(0,0)
        self.window.geometry("200x80")
        self.window.mainloop()

janela = Tk()

app = loginWindow
app.__init__(app, janela)