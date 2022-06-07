#create a DB to registrate costumers

import sqlite3
import os
import io
import datetime
import names


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

  