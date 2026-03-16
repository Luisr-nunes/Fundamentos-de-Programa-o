print("--- Calculadora de Pontos do App Vida Saudável ---")
horas_no_mes = float(input("Digite o total de horas de atividade física que você fez no mês: "))

if horas_no_mes < 0:
    print("\nErro: O número de horas inserido é inválido. Por favor, insira um valor positivo.")
else:
    pontos_finais = 0
    if horas_no_mes <= 10:
        pontos_finais = horas_no_mes * 2
    elif horas_no_mes <= 20:
        pontos_finais = horas_no_mes * 5
    else:
        pontos_finais = horas_no_mes * 10

    print("\n--- Sua Pontuação ---")
    print(f"Parabéns! Você acumulou um total de {pontos_finais} pontos este mês.")