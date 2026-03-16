print("--- Controle de Certificados do Curso de Tecnologia ---")
total_alunos = int(input("Digite o número total de alunos na turma: "))

alunos_com_certificado = 0
lista_nomes_aprovados = ""

if total_alunos > 0:
    for i in range(total_alunos):
        print(f"\n--- Aluno {i + 1} de {total_alunos} ---")
        nome = input("Digite o nome do aluno: ")
        presencas = int(input(f"Digite a quantidade de encontros que {nome} frequentou (0 a 10): "))

        if presencas >= 6:
            alunos_com_certificado = alunos_com_certificado + 1
            lista_nomes_aprovados = lista_nomes_aprovados + nome + "\n"

    percentual_aprovados = (alunos_com_certificado / total_alunos) * 100

    print("\n--- Relatório Final ---")
    print("Alunos com direito ao certificado:")
    if lista_nomes_aprovados == "":
        print("Nenhum aluno atingiu a frequência mínima.")
    else:
        print(lista_nomes_aprovados)

    print(f"Porcentagem de alunos com direito ao certificado: {percentual_aprovados:.2f}%")

else:
    print("Nenhum aluno foi inserido. O programa será encerrado.")