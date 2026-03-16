print("Controle de Presença - Curso Gratuito de Tecnologia")

# Quantos alunos existem
numero_alunos = int(input("Informe o número total de alunos: "))

aprovados = []  # lista de nomes com direito ao certificado

for i in range(1, numero_alunos + 1):
    print(f"\nAluno {i} de {numero_alunos}")
    nome = input("Nome do aluno: ").strip()

    # lê a quantidade de encontros assistidos e valida (0 a 10)
    encontros = int(input("Quantidade de encontros frequentados (0 a 10): "))
    while encontros < 0 or encontros > 10:
        print("Valor inválido. Digite um número entre 0 e 10.")
        encontros = int(input("Quantidade de encontros frequentados (0 a 10): "))

    # Regra: para receber o certificado precisa ter participado de pelo menos 6 encontros
    if encontros >= 6:
        aprovados.append(nome)

# Resultado
print("\n----- Resultado -----")
if aprovados:
    print("Alunos com direito ao certificado:")
    for nome in aprovados:
        print("-", nome)
else:
    print("Nenhum aluno tem direito ao certificado.")

porcentagem = (len(aprovados) / numero_alunos) * 100 if numero_alunos > 0 else 0
print(f"Porcentagem de alunos aprovados: {porcentagem:.2f}%")

# Observação: o enunciado menciona '4 encontros ou mais' em uma linha confusa,
# mas a regra principal diz 'pelo menos 6 encontros' para receber o certificado.
# Se quiser usar 4 como critério, altere o valor 6 na linha acima para 4.
