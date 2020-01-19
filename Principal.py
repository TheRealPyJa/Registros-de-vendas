from tkinter import *
from Adicionar import *
from AdicionarProduto import *

def adicionar(event):
    adicionarProdutoJanela = AdicionarProduto
    adicionarProdutoJanela.__init__(adicionarProdutoJanela, app.window)

class Principal:

    def __init__(self):
        self.window = Tk()

        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT)

        self.frameButtons = Frame(self.window)
        self.frameButtons.pack(side=RIGHT, anchor=W)

        self.dataLabel = Label(self.frame, text="Data                         |    Produto1     |    Produto2    |   Produto3   |"
                                                "     Produto4     |     Total     |     Valor")
        self.dataLabel.pack(anchor=W)

        self.tabela = Text(self.frame, width=65)
        self.tabela.insert(INSERT, "02/01/2020      10        5         8")
        self.tabela.insert(INSERT, "\n03/01/2020      2         4         12")
        self.tabela["state"] = "disabled"
        self.tabela.pack()

        self.adicionarProdutoButton = Button(self.frameButtons, text="Adicionar Produto")
        self.adicionarProdutoButton.bind("<Button-1>", adicionar)
        self.adicionarProdutoButton.grid(row=0, column=0, sticky=NW)

        self.window.title("Historico")
        self.window.geometry("700x400")
        self.window.resizable(0,0)
        self.window.mainloop()

app = Principal
