import tkinter.messagebox
from Bd_Sistema_IMC.Criacao_Tabelas import CriacaoTabelas
from Sistema_IMC.Interface_Grafica.Tela_Listagem import *
from Manipulacao_Arquivos.Arquivos import Arquivos


class OperacoesCrud(CriacaoTabelas):

    def __init__(self):
        pass

    def criacao_tabela_imc(self):
        self.creation_table_imc()

    def excluir_tabela_imc(self):
        self.drop_table_imc()

    def insert(self, nome, peso, altura, imc, msg_imc):
        try:
            verifica_reg = self.select_verificao(nome)
            if verifica_reg is None:
                self.conexao_aberta()
                sql = ("insert into IMC (nome,peso,altura,imc,categoria) values('%s',%.2f,%.2f,%.2f,'%s');" %
                       (nome, peso, altura, imc, msg_imc))
                self.cursor.execute(sql)
                self.conexao.commit()
                tkinter.messagebox.showinfo("OK", "Foi inserido um registro no banco de dados.")

            else:
                tkinter.messagebox.showwarning("Atenção", "Já existe um registro com este nome, \n "
                                                          "por favor escolha outro.")
        except():
            tkinter.messagebox.showwarning("Atenção", "Erro ao tentar inserir o registro no Bano de Dados.")
        finally:
            self.conexao_fechada()

    def update(self, user_id, nome, peso, altura, imc, categoria):
        try:
            verifica_nome = self.select_verificao(nome)
            if verifica_nome is None:
                self.conexao_aberta()
                sql = ("update IMC  set nome = '%s'"
                       " where user_id = %d;" % (nome, user_id))
                self.cursor.execute(sql)
                self.conexao.commit()
                tkinter.messagebox.showinfo("OK", "O Nome do Usuário foi alterado com sucesso.")

            else:
                self.conexao_aberta()
                sql = ("update IMC  set peso = %.2f,altura = %.2f,imc = %.2f ,categoria = '%s' "
                       " where user_id = %d;" % (peso, altura, imc, categoria, user_id))
                self.cursor.execute(sql)
                self.conexao.commit()
                tkinter.messagebox.showinfo("OK", "Os dados foram alterados com sucesso.")

        except():
            tkinter.messagebox.showerror("Erro", " Erro ao tentar alterar o registro.")
        finally:
            self.conexao_fechada()

    def delete(self, user_id):
        try:
            self.conexao_aberta()
            sql = ("delete from IMC where user_id = %d;" % user_id)
            self.cursor.execute(sql)
            self.conexao.commit()
            tkinter.messagebox.showinfo("OK", "O registro foi deletado com sucesso.")

        except():
            tkinter.messagebox.showerror("Erro", " Erro ao tentar deletar o registro.")
        finally:
            self.conexao_fechada()

    def select_verificao(self, nome):
        try:
            self.conexao_aberta()
            sql = ("select nome from imc where nome = '%s';" % nome)
            self.cursor.execute(sql)
            consulta_verificacao = self.cursor.fetchone()

            if consulta_verificacao is not None:
                return consulta_verificacao[0]

            else:
                return None
        except():
            tkinter.messagebox_showwarning("Atenção", "Erro em geral ao realizar o select de verificação ")
        finally:
            self.conexao_fechada()

    def select_like(self, nome):
        try:
            self.conexao_aberta()
            sql = "select * from imc where upper(nome) like '%" + nome.upper() + "%';"
            self.cursor.execute(sql)
            consulta_unica = self.cursor.fetchone()

            if consulta_unica is not None:
                tkinter.messagebox.showinfo("Informações", "Nome: %s \n Peso: %s \n Altura: %s \n IMC: %s \n "
                                                           "Categoria: %s" % (consulta_unica[1], consulta_unica[2],
                                                                              consulta_unica[3], consulta_unica[4],
                                                                              consulta_unica[5]))
                print("Nome: %s " % consulta_unica[1])
                print("Peso: %.2f " % consulta_unica[2])
                print("Altura: %.2f " % consulta_unica[3])
                print("IMC: %.2f " % consulta_unica[4])
                print("Categoria: %s " % consulta_unica[5])
                print("_" * 80)
                return consulta_unica

        except():
            tkinter.messagebox.showwarning("Atenção", "Não a dados para este nome.")
        finally:
            self.conexao_fechada()

    def select_rank_15(self):
        try:
            dados = []

            self.conexao_aberta()
            sql = "select * from imc order by nome limit 15;"
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()

            for rec in consulta:
                dados.append(rec)

            instancia_form_listagem(dados)

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar recuperar consulta do banco de dados.")
        finally:
            self.conexao_fechada()

    def select_all(self):
        try:
            dados = []

            self.conexao_aberta()
            sql = "select * from imc order by user_id,nome;"
            self.cursor.execute(sql)
            consulta = self.cursor.fetchall()

            for rec in consulta:
                dados.append(rec)

            if tkinter.messagebox.askyesnocancel("Pergunta", "Deseja exportar em arquivos a lista de dados ?"):
                relatorio = Arquivos()
                relatorio.gravar_arquivo(dados)
                relatorio.gerar_xml(dados)

        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar recuperar consulta do banco de dados.")
        finally:
            self.conexao_fechada()
