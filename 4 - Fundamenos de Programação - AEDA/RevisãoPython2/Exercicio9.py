while True:
    print("\n--- Nova Simulação de Investimento ---")
    valor_inicial = float(input("Digite o valor inicial do investimento: R$ "))
    taxa_anual_pct = float(input("Digite a taxa de juros anual (em %): "))
    num_anos = int(input("Digite o número de anos para o investimento: "))

    if valor_inicial <= 0 or taxa_anual_pct <= 0 or num_anos <= 0:
        print("Erro: Todos os valores devem ser maiores que zero. Por favor, inicie uma nova simulação.")
        continue

    valor_atual = valor_inicial
    taxa_anual_decimal = taxa_anual_pct / 100

    print("\n--- Projeção do Investimento ---")
    for ano in range(1, num_anos + 1):
        juros_do_ano = valor_atual * taxa_anual_decimal
        valor_atual = valor_atual + juros_do_ano
        print(f"Ao final do Ano {ano}, o valor será de: R$ {valor_atual:.2f}")

    resposta = input("\nDeseja fazer uma nova simulação? (S/N): ")
    if resposta.upper() != 'S':
        break

print("\nPrograma de simulação encerrado. Obrigado por usar!")