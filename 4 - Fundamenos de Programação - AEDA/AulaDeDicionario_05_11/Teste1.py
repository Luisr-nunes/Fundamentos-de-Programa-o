aluno = {}

aluno["nome"] = input("Informe o nome do aluno: ")
aluno["idade"] = int(input("Informe a idade do aluno: "))
aluno["curso"] = input("Informe o curso do aluno: ")

print("\n-----Dados do Aluno-----")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")