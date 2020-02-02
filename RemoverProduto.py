from tkinter import *
from tkinter.ttk import *
from Banco import *

def remover(event):
    produto = app.produtosCombo.get()
    Banco.deletaProduto(Banco, produto)

class RemoverProduto:

    def preencheCombo(self):
        produtos = Banco.recuperaProdutos(Banco)
        produtosNome = []
        for produto in produtos:
             produtosNome.append(produto[1])
        self.produtosCombo["values"] = tuple(produtosNome)

    def __init__(self, window):

        self.window = Toplevel(window)

        self.produtosCombo = Combobox(self.window, state="readonly")
        self.preencheCombo(RemoverProduto)
        self.produtosCombo.current(0)
        self.produtosCombo.grid(row=0, column=1)

        self.produtoLabel = Label(self.window, text="Produto:")
        self.produtoLabel.grid(row=0, column=0, padx=(30,0))

        self.removerButton = Button(self.window, text="Remover")
        self.removerButton.bind("<Button-1>", remover)
        self.removerButton.grid(row=1, column=1, pady=10)

        larguraJanela = 265
        alturaJanela = 60

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Remover produto")
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.mainloop()

app = RemoverProduto