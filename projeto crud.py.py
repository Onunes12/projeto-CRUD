import sqlite3
conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

produtos = []
while True:
    print(''' 
 1 - CADASTRAR PROODUTO
 2 - CONSULTAR PRODUTO
 3 - ATUALIZAR PRODUTO
 4 - DELETAR PRODUTO
 5 - SAIR ''')
    escolha = int(input('Digite a opcao desejada: '))
    if escolha == 1:
        nome = (input('Digite o nome do produto: ')).upper().strip()
        preco = float(input('Digite o preco do produto: '))
        quantidade = int(input('Digite a quantidade de produtos: '))
        cursor.execute(' INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', (nome, preco, quantidade))
        conexao.commit()
        produto = {'nome': nome,
                   'preco': preco,
                   'quantidade': quantidade}
        produtos.append(produto)
        print('Produto cadastrado com sucesso!')
    elif escolha == 2:
        cursor.execute('SELECT * FROM produtos')
        registros = cursor.fetchall()

        if registros:
             for registro in registros:
                  print(registro)        
        else:
            print('Nenhum produto cadastrado!') 
    elif escolha == 3:
        print('''OQ  VOCE GOSTARIA DE ATUALIZAR?
        1 - NOME
        2 - PRECO 
        3 - QUANTIDADE''')
        opcao = int(input('Digite a opcao desejada: '))
        
        if opcao == 1:
            nome_atual = input('Digite o nome do produto que deseja alterar: ').upper().strip()

            cursor.execute('SELECT id FROM produtos WHERE nome = ? COLLATE NOCASE', (nome_atual,))
            produto = cursor.fetchone()
            if produto:
                novo_nome = input('Digite o novo nome do produto: ').upper().strip()
                cursor.execute('UPDATE produtos SET nome = ? WHERE id = ?', (novo_nome, produto[0]))
                conexao.commit()
                print('Nome atualizado com sucesso! ( nome antigo : {} / nome novo : {} )'.format(nome_atual, novo_nome))
            else:
                print('Produto nao encontrado...')
        elif opcao == 2:
            nome_atual = input('Digite o nome do produto que deseja alterar o preco: ').upper().strip()
            cursor.execute('SELECT id, preco FROM produtos WHERE nome = ? COLLATE NOCASE', (nome_atual,))
            produto = cursor.fetchone()
            
            if produto:
                preco_antigo = produto[1]
                novo_preco = float(input('Digite o novo preco do produto:'))
                cursor.execute('UPDATE produtos SET preco = ? WHERE id = ?', (novo_preco, produto[0]))
               
                conexao.commit()
                print('Preco atualizado com sucesso! ( preco antigo : {} / preco novo : {} )'.format(preco_antigo, novo_preco))
            else:
                print('Produto nao encontrado...')

        elif opcao == 3:
             nome_atual = input('Digite o nome do produto que deseja alterar a quantidade: ').upper().strip()
             cursor.execute('SELECT id, quantidade FROM produtos WHERE nome = ? COLLATE NOCASE', (nome_atual,))
             produto = cursor.fetchone()
             if produto:
                 quantidade_antiga = produto[1]
                 nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                 cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (nova_quantidade, produto[0]))
                 conexao.commit()
                 print('Quantidade atualizada com sucesso! ( quantidade antiga : {} / quantidade nova : {} )'.format(quantidade_antiga, nova_quantidade))

                  
             else:
                  print('Produto nao registrado!')
            
    elif escolha == 4:
        nome_atual = input('Digite o nome do produto que deseja deletar: ').strip()
        cursor.execute('DELETE FROM produtos WHERE nome = ? COLLATE NOCASE',(nome_atual,))
        conexao.commit()
        if cursor.rowcount > 0:
            print('Produto deletado com sucesso!!')
        else:
            print('Produto nao encontrado!')
    
    elif escolha == 5:
        print('Saindo do programa...')
        break
