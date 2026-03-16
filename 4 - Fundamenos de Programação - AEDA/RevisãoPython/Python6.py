print("Simulador de Caixa de Supermercado")

subtotal = 0.0

while True:
    nome = input("Nome do produto: ").strip()

    preco = float(input("Preço unitário: "))
    if preco <= 0:
        print("Preço inválido. O preço deve ser maior que zero. Produto não registrado.")
        # pergunta se quer continuar
        resp = input("Deseja registrar outro item? (S/N): ").strip().upper()
        if resp == 'S':
            continue
        else:
            break

    quantidade = int(input("Quantidade: "))
    if quantidade < 1:
        print("Quantidade inválida. Deve ser pelo menos 1. Produto não registrado.")
        resp = input("Deseja registrar outro item? (S/N): ").strip().upper()
        if resp == 'S':
            continue
        else:
            break

    # cálculo do total do item e soma ao subtotal
    total_item = preco * quantidade
    subtotal += total_item
    print(f"Produto registrado: {nome} | Total item: R$ {total_item:.2f}")

    # pergunta se deseja continuar
    resp = input("Deseja registrar outro item? (S/N): ").strip().upper()
    while resp not in ('S', 'N'):
        resp = input("Resposta inválida. Digite 'S' para sim ou 'N' para não: ").strip().upper()
    if resp == 'N':
        break

print(f"\nValor total da compra: R$ {subtotal:.2f}")
