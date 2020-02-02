from tkinter import *
from Banco import *
from Exito import *

def fecharDia(event):
    quant = []
    for quantidade in app.quantidadeEntry:
        quantidadeGet = quantidade.get()
        if quantidadeGet.isdigit():
            quant.append(int(quantidade.get()))
        else:
            exitoTela = Exito
            exitoTela.__init__(exitoTela, app.pai, "Erro ao fechar dia")
    Banco.fechaDia(Banco, quant)
    app.window.destroy()
    exitoTela = Exito
    exitoTela.__init__(exitoTela, app.pai, "Dia fechado com sucesso")

class AdicionaDia:

    def __init__(self, pai):
        self.window = Toplevel(pai)
        self.pai = pai

        self.produtosLabel = Label(self.window, text="Produtos")
        self.produtosLabel.grid(row=0, column=0)

        self.quantidadeLabel = Label(self.window, text="Quantidade")
        self.quantidadeLabel.grid(row=0, column=1)

        self.produtos = Banco.recuperaProdutos(Banco)
        self.adicionaNomes(self)

        self.quantidadeEntry = []
        self.adicionaQuantidadeEntry(self)

        self.salvarButton = Button(self.window, text="Salvar")
        self.salvarButton.bind("<Button-1>", fecharDia)
        self.salvarButton.grid(row=60, column=1)

        larguraJanela = 200
        alturaJanela = 60

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Fechar dia")
        self.window.geometry("+{}+{}".format(distanciaLateral, distanciaSuperior))
        self.window.resizable(0,0)
        self.window.mainloop()

    def adicionaNomes(self):
        for produto in self.produtos:
            nome = Entry(self.window)
            nome.insert(0, produto[1])
            nome.config(state='readonly')
            nome.grid(row=self.produtos.index(produto) + 1, column=0)

    def adicionaQuantidadeEntry(self):
        for produto in self.produtos:
            quantidadeEntry = Entry(self.window)
            quantidadeEntry.grid(row=self.produtos.index(produto) + 1, column=1)
            self.quantidadeEntry.append(quantidadeEntry)

app = AdicionaDia