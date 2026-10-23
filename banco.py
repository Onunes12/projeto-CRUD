import sqlite3


conexao = sqlite3.connect('estoque.db')

print('Banco de dados criado com sucesso!')


conexao.execute(''' 
CREATE TABLE IF NOT EXISTS PRODUTOS
( ID INTEGER PRIMARY KEY ,
NOME TEXT NOT NULL,
PRECO REAL NOT NULL,
QUANTIDADE INTEGER NOT NULL);''')


conexao.execute( ''' INSERT INTO PRODUTOS (NOME, PRECO, QUANTIDADE)
VALUES ('Camiseta', 29.90, 40),
('Calça', 79.90, 20),
('Tênis', 199.90, 15),
('Jaqueta', 149.90, 10),
('Meias', 9.90, 100);''')

conexao.commit()
conexao.close()