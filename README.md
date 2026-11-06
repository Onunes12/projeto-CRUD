
# Sistema de Gerenciamento de Estoque — Python

Projeto desenvolvido em Python com integração ao banco de dados SQLite, com o objetivo de praticar lógica de programação, manipulação de dados e operações CRUD.

## Funcionalidades

O sistema permite realizar as quatro operações principais de um CRUD:

- **Create:** Cadastrar produtos com nome, quantidade e preço.
- **Read:** Listar produtos cadastrados e consultar produtos pelo nome.
- **Update:** Atualizar nome, quantidade ou preço de um produto.
- **Delete:** Excluir produtos cadastrados.

O projeto também conta com validações de entrada e verificações de existência dos produtos.

## Tecnologias utilizadas

- Python 3
- SQLite
- Biblioteca sqlite3 do Python
- Git e GitHub

## Estrutura do projeto

- `CRUD.py` — Arquivo principal, responsável pelo menu e pelas operações CRUD.
- `banco.py` — Arquivo responsável pela conexão com o banco de dados.
- `.gitignore` — Configuração dos arquivos ignorados pelo Git.

## Como executar

1. Tenha o Python 3 instalado.
2. Faça o download ou clone o repositório.
3. Configure o banco de dados SQLite conforme o projeto.
4. Abra o terminal na pasta do projeto.
5. Execute o comando:

`python CRUD.py`

## Objetivo do projeto

Este projeto foi desenvolvido como parte dos meus estudos em desenvolvimento Back-end.

Durante o desenvolvimento, pratiquei:

- Estruturas condicionais e de repetição.
- Manipulação de dados em Python.
- Integração com banco de dados relacional.
- Comandos SQL: INSERT, SELECT, UPDATE e DELETE.
- Validação de dados e tratamento de situações em que um produto não existe.
- Versionamento de código utilizando Git e GitHub.

## Próximas melhorias

- Melhorar as validações de entrada.
- Organizar e refatorar o código.
- Desenvolver uma API utilizando Python.
- Expandir as funcionalidades do sistema.
