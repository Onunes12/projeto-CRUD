import sqlite3


conexao = sqlite3.connect('estoque.db')

print('Banco de dados criado com sucesso!')


conexao.execute(''' 
CREATE TABLE IF NOT EXISTS PRODUTOS
( ID INTEGER PRIMARY KEY ,
NOME TEXT NOT NULL,
PRECO REAL NOT NULL,
QUANTIDADE INTEGER NOT NULL);''')


conexao.commit()
conexao.close()