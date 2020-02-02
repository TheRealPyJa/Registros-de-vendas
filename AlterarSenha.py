from tkinter import *
from Exito import *

def alterarSenha(event):
    arq = open("Login.config", "w")
    arq.write("Login: " + app.novoUsuarioEntry.get() + "\nSenha: " + app.novaSenhaEntry.get())
    arq.close()
    app.window.destroy()
    exitoJanela = Exito
    exitoJanela.__init__(exitoJanela, app.pai, "Senha alterada com sucesso")

class AlterarSenha:

    def __init__(self, window):
        self.window = Toplevel(window)
        self.pai = window

        self.novoUsuarioLabel = Label(self.window, text="Novo usuário:")
        self.novoUsuarioLabel.grid(row=0, column=0, sticky=W, padx=(20,0), pady=3)

        self.novaSenhaLabel = Label(self.window, text="Nova senha:")
        self.novaSenhaLabel.grid(row=1, column=0, sticky=W, padx=(20,0), pady=3)

        self.novoUsuarioEntry = Entry(self.window)
        self.novoUsuarioEntry.grid(row=0, column=1)

        self.novaSenhaEntry = Entry(self.window)
        self.novaSenhaEntry.grid(row=1, column=1)

        self.alterarSenhaButton = Button(self.window, text="Alterar senha")
        self.alterarSenhaButton.bind("<Button-1>", alterarSenha)
        self.alterarSenhaButton.grid(row=2, column=1)

        larguraJanela = 250
        alturaJanela = 85

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Alterar Senha")
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.resizable(0,0)
        self.window.mainloop()

app = AlterarSenha