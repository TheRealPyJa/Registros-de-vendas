from tkinter import *
from Banco import *

class TabelaProdutos:

    def __init__(self, pai):
        self.window = Toplevel(pai)

        self.dadosLabelFrame = Frame(self.window)
        self.dadosLabelFrame.pack(anchor=W)

        self.produtosFrame = Frame(self.window)
        self.produtosFrame.pack(anchor=W)

        self.dadosLabel = Label(self.dadosLabelFrame, text="Id                                     |Nome                             |Preço                               |Criado                            |Modificado    ")
        self.dadosLabel.pack(anchor=W)

        self.produtos = Banco.recuperaProdutos(Banco)

        self.mostraProdutos(self)

        larguraJanela = 700
        alturaJanela = 600

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Produtos")
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.mainloop()


    def mostraProdutos(self):
        for produto in self.produtos:
            produtoIdEntry = Entry(self.produtosFrame)
            produtoIdEntry.insert(0, str(produto[0]))
            produtoIdEntry.config(state='readonly')
            produtoIdEntry.grid(row=self.produtos.index(produto), column=0)

            produtoNomeEntry = Entry(self.produtosFrame)
            produtoNomeEntry.insert(0, str(produto[1]))
            produtoNomeEntry.config(state='readonly')
            produtoNomeEntry.grid(row=self.produtos.index(produto), column=1)

            produtoPreçoEntry = Entry(self.produtosFrame)
            produtoPreçoEntry.insert(0, "R$                           " + str(float(produto[2])))
            produtoPreçoEntry.config(state='readonly')
            produtoPreçoEntry.grid(row=self.produtos.index(produto), column=2)

            produtoCriadoEntry = Entry(self.produtosFrame)
            produtoCriadoEntry.insert(0, self.retornaData(self, produto[0]))
            produtoCriadoEntry.config(state='readonly')
            produtoCriadoEntry.grid(row=self.produtos.index(produto), column=3)

            produtoModificadoEntry = Entry(self.produtosFrame)
            produtoModificadoEntry.insert(0, str(produto[3]))
            produtoModificadoEntry.config(state='readonly')
            produtoModificadoEntry.grid(row=self.produtos.index(produto), column=4)

    def retornaData(self, id):
        id = str(id)
        return id[0:2] + "/" + id[2:4] + "/" + id[4:8]