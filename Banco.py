import sqlite3
from datetime import  datetime

class Banco:

    def __init__(self):
        self.alo = 2

    def criar(self):
        try:
            conexao = sqlite3.connect("Registros.db")

            criarTables = """CREATE TABLE Registros (
                                
                                data TEXT NOT NULL,
                                total INTEGER NOT NULL,
                                valor INTEGER NOT NULL);"""

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
            adicionarColunaQuery = """ALTER TABLE Registros ADD """ + nome + """ INTEGER;"""

            id = datetime.now().strftime("%d%m%Y%H%M%S")
            modificaçao = datetime.now().strftime("%d/%m/%Y")

            dados = (id, nome, preço, modificaçao)

            cursor = conexao.cursor()
            cursor.execute(adicionarProdutosQuery, dados)
            cursor.execute(adicionarColunaQuery)
            cursor.close()

            conexao.commit()

        except sqlite3.OperationalError:
            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao adicionar Produto: ", error)
        finally:
            conexao.close()

    def recuperaProdutos(self):
        try:
            conexao = sqlite3.connect("Registros.db")

            recuperaProdutosQuery = """SELECT * FROM Produtos"""

            cursor = conexao.cursor()
            cursor.execute(recuperaProdutosQuery)
            produtos = cursor.fetchall()
            cursor.close()

            return produtos

        except sqlite3.Error as error:
            print("Falha ao recuperar produtos: ", error)
        finally:
            conexao.close()

    def deletaProduto(self, produto):
        try:
            conexao = sqlite3.connect("Registros.db")

            deletaProdutoQuery = """DELETE from Produtos where nome=?"""

            cursor = conexao.cursor()
            cursor.execute(deletaProdutoQuery, (produto,))
            cursor.close()

            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao excluir produto: ", error)
        finally:
            conexao.close()

    def organizaLista(self, lista1, lista2, lista3):

        indexs = []
        for i in range(len(lista1)):
            if not lista1[i] == lista2[i]:
                #print(lista1[i] + " não é igual a " + lista2[i])
                for item in lista2:
                    if item == lista1[i]:
                        #print(item + " é igual " + lista1[i])
                        indexs.append((i, lista2.index(item)))
                        #print(str(i) + " e " + str(lista2.index(item)) + " foram adicionados a indexs")
                        lista1[i], lista2[lista2.index(item)] = lista2[lista2.index(item)], lista1[i]
                        break
            else:
                continue
        for i in range(0, len(indexs), 2):
            lista3[indexs[i][0]], lista3[indexs[i][1]] = lista3[indexs[i][1]], lista3[indexs[i][0]]

        return lista3

    def fechaDia(self, quantidadeArray):
        try:
            conexao = sqlite3.connect("Registros.db")

            produtosBanco = Banco.recuperaProdutos(Banco)
            produtosNome = []
            linhas = []

            data = datetime.now().strftime("%d%m%Y")

            criaTableDiaQuery = "CREATE TABLE dia" + data + "(produto, total, valor)"
            fechaDiaQuery = "INSERT INTO dia" + data + " (produto, total, valor) VALUES (?,?,?);"

            for produto in produtosBanco:
                produtosNome.append(produto[1])

            for quantidade in quantidadeArray:
                produto = produtosBanco[quantidadeArray.index(quantidade)][1]
                valor = quantidade * produtosBanco[produtosNome.index(produto)][2]
                tup = (produto, str(quantidade), str(valor))
                linhas.append(tup)

            cursor = conexao.cursor()
            cursor.execute(criaTableDiaQuery)
            cursor.executemany(fechaDiaQuery, linhas)
            cursor.close()

            conexao.commit()
        except sqlite3.Error as error:
            print("Erro ao fechar o dia: ", error)
        finally:
            conexao.close()

    def recuperaDias(self):
        try:
            conexao = sqlite3.connect("Registros.db")

            recuperaDiasQuery = "SELECT name FROM sqlite_master WHERE type='table';"

            cursor = conexao.cursor()
            cursor.execute(recuperaDiasQuery)
            dias = cursor.fetchall()
            cursor.close()

            if len(dias) > 1:
                return dias
            else:
                return 0
        except sqlite3.Error as error:
            print("Erro ao recuperar dias: ", error)
        finally:
            conexao.close()

    def recuperaRegistros(self, dia):
        try:
            conexao = sqlite3.connect("Registros.db")

            recuperaRegistrosQuery = "SELECT * FROM dia" + dia

            cursor = conexao.cursor()
            cursor.execute(recuperaRegistrosQuery)
            registros = cursor.fetchall()
            cursor.close()

            return registros

        except sqlite3.Error as error:
            print("Erro ao recuperar registros: ", error)
        finally:
            conexao.close()
