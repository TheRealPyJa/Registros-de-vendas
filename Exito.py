from tkinter import *


def okButtonCommand():
    app.window.destroy()

class Exito:

    def __init__(self, window, mensagem):
        self.window = Toplevel(window)

        self.statusLabel = Label(self.window, text=mensagem)
        self.statusLabel.pack()

        self.okButton = Button(self.window, text="Ok", command=okButtonCommand)
        self.okButton.pack(pady=5, ipadx=30)

        larguraJanela = 200
        alturaJanela = 60

        largura = self.window.winfo_screenwidth()
        altura = self.window.winfo_screenheight()

        distanciaLateral = int((largura / 2) - (larguraJanela / 2))
        distanciaSuperior = int((altura / 2) - (alturaJanela / 2))

        self.window.title("Status")
        self.window.resizable(0,0)
        self.window.geometry("{}x{}+{}+{}".format(larguraJanela, alturaJanela, distanciaLateral, distanciaSuperior))
        self.window.mainloop()

app = Exito