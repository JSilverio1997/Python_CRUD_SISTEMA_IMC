# coding=utf-8
import tkinter.messagebox
from xml.etree.ElementTree import ElementTree, Element


class Arquivos:

    def __init__(self):
        pass

    @staticmethod
    def gravar_arquivo(dados=[]):
        try:
            cont = 0
            arquivo = open("C:\\Users\\Usuario\\João Victor\\Joao\\Projetos\\Python\\Projects in Python\\" +
                           "\\Com Interface Gráfica\\Projeto em Python - Sistema de "
                           "IMC\\Sistema_IMC\\Manipulacao_Arquivos" +
                           "\\Lista de Arquivos\\" + "lista_dados.txt", "w")
            arquivo.write(" \t \t \t Lista de Dados \n")
            arquivo.write("_" * 80 + "\n")

            for gravacao in dados:
                cont += 1
                arquivo.write("User ID: %s\n" % gravacao[0])
                arquivo.write("Nome: %s \n" % gravacao[1])
                arquivo.write("Peso: %.2f \n" % gravacao[2])
                arquivo.write("Altura: %s \n" % gravacao[3])
                arquivo.write("IMC: %s \n" % gravacao[4])
                arquivo.write("Categoria: %s \n" % gravacao[5])
                arquivo.write("_" * 80 + "\n")

            arquivo.write("Quantidade de Registros: %d \n" % cont)
            arquivo.write("_" * 80 + "\n")
            arquivo.close()
            tkinter.messagebox.showinfo("Informação",
                                        "A Lista de todos os dados foi salva em um arquivo txt com sucesso.")

        except ():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar gravar as informações em um arquivo txt.")
            arquivo.close()

    @staticmethod
    def gerar_xml(dados=[]):
        try:
            xml_cabecalho = Element("Lista de Dados")
            for reg in dados:
                xml_id = Element("%d" % reg[0])
                xml_nome = Element("%s" % reg[1])
                xml_peso = Element("%.2f" % reg[2])
                xml_altura = Element("%.2f" % reg[3])
                xml_imc = Element("%.2f" % reg[4])
                xml_categoria = Element("%s" % reg[5])

                xml_cabecalho.append(xml_id)
                xml_cabecalho.append(xml_nome)
                xml_cabecalho.append(xml_peso)
                xml_cabecalho.append(xml_altura)
                xml_cabecalho.append(xml_imc)
                xml_cabecalho.append(xml_categoria)

                caminho = "C:\\Users\\Usuario\\João Victor\\Joao\\Projetos\\Python\\Projects in Python\\" \
                          "\\Com Interface Gráfica\\Projeto em Python - Sistema de " \
                          "IMC\\Sistema_IMC\\Manipulacao_Arquivos\\Lista de Arquivos\\"
                ElementTree(xml_cabecalho).write(caminho + "\\" + "lista_dados.xml")
            tkinter.messagebox.showinfo("Informação", "Foi criado um arquivo xml com todos os dados.")

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar criar o arquivo em xml.")

    @staticmethod
    def leitura_arquivos(extensao_arq=""):
        try:
            arquivo = open("C:\\Users\\Usuario\\João Victor\\Joao\\Projetos\\Python\\Projects in Python\\" +
                           "\\Com Interface Gráfica\\Projeto em Python - Sistema de " +
                           "IMC\\Sistema_IMC\\Manipulacao_Arquivos\\Lista de Arquivos\\" + "lista_dados" + extensao_arq,
                           "r")
            print("Lendo o arquivo gravado no diretório Lista de Arquivos \n")

            for leitura in arquivo.readlines():
                print(leitura)

            arquivo.close()

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar realizar a leitura do arquivo.")
            arquivo.close()
