from tkinter import *
from Manipulacao_Arquivos.Arquivos import Arquivos


class TelaListagem:

    def __init__(self, master, dados=[]):
        self.master = master
        self.master.title("Listagem de Dados")
        self.criacao_componentes(dados)

    def criacao_componentes(self, dados=[]):
        linha = 4
        cor = ""

        for registros in dados:

            nome = registros[1]
            peso = registros[2]
            altura = registros[3]
            imc = registros[4]
            categoria = registros[5]

            if linha % 2 == 0:
                cor = "light green"

            else:
                cor = "white"

            lbl_nome = Label(text="Nome:%s " % nome, bg=cor, relief="ridge", padx=2, width=20, pady=5)
            lbl_nome["font"] = ("Arial", "12", "bold")
            lbl_nome.grid(row=linha + 1, column=1)

            lbl_peso = Label(text="Peso: %.2f " % peso, bg=cor, relief="ridge", padx=2, width=10, pady=5)
            lbl_peso["font"] = ("Arial", "12", "bold")
            lbl_peso.grid(row=linha + 1, column=2)

            lbl_altura = Label(text="Altura: %.2f " % altura, bg=cor, relief="ridge", padx=2, width=10, pady=5)
            lbl_altura["font"] = ("Arial", "12", "bold")
            lbl_altura.grid(row=linha + 1, column=3)

            lbl_imc = Label(text="IMC: %.2f " % imc, bg=cor, relief="ridge", padx=2, width=10, pady=5)
            lbl_imc["font"] = ("Arial", "12", "bold")
            lbl_imc.grid(row=linha + 1, column=4)

            lbl_categoria = Label(text="Categoria: %s" % categoria, bg=cor, relief="ridge", width=48, pady=5)
            lbl_categoria["font"] = ("Arial", "12", "bold")
            lbl_categoria.grid(row=linha + 1, column=5)

            linha = linha + 1

        btn_voltar = Button()
        btn_voltar["text"] = "Voltar"
        btn_voltar["font"] = "arial,10,bold"
        btn_voltar["width"] = 20
        btn_voltar["command"] = self.form_sistema_imc
        btn_voltar.grid(row=1, column=2, pady=5, columnspan=2, )

        btn_ler_arq = Button()
        btn_ler_arq["text"] = "Leitura de Arquivos"
        btn_ler_arq["font"] = "arial,10,bold"
        btn_ler_arq["width"] = 20
        btn_ler_arq["command"] = self.leitura_arquivos
        btn_ler_arq.grid(row=1, column=5, pady=5, columnspan=2, )

        btn_alterar = Button()
        btn_alterar["text"] = "Alterar"
        btn_alterar["font"] = "arial,10,bold"
        btn_alterar["width"] = 20
        btn_alterar["command"] = self.form_pesquisa
        btn_alterar.grid(row=linha + 2, column=3, columnspan=3, padx=2, pady=8)

        btn_deletar = Button()
        btn_deletar["text"] = "Excluir"
        btn_deletar["font"] = "arial,10,bold"
        btn_deletar["width"] = 20
        btn_deletar["command"] = self.form_pesquisa
        btn_deletar.grid(row=linha + 2, column=2, columnspan=3, padx=2, pady=8)

    def form_sistema_imc(self):
        self.master.destroy()
        from Sistema_IMC.Interface_Grafica.Main import instanciando_form_imc
        instanciando_form_imc()

    @staticmethod
    def leitura_arquivos():
        arquivo = Arquivos()
        arquivo.leitura_arquivos(".txt")
        arquivo.leitura_arquivos(".xml")

    def form_pesquisa(self):
        self.master.destroy()
        from Sistema_IMC.Interface_Grafica.Tela_Pesquisa import instancia_form_tela_pesquisa
        instancia_form_tela_pesquisa()


def instancia_form_listagem(dados=[]):
    lista = Tk()
    TelaListagem(lista, dados)
    lista.iconbitmap(r"Images/IconeIMC.ico")
    lista.configure(relief="ridge", bg="silver", border=10)
    lista.geometry("1040x750+200+5")
    lista.resizable(0, 0)
    lista.maxsize(1040, 750)
    lista.mainloop()
