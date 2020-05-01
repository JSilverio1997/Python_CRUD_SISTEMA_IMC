

class SistemaIMC:
    def __init__(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome.title()

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self,peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self,altura):
        self.__altura = altura

    @property
    def imc(self):
        return self.__imc

    @imc.setter
    def imc(self,imc):
        self.__imc = imc

    @property
    def msg_imc(self):
        return self.__msg_imc

    @msg_imc.setter
    def msg_imc(self,msg_imc):
        self.__msg_imc = msg_imc.title()











