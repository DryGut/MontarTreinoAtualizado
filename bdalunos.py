#create a DB to registrate costumers

import sqlite3
import os
import io
import datetime


class Connect():
    """cria a conexao com o banco de dados"""
    def __init__(self, db_name):
        try:
            #conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print('Banco: ', db_name)
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("Sqlite version: %s" % self.data)
        except sqlite3.Error:
            print('Erro ao abrir o banco de dados')
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print('Conexao Encerrada')


class ClientesDb():
    """cria o banco de dados"""

    tb_name = 'clientes'

    def __init__(self):
        """conecta com banco de dados"""

        self.db = Connect('clientes.db')
        self.tb_name

    def fechar_conexao(self):
        """fecha conexao"""

        self.db.close_db()

    def criar_schema(self, schema_name='clientes_schema.sql'):
        """criando tabela apartir de um arquivo"""

        print("Criando tabela %s ..." % self.tb_name)

        try:
            with open(schema_name, 'rt') as f:
                schema = f.read()
                self.db.cursor.executescript(schema)
        except sqlite3.Error:
            print('Aviso: A tabela ja existe %s' % self.tb_name)
            return False
        print("Tabela criada com Sucesso")

    def inserir_dados(self):
        """inserindo dados dos alunos"""

        self.nome = input('Nome: ').title()
        self.idade = input('Idade: ')
        self.cpf = input('CPF: ')
        self.email = input('Email: ')
        self.celular = input('Celular: ')
        self.criado_em = datetime.datetime.now().isoformat(" ")

        try:
            self.db.cursor.execute(
                """
                      INSERT INTO alunos (
                      nome, 
                      idade, 
                      cpf, 
                      email, 
                      celular, 
                      criado_em) 
                      VALUES  (?, ?, ?, ?, ?, ?)
                      """, (self.nome, self.idade, self.cpf, self.email,
                            self.celular, self.criado_em))
            self.db.commit_db()
            print("dados inseridos com sucesso")

        except sqlite3.IntegrityError:
            print("Aviso: Email Invalido.")
            return False

    def localizador(self, id):
        """localiza os dados antes de editar ou deletar"""

        l = self.db.cursor.execute('SELECT * FROM alunos WHERE id = ?', (id, ))
        return l.fetchone()

    def novo_cadastro(self, nome):
        """localiza cadastro"""

        n = self.db.cursor.execute("SELECT nome FROM alunos")
        
        return list(n.fetchone())

    def atualizar_dados(self, id):
        """atualiza os dados dos alunos cadastrados"""

        try:

            a = self.localizador(id)

            if a:
                self.novo_email = input('Novo Email: ')
                self.novo_celular = input('Novo Numero: ')
                self.db.cursor.execute(
                    """
                               UPDATE alunos SET
                               email = ?,
                               celular = ?
                               WHERE id = ?
                               """, (
                        self.novo_email,
                        self.novo_celular,
                        id,
                    ))
                self.db.commit_db()
                print('Dados atualizados com Sucesso')

            else:
                print('Dados Invalidos')

        except sqlite3.ValueError:
            raise ValueError

    def deletar_dados(self, id):
        """deleta os dados existentes"""

        try:
            a = self.localizador(id)

            if a:
                self.db.cursor.execute(
                    """
                                 DELETE FROM alunos WHERE id = ? 
                                 """, (id, ))
                self.db.commit_db()
                print('Dados removidos com Sucesso')

            else:
                print('Dados Inexistentes')

        except sqlite3.ValueError:
            raise ValueError
