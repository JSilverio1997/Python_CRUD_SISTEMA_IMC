from Sistema_IMC.Interface_Grafica.Tela_IMC import instanciando_form_imc


class Main:
    def __init__(self):
        self.instanciar()

    @staticmethod
    def instanciar():
        instanciando_form_imc()


execute = Main()
