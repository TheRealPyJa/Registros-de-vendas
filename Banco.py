import sqlite3
from datetime import  datetime

class Banco:

    def __init__(self):
        self.alo = 2

    def criar(self):
        try:
            conexao = sqlite3.connect("Registros.db")

            criarTables = """CREATE TABLE Produtos (
                                
                                id INTEGER NOT NULL,
                                nome TEXT NOT NULL,
                                preço INTEGER NOT NULL,
                                modificaçao TEXT NOT NULL);"""

            cursor = conexao.cursor()
            cursor.execute(criarTables)
            cursor.close()

            conexao.commit()

        except sqlite3.Error as error:
            print("Erro ao criar tabela: ", error)
        finally:
            conexao.close()

    def addProduto(self, nome, preço):
        try:
            conexao = sqlite3.connect("Registros.db")

            adicionarProdutosQuery = """INSERT INTO Produtos (id, nome, preço, modificaçao) VALUES (?,?,?,?);"""

            id = datetime.now().strftime("%d%m%Y%H%M%S")
            modificaçao = datetime.now().strftime("%d/%m/%Y")

            dados = (id, nome, preço, modificaçao)

            cursor = conexao.cursor()
            cursor.execute(adicionarProdutosQuery, dados)
            cursor.close()

            conexao.commit()

        except sqlite3.Error as error:
            print("Erro ao adicionar Produto: ", error)
        finally:
            conexao.close()