aluno = []

while True:
    alunos ={}
    alunos["nome"] = input("Informe o nome do aluno: ")
    alunos["idade"] = int(input("Informe a idade do aluno: "))
    alunos["curso"] = input("Informe o curso do aluno: ")
    aluno.append(alunos)

    continuar = int(input("Deseja continuar cadastrando outro aluno (1 - sim / 2 - não): "))
    if continuar == 2:
        break

print("\n-----Dados do Aluno-----")
for a in aluno:
    print(f"Nome: {a['nome']} | Idade: {a['idade']} | Curso: {a['curso']}")
                                          
    