print("--- Orçamento da Semana de Tecnologia ---")

qtd_alunos = int(input("Digite a quantidade de alunos inscritos: "))

valor_camisetas = float(input("Digite o valor total das camisetas: R$ "))
qtd_kits_coffee = int(input("Digite a quantidade de kits de coffee break: "))
valor_unitario_kit = float(input("Digite o valor unitário de cada kit: R$ "))
valor_aluguel = float(input("Digite o valor do aluguel do auditório: R$ "))
valor_patrocinio = float(input("Digite o valor do patrocínio recebido: R$ "))

custo_total_kits = qtd_kits_coffee * valor_unitario_kit

total_gasto = valor_camisetas + custo_total_kits + valor_aluguel

if valor_patrocinio >= total_gasto:
    total_apos_patrocinio = 0.0
else:
    total_apos_patrocinio = total_gasto - valor_patrocinio

taxa_por_aluno = total_apos_patrocinio / qtd_alunos

print("\n--- Resultado Final do Orçamento ---")
print(f"O custo total do evento é: R$ {total_gasto:.2f}")
print(f"O custo total após o patrocínio é: R$ {total_apos_patrocinio:.2f}")
print(f"A taxa por aluno será de: R$ {taxa_por_aluno:.2f}")