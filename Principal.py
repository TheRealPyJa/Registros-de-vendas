from tkinter import *
from tkinter.ttk import *
from AdicionarProduto import *
from AdicionaDia import *
from TabelaProdutos import *
from RemoverProduto import *

def adicionarDia(event):
    adicionarDiaJanela = AdicionaDia
    adicionarDiaJanela.__init__(adicionarDiaJanela, app.window)

def adicionarProduto(event):
    adicionarProdutoJanela = AdicionarProduto
    adicionarProdutoJanela.__init__(adicionarProdutoJanela, app.window)

def mostrarTabela(event):
    mostrarTabelaJanela = TabelaProdutos
    mostrarTabelaJanela.__init__(mostrarTabelaJanela, app.window)

def removerProduto(event):
    removerProdutoJanela = RemoverProduto
    removerProdutoJanela.__init__(removerProdutoJanela, app.window)

def preencheCombo():
    dias = Banco.recuperaDias(Banco)
    dataArray = []
    if not dias:
        app.dataCombo["values"] = "Sem-registros"
    else:
        for i in range(1, len(dias)):
            data = dias[i][0].split("a")[1]
            dia = "{}/{}/{}".format(data[0:2], data[2:4], data[4:])
            dataArray.append(dia)
        app.dataCombo["values"] = tuple(dataArray)

def preencheTabela(event=None):

    if app.dataCombo.get() == "Sem-registros":
        return
    produtos = Banco.recuperaProdutos(Banco)
    dia = app.dataCombo.get().split("/")
    data = "{}{}{}".format(dia[0], dia[1], dia[2])
    registros = Banco.recuperaRegistros(Banco, data)

    app.tabela["state"]="normal"

    app.tabela.delete(1.0, END)

    if  registros:
        for registro in registros:

            linha = []
            produto = registro[0]
            total = registro[1]
            valor = registro[2]

            for i in range(55):
                linha.append(" ")
            for i in range(len(produto)):
                linha[i] = produto[i]
            for i in range(44, 44 + len(total)):
                linha[i] = total[i-44]
            for i in range(54, 54 + len(str(valor))):
                linha[i - len(valor)] = valor[i - 54]

            for char in linha:
                app.tabela.insert(INSERT, char)

        total = 0
        valor = 0
        totalStr = "Total"
        linha = []

        for registro in registros:
            total += int(registro[1])
            valor += float(registro[2])

        total = str(total)
        valor = str(valor)

        for i in range(55):
            linha.append(" ")
        for i in range(len(totalStr)):
            linha[i] = totalStr[i]
        for i in range(44, 44 + len(total)):
            linha[i] = total[i - 44]
        for i in range(54, 54 + len(valor)):
            linha[i - len(valor)] = valor[i-54]
        for char in linha:
            app.tabela.insert(INSERT, char)

    app.tabela["state"]="disabled"


class Principal:

    def __init__(self):
        self.window = Tk()

        self.frame = Frame(self.window)
        self.frame.grid(row=0, column=0)

        self.labelComboFrame = Frame(self.frame)
        self.labelComboFrame.pack(anchor=W)

        self.frameButtons = Frame(self.window)
        self.frameButtons.grid(row=0, column=1, padx=30, pady=30,sticky=N)

        self.dataLabel = Label(self.labelComboFrame, text="                                                                                     Total     |     Valor")
        self.dataLabel.grid(row=0, column=1, sticky=NW)

        self.dataCombo = Combobox(self.labelComboFrame, state="readonly", width=11, postcommand=preencheCombo)
        preencheCombo()
        self.dataCombo.current(0)
        self.dataCombo.grid(row=0, column=0)

        self.tabela = Text(self.frame, width=55)
        self.tabela["state"] = "disabled"
        preencheTabela()
        self.tabela.pack(anchor=W)

        self.dataCombo.bind("<<ComboboxSelected>>", preencheTabela)

        self.adicionaDiaButton = Button(self.frameButtons, text="Fechar dia")
        self.adicionaDiaButton.bind("<Button-1>", adicionarDia)
        self.adicionaDiaButton.grid(row=0, column=0, ipadx=20)

        self.adicionarProdutoButton = Button(self.frameButtons, text="Adicionar Produto")
        self.adicionarProdutoButton.bind("<Button-1>", adicionarProduto)
        self.adicionarProdutoButton.grid(row=1, column=0, ipadx=2, pady=(25,25))

        self.removerProdutoButton = Button(self.frameButtons, text="Remover produto")
        self.removerProdutoButton.bind("<Button-1>", removerProduto)
        self.removerProdutoButton.grid(row=2, column=0, ipadx=5, pady=(0,25))

        self.tabelaProdutosButton = Button(self.frameButtons, text="Tabela de produtos")
        self.tabelaProdutosButton.bind("<Button-1>", mostrarTabela)
        self.tabelaProdutosButton.grid(row=3, column=0)

        larguraJanela = 700
        alturaJanela = 400

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Historico")
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.resizable(0,0)
        self.window.mainloop()

app = Principal
