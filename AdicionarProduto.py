from tkinter import *
from Banco import *

def add(event):
    nome = app.nomeEntry.get()
    preço = app.preçoEntry.get()

    try:
        float(preço)
        Banco.addProduto(Banco, nome, preço)
        app.window.destroy()
        Exito(app.pai, True)
    except ValueError:
        Exito(app.window, False)


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

        self.window.title("Adicionar Produto")
        self.window.resizable(0,0)
        self.window.geometry("300x100")
        self.window.mainloop()

class Exito:

    def __init__(self, window, status):
        self.window = Toplevel(window)

        if status:
            self.statusLabel = Label(self.window, text="Produto adicionado com exito!")
            self.statusLabel.pack()
        else:
            self.statusLabel = Label(self.window, text="Erro ao adicionar produto!")
            self.statusLabel.pack()

        self.okButton = Button(self.window, text="Ok", command=self.okButtonCommand)
        self.okButton.pack(pady=5, ipadx=30)

        self.window.title("Status")
        self.window.resizable(0,0)
        self.window.geometry("200x60")
        self.window.mainloop()

    def okButtonCommand(self):
        self.window.destroy()

app = AdicionarProduto
