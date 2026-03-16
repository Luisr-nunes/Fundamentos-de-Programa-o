total_compra = 0.0
print("--- Bem-vindo ao Caixa do Supermercado ---")
print("Vamos registrar os produtos da sua compra.")


while True:
    print("\n--- Novo Produto ---")
    nome_produto = input("Digite o nome do produto: ")
    preco_unitario = float(input(f"Digite o preço unitário de '{nome_produto}': R$ "))
    quantidade = int(input(f"Digite a quantidade de '{nome_produto}': "))

    if preco_unitario > 0 and quantidade >= 1:
        subtotal_item = preco_unitario * quantidade
        total_compra = total_compra + subtotal_item

        print(f"'{nome_produto}' adicionado. Subtotal do item: R$ {subtotal_item:.2f}")
        print(f"Total da compra até agora: R$ {total_compra:.2f}")
    else:
        print("Erro: Preço ou quantidade inválidos. O preço deve ser maior que zero e a quantidade deve ser pelo menos 1.")
        print("Este item não será registrado.")

    while True:
        resposta = input("\nDeseja registrar outro item? (S/N): ")
        if resposta.upper() == 'S' or resposta.upper() == 'N':
            break
        else:
            print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")

    if resposta.upper() == 'N':
        print("Finalizando a compra...")
        break

print("\n--- Compra Finalizada ---")
print(f"O valor total da sua compra é: R$ {total_compra:.2f}")
print("Obrigado por comprar conosco!")