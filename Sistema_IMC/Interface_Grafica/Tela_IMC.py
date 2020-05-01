import tkinter as tk
import tkinter.messagebox
from Sistema_IMC.Metodos_Sistema_IMC.Calculo_IMC import Calculo
from Bd_Sistema_IMC.Operacoes_CRUD import OperacoesCrud


class SistemaIMCInterface(tk.Frame):

    def __init__(self, master):
        # Estrutura do formulario
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Sistema IMC Para Adultos")
        self.criar_objetos()

    def criar_objetos(self):

        # Labels
        tk.Label(text="Sistema de IMC", font="arial").grid(row=1, column=5, columnspan=10, pady=8, padx=8)
        tk.Label(text="Nome:", font="arial").grid(row=4, column=4, pady=4)
        tk.Label(text=" Peso:", font="arial").grid(row=5, column=4, pady=4)
        tk.Label(text="Altura:", font="arial").grid(row=7, column=4, pady=4)

        # TextFields
        nome = tk.Entry(width=25, font="Arial")
        nome.grid(row=4, column=5, columnspan=1, padx=3)
        nome.focus()
        self.nome = nome

        peso = tk.Entry(width=25, font="Arial")
        peso.grid(row=5, column=5, columnspan=1, padx=3)
        self.peso = peso

        altura = tk.Entry(width=25, font="Arial")
        altura.grid(row=7, column=5, columnspan=1, padx=3)
        self.altura = altura

        # Botões

        btn_calcular = tk.Button(text="Calcular", width="8", font="arial,18bold", command=self.calcular)
        btn_calcular.grid(row=12, column=5, pady=5)

        # Limpar
        btn_limpar = tk.Button(text="Limpar", font="arial,,18bold", width="8", command=self.limpar)
        btn_limpar.grid(row=13, column=5)

        # Listar
        btn_listar = tk.Button(text="Listar", font="arial,,18", width="8", command=self.listar)
        btn_listar.grid(row=2, column=5, pady=3, padx=2, columnspan=1)

        # Exportar
        btn_exportar = tk.Button(text="Exportar", font="arial,,18", width="8", command=self.exportar)
        btn_exportar.grid(row=3, column=5, pady=5, padx=2, columnspan=1)

    def listar(self):
        self.master.destroy()
        select = OperacoesCrud()
        select.select_rank_15()

    @staticmethod
    def exportar():
        select = OperacoesCrud()
        select.select_all()

    def calcular(self):
        try:
            nome = self.nome.get()
            peso = self.peso.get().replace(',', '.')
            altura = self.altura.get().replace(',', '.')

            if len(nome) < 3 or nome == "":
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o seu nome.")
                self.nome.delete(0, len(self.nome.get()))
                self.nome.focus()

            elif peso.isalpha() or peso == "" or peso.isspace():
                tkinter.messagebox.showwarning("Atenção", "Por favor digite o peso corretamente.")
                self.peso.focus()

            elif altura.isalpha() or altura == "" or altura.isspace():
                tkinter.messagebox.showwarning("Atenção", "Por favor digite a altura corretamente.")
                self.altura.focus()

            else:
                calcular = Calculo()
                calcular.calcular_imc(nome, peso, altura)
                self.limpar()

        except ValueError:
            tkinter.messagebox.showwarning("Atenção", "Por favor digite somente números")
            self.limpar()

    def limpar(self):
        self.nome.delete(0, len(self.nome.get()))
        self.peso.delete(0, len(self.peso.get()))
        self.altura.delete(0, len(self.altura.get()))
        self.nome.focus()


def instanciando_form_imc():
    sistema_imc = tk.Tk()
    sistema_imc.iconbitmap(r"Images/IconeIMC.ico")
    SistemaIMCInterface(sistema_imc)
    sistema_imc.configure(relief="ridge", bg="light green", border=10)
    sistema_imc.geometry("350x320+500+200")
    sistema_imc.resizable(0, 0)
    sistema_imc.minsize(350, 300)
    sistema_imc.maxsize(350, 320)
    sistema_imc.mainloop()
    exit()
