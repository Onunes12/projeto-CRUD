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
        produto = {'nome': nome,
                   'preco': preco,
                   'quantidade': quantidade}
        produtos.append(produto)
        print('Produto cadastrado com sucesso!')
    elif escolha == 2:
        if len(produtos) > 0:
            for produto in produtos:
                print(f'nome: {produto['nome']}, preco: {produto['preco']}, quantidade: {produto['quantidade']}')
        else:
            print('Nenhum produto cadastrado!') 
    elif escolha == 3:
        print('''OQ  VOCE GOSTARIA DE ATUALIZAR?
        1 - NOME
        2 - PRECO 
        3 - QUANTIDADE''')
        opcao = int(input('Digite a opcao desejada: '))
        if opcao == 1:
            nome_atual = input('Digite o nome do produto que deseja atualizar: ').upper().strip()
            encontrado = False
            for produto in produtos:
                if produto['nome'] == nome_atual:
                    encontrado = True
                    novo_nome = input('Digite o novo nome do produto: ').upper().strip()
                    produto['nome'] = novo_nome
                    print('nome do produto foi atualizado com sucesso!!')
            if not encontrado:
                    print('Produto nao encontrado!')
        elif opcao == 2:
            nome_atual = input('Digite o nome do produto que deseja alterar o preco: ').upper().strip()
            encontrado = False
            for produto in produtos:
                if produto['nome'] == nome_atual:
                    encontrado = True
                    novo_preco = float(input('Digite o novo preco do produto: '))
                    produto['preco'] = novo_preco
                    print('Preco do produto foi atualizado com sucesso!!')
            if not encontrado:
                    print('Produto nao encontrado!')
        elif opcao == 3:
             nome_atual = input('Digite o nome do produto que deseja alterar a quantidade: ').upper().strip()
             encontrado = False
             for produto in produtos:
                  if produto['nome'] == nome_atual:
                       encontrado = True
                       nova_quantidade = int(input('Digite a nova quantidade do produto: '))
                       produto['quantidade'] = nova_quantidade
                       print('Quantidade do produto foi atualizada com sucesso!!')
             if not encontrado:
                    print('Produto nao encontrado!')
    elif escolha == 4:
        nome_atual = input('Digite o nome do produto que deseja deletar: ').upper().strip()
        encontrado = False
        for produto in produtos:
              if produto['nome'] == nome_atual:
                   encontrado = True
                   produtos.remove(produto)
                   print('Produto deletado com sucesso!!')
        if not encontrado:
            print('Produto nao encontrado!')
    elif escolha == 5:
        print('Saindo do programa...')
        break
