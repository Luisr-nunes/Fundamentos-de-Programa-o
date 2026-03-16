print("Cadastro de 5 pessoas - Idade e Sexo")

N = 5
homens = 0
soma_idades = 0
maior_mulher = 0  # 0 indica que ainda não houve mulher cadastrada
mulheres_acima_20 = 0

for i in range(1, N + 1):
    print(f"\nPessoa {i}:")
    idade = int(input("Informe a idade: "))

    # pega apenas o primeiro caractere e valida
    sexo = input("Informe o sexo (M/F): ").strip().upper()
    while not sexo or sexo[0] not in ("M", "F"):
        sexo = input("Entrada inválida. Digite 'M' para masculino ou 'F' para feminino: ").strip().upper()
    sexo = sexo[0]

    soma_idades += idade

    if sexo == "M":
        homens += 1
    else:  # mulher
        if idade > maior_mulher:
            maior_mulher = idade
        if idade > 20:
            mulheres_acima_20 += 1

media = soma_idades / N

print("\n----- Resultado -----")
print(f"a) Quantos homens foram cadastrados: {homens}")
if maior_mulher == 0:
    print("b) Não houve mulheres cadastradas.")
else:
    print(f"b) Idade da mulher mais velha: {maior_mulher}")
print(f"c) Média de idade do grupo: {media:.2f}")
print(f"d) Quantas mulheres têm mais de 20 anos: {mulheres_acima_20}")