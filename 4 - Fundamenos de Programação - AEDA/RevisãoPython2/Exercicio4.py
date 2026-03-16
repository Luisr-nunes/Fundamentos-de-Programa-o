print("--- Análise de Consumo da Frota ---")
distancia_percorrida = float(input("Digite a distância total percorrida (em Km): "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto (em litros): "))


if combustivel_gasto <= 0:
    print("\nErro: A quantidade de combustível deve ser um valor positivo e maior que zero.")
else:
    consumo_medio = distancia_percorrida / combustivel_gasto
    if consumo_medio < 4:
        classificacao = "Muito ruim"
    elif consumo_medio <= 8:
        classificacao = "Ruim"
    elif consumo_medio <= 12:
        classificacao = "Regular"
    elif consumo_medio <= 14:
        classificacao = "Bom"
    else:
        classificacao = "Excelente"


    print("\n--- Relatório de Desempenho do Veículo ---")
    print(f"O consumo médio foi de: {consumo_medio:.2f} km/l")
    print(f"Classificação: {classificacao}")