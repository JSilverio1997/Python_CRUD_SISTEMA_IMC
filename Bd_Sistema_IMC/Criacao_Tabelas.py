import tkinter.messagebox
from Bd_Sistema_IMC.Conexao_Banco_IMC import Conexao


class CriacaoTabelas(Conexao):

    def creation_table_imc(self):
        try:
            self.conexao_aberta()
            sql = "CREATE TABLE IMC( " \
                  "USER_ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                  "NOME VARCHAR(40) UNIQUE," \
                  "PESO FLOAT," \
                  "ALTURA FLOAT," \
                  "IMC FLOAT," \
                  "CATEGORIA VARCHAR(100));"
            self.cursor.execute(sql)
            print("_" * 80)
            print("A tabela IMC foi criada com sucesso.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar criar a tabela")
        finally:
            self.conexao_fechada()

    def drop_table_imc(self):
        try:
            self.conexao_aberta()
            sql = 'DROP TABLE IMC;'
            self.cursor.execute(sql)
            print("_" * 80)
            print("Tabela excluída")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar excluir a tabela IMC.")
        finally:
            self.conexao_fechada()
