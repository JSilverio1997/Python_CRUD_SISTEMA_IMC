import tkinter.messagebox
from Sistema_IMC.Metodos_Sistema_IMC.IMC_Getters_Setters import SistemaIMC
from Bd_Sistema_IMC.Operacoes_CRUD import OperacoesCrud


class Calculo:

    def __init__(self):
        pass

    @staticmethod
    def calcular_imc(nome, peso, altura):
        try:
            nome = nome
            peso = float(peso)
            altura = float(altura)
            msg_imc = ""

            if peso >= 10 and altura >= 0.3:
                imc = peso / altura ** 2

                # Verificando o Indice de Massa Corporal
                if imc < 17:
                    msg_imc = " Muito Abaixo do Peso."

                elif 17 <= imc <= 18.49:
                    msg_imc = "Abaixo do Peso."

                elif 18.5 <= imc <= 24.99:
                    msg_imc = "com o Peso ideal."

                elif 25 <= imc <= 29.99:
                    msg_imc = "Acima do Peso."

                elif 30 <= imc <= 34.99:
                    msg_imc = "com Obesidade 1."

                elif 35 <= imc <= 39.99:
                    msg_imc = "com Obesidade 2."

                elif imc >= 40:
                    msg_imc = "com Obesidade 3."

                # Instanciando a Classe abaixo para usar seus metodos getters e setters
                encaps = SistemaIMC()
                encaps.nome = nome
                encaps.peso = peso
                encaps.altura = altura
                encaps.imc = imc
                encaps.msg_imc = msg_imc

                tkinter.messagebox.showinfo("OK", "%s o seu IMC é %.2f e você está %s" % (encaps.nome,
                                                                                          round(encaps.imc, 2),
                                                                                          msg_imc))

                insert = OperacoesCrud()
                insert.insert(encaps.nome, encaps.peso, encaps.altura, encaps.imc, encaps.msg_imc)

            elif peso < 10:
                tkinter.messagebox.showwarning("Atenção", "O peso mínimo é 10 Quilos.")

            elif altura < 0.3:
                tkinter.messagebox.showwarning("Atenção", "A Altura mínima é de 0.30.")

        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar realizar o cálculo do IMC.")

    @staticmethod
    def recalcular_imc(user_id, nome, peso, altura):
        try:
            nome = nome
            peso = float(peso)
            altura = float(altura)
            msg_imc = ""

            if peso >= 10 and altura >= 0.3:
                imc = peso / altura ** 2

                # Verificando o Indice de Massa Corporal
                if imc < 17:
                    msg_imc = " Muito Abaixo do Peso."

                elif 17 <= imc <= 18.49:
                    msg_imc = "Abaixo do Peso."

                elif 18.5 <= imc <= 24.99:
                    msg_imc = "com o Peso ideal."

                elif 25 <= imc <= 29.99:
                    msg_imc = "Acima do Peso."

                elif 30 <= imc <= 34.99:
                    msg_imc = "com Obesidade 1."

                elif 35 <= imc <= 39.99:
                    msg_imc = "com Obesidade 2."

                elif imc >= 40:
                    msg_imc = "com Obesidade 3."

                tkinter.messagebox.showinfo("OK", "%s o seu IMC é %.2f e você está %s" % (nome, round(imc, 2),
                                                                                          msg_imc))

                update = OperacoesCrud()
                update.update(user_id, nome, peso, altura, imc, msg_imc)

            elif peso < 10:
                tkinter.messagebox.showwarning("Atenção", "O peso mínimo é 10 Quilos.")

            elif altura < 0.3:
                tkinter.messagebox.showwarning("Atenção", "A Altura mínima é de 0.30.")

        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar realizar o cálculo do IMC.")
