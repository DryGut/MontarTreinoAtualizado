#arquivo para manipulação do DB

from bdalunos import Connect, ClientesDb

c = ClientesDb()
c.criar_schema()