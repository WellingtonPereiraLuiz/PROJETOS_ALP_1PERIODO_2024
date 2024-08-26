# Inicializando o carrinho de compras
carrinho = {}
produto_id = 1

while True:
    # Solicitando a descrição do produto
    descricao = input("Digite a descrição do produto (ou 'sair' para encerrar): ")
    
    if descricao.lower() == "sair":
        break

    # Solicitando a quantidade do produto
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido para a quantidade.")
        continue

    # Solicitando o preço do produto
    try:
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Por favor, digite um número válido para o preço.")
        continue

    # Armazenando o produto no dicionário
    carrinho[produto_id] = {
        'Descrição': descricao,
        'Quantidade': quantidade,
        'Preço': preco
    }
    
    produto_id += 1

# Exibindo os produtos cadastrados
print("\nProdutos cadastrados no carrinho:")
for id_produto, detalhes in carrinho.items():
    print(f"ID: {id_produto}")
    for chave, valor in detalhes.items():
        print(f"  {chave}: {valor}")
    print()  # Linha vazia para separar os produtos
