print("--- Monitor de Produção Diária de Garrafas ---")
num_dias = int(input("Digite o número de dias que deseja registrar: "))

total_garrafas = 0

if num_dias <= 0:
    print("Erro: O número de dias deve ser maior que zero.")
else:
    for dia in range(num_dias):
        producao_do_dia = int(input(f"Digite a produção do Dia {dia + 1}: "))
        total_garrafas = total_garrafas + producao_do_dia

    media_diaria = total_garrafas / num_dias

    if media_diaria < 1000:
        mensagem_desempenho = "Produção baixa"
    elif media_diaria <= 2000:
        mensagem_desempenho = "Produção satisfatória"
    else:
        mensagem_desempenho = "Produção excelente"

    print("\n--- Relatório Final de Produção ---")
    print(f"Total de garrafas produzidas: {total_garrafas} unidades")
    print(f"Média de produção diária: {media_diaria:.2f} garrafas/dia")
    print(f"Desempenho da produção: {mensagem_desempenho}")