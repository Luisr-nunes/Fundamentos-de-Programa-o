total_homens = 0
idade_mulher_mais_velha = 0
soma_idades_grupo = 0
mulheres_mais_de_20 = 0

print("--- Análise de Dados do Grupo ---")
print("Por favor, insira a idade e o sexo de 5 pessoas.")

for i in range(5):
    print(f"\n--- Pessoa {i + 1} de 5 ---")
    idade = int(input("Digite a idade: "))
    sexo = ''
    while sexo not in ('M', 'F'):
        sexo = input("Digite o sexo (M/F): ").upper()
        if sexo not in ('M', 'F'):
            print("Entrada inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")

    soma_idades_grupo = soma_idades_grupo + idade

    if sexo == 'M':
        total_homens = total_homens + 1
    elif sexo == 'F':
        if idade > idade_mulher_mais_velha:
            idade_mulher_mais_velha = idade
        if idade > 20:
            mulheres_mais_de_20 = mulheres_mais_de_20 + 1

media_idade_grupo = soma_idades_grupo / 5

print("\n--- Resultados da Análise ---")
print(f"a) Total de homens cadastrados: {total_homens}")
print(f"b) Idade da mulher mais velha: {idade_mulher_mais_velha} anos")
print(f"c) Média de idade do grupo: {media_idade_grupo:.1f} anos")
print(f"d) Mulheres com mais de 20 anos: {mulheres_mais_de_20}")