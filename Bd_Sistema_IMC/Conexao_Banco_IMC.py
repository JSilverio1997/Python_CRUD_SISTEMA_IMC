import sqlite3
import tkinter.messagebox


class Conexao:

    def __init__(self):
        pass

    def conexao_aberta(self):
        try:
            conexao = sqlite3.connect("BD_IMC")
            cursor = conexao.cursor()
            self.conexao = conexao
            self.cursor = cursor

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar criar uma conexão com o banco de dados.")
            self.conexao.close()

    def conexao_fechada(self):
        self.conexao.close()
