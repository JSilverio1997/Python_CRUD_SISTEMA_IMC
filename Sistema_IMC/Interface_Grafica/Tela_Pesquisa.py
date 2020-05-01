from tkinter import *
import tkinter.messagebox
from Bd_Sistema_IMC.Operacoes_CRUD import OperacoesCrud
from Sistema_IMC.Metodos_Sistema_IMC.Calculo_IMC import Calculo


class TelaPesquisa(OperacoesCrud):

    def __init__(self, master):
        self.master = master
        self.master.title("Pesquisa")
        self.criacao_componentes()
        self.desativa_ativa_comp(False)

    def criacao_componentes(self):
        textos_labels = ["Nome:", "Peso:", "Altura:", "IMC:", "Categoria:"]
        cont_linha = 2
        # Labels
        Label(text="Pesquisar", font="arial,18", bg="light green").grid(row=0, column=4, padx=2, pady=2,
                                                                        columnspan=1)

        Label(text="Pesquisa:", font="arial,18", bg="light green").grid(row=1, column=3, padx=2, pady=2,
                                                                        columnspan=1)

        Label(text="", font="arial,8", bg="light green").grid(row=2, column=3)

        for texto in textos_labels:
            cont_linha += 1
            Label(text=texto, font="arial,12", bg="light green").grid(row=cont_linha + 1, column=3,
                                                                      padx=3, pady=2)

        # TextFields
        self.pesquisar = Entry(font="arial", width=30)
        self.pesquisar.focus()
        self.nome = Entry(font="arial", width=30)
        self.peso = Entry(font="arial", width=30)
        self.altura = Entry(font="arial", width=30)
        self.imc = Entry(font="arial", width=30)
        self.categoria = Entry(font="arial", width=30)

        self.pesquisar.grid(row=1, column=4, columnspan=1, padx=2, pady=2)
        self.nome.grid(row=4, column=4, columnspan=1)
        self.peso.grid(row=5, column=4, columnspan=1)
        self.altura.grid(row=6, column=4, columnspan=1)
        self.imc.grid(row=7, column=4, columnspan=1)
        self.categoria.grid(row=8, column=4, columnspan=1)

        # Buttons
        self.btn_pesquisar = Button(text="Pesquisar", width=8, font="Arial", command=self.consulta_unica)
        self.btn_pesquisar.grid(row=1, column=5, pady=2, padx=2, columnspan=1)

        self.btn_alterar = Button(text="Alterar", width=8, font="Arial", command=self.alterar)
        self.btn_alterar.grid(row=10, column=3, columnspan=2, pady=4)

        self.btn_deletar = Button(text="Excluir", width=8, font="Arial", command=self.excluir)
        self.btn_deletar.grid(row=10, column=4, columnspan=2, pady=4)

        self.btn_voltar = Button(text="Voltar", width=8, font="Arial", command=self.voltar_form_listar)
        self.btn_voltar.grid(row=11, column=3, columnspan=2, pady=4)

        self.btn_limpar = Button(text="Limpar", width=8, font="Arial", command=self.limpar)
        self.btn_limpar.grid(row=11, column=4, columnspan=2, pady=4)

    def consulta_unica(self):
        try:
            nome = self.pesquisar.get()
            if nome == "" or nome.isdigit() or len(nome) < 3:
                tkinter.messagebox.showwarning("Atenção", "Por favor digite um nome válido para pesquisar.")

            else:
                self.limpar()
                retorna_dados = self.select_like(nome)
                if retorna_dados is not None:
                    self.desativa_ativa_comp(True, retorna_dados)
        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar realizar a consulta")
            self.conexao_fechada()
            self.limpar()

    def desativa_ativa_comp(self, status, dados=[]):
        try:
            status = bool(status)
            user_id = 0
            if status is False:
                self.nome.config(state="read")
                self.peso.config(state="read")
                self.altura.config(state="read")
                self.imc.config(state="read")
                self.categoria.config(state="read")
                self.btn_alterar.configure(state="disabled")
                self.btn_deletar.configure(state="disabled")

            elif status:
                self.nome.config(state="normal")
                self.peso.config(state="normal")
                self.altura.config(state="normal")
                self.imc.config(state="normal")
                self.categoria.config(state="normal")
                self.btn_alterar.configure(state="normal")
                self.btn_deletar.configure(state="normal")

                self.pesquisar.delete(0, len(self.pesquisar.get()))
                self.pesquisar.insert(1, dados[1])

                self.user_id = dados[0]
                self.nome.insert(1, dados[1])
                self.peso.insert(2, dados[2])
                self.altura.insert(3, dados[3])

                # Condicao exclusiva pra IMC
                self.imc.insert(4, dados[4])
                self.categoria.insert(5, dados[5])
                self.imc.config(state="read")
                self.categoria.config(state="read")

        except():
            tkinter.messagebox.showwarning("Atenção",
                                           "Erro ao tentar desabilitar ou habilitar propriedades de componenetes.")
            self.conexao_fechada()

    def alterar(self):
        try:
            user_id = int(self.user_id)
            nome = self.nome.get()
            peso = float(self.peso.get().replace(',', '.'))
            altura = float(self.altura.get().replace(',', '.'))
            categoria = self.categoria.get()

            if tkinter.messagebox.askyesnocancel("Pergunta", "Você deseja alterar este registro: %s ?" % nome):
                recalcular = Calculo()
                recalcular.recalcular_imc(user_id, nome, peso, altura)

            self.limpar()

        except():
            tkinter.messagebox.showwarning("Atenção",
                                           "Erro ao tentar realizar o update do registro: %s" % self.nome.get())
            self.conexao_fechada()

    def excluir(self):

        if tkinter.messagebox.askyesnocancel("Pergunta", "Você deseja excluir o(a)  %s ?" % self.nome.get()):
            user_id = int(self.user_id)
            self.delete(user_id)

        self.limpar()

    def voltar_form_listar(self):
        self.master.destroy()
        self.select_rank_15()

    def limpar(self):
        self.pesquisar.delete(0, len(self.pesquisar.get()))
        self.nome.delete(0, len(self.nome.get()))
        self.peso.delete(0, len(self.peso.get()))
        self.altura.delete(0, len(self.altura.get()))

        # Condicao exclusiva pra limpar IMC e Categoria
        self.imc.config(state="normal")
        self.imc.delete(0, len(self.imc.get()))
        self.categoria.config(state="normal")
        self.categoria.delete(0, len(self.categoria.get()))

        self.pesquisar.focus()
        self.desativa_ativa_comp(False)


def instancia_form_tela_pesquisa():
    pesq = Tk()
    TelaPesquisa(pesq)
    pesq.iconbitmap(r"Images/IconeIMC.ico")
    pesq.geometry("520x450+500+200")
    pesq.configure(relief="ridge", bg="light green", border=10)
    pesq.resizable(0, 0)
    pesq.minsize(350, 300)
    pesq.maxsize(520, 350)
    pesq.mainloop()
