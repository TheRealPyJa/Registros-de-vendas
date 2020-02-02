from tkinter import *
from Banco import *
from Exito import *

def add(event):
    nome = app.nomeEntry.get()
    preço = app.preçoEntry.get()

    try:
        float(preço)
        Banco.addProduto(Banco, nome, preço)
        app.window.destroy()
        exitoTela = Exito
        exitoTela.__init__(exitoTela, app.pai, "Produto adicionado com sucesso!")
    except ValueError:
        exitoTela = Exito
        exitoTela.__init__(exitoTela, app.pai, "Erro ao adicionar produto!")


class AdicionarProduto:

    def __init__(self, window):
        self.pai = window
        self.window = Toplevel(window)

        self.frame = Frame(self.window)
        self.frame.pack(anchor=NW)

        self.nomeLabel = Label(self.frame, text="Nome:")
        self.nomeLabel.grid(row=0, column=0, sticky=NW)

        self.preçoLabel = Label(self.frame, text="Preço:")
        self.preçoLabel.grid(row=1, column=0, pady=3, sticky=NW)

        self.nomeEntry = Entry(self.frame)
        self.nomeEntry.grid(row=0, column=1, sticky=NW)

        self.preçoEntry = Entry(self.frame)
        self.preçoEntry.grid(row=1, column=1, pady=3, sticky=NW)

        self.adicionarButton = Button(self.frame, text="Adicionar")
        self.adicionarButton.bind("<Button-1>", add)
        self.adicionarButton.grid(row=2, column=1, pady=10)

        larguraJanela = 300
        alturaJanela = 100

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Adicionar Produto")
        self.window.resizable(0,0)
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.mainloop()

app = AdicionarProduto
