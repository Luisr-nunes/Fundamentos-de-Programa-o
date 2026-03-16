    
qntAlunos = float(input("Informe a quantidade de alunos inscritos: "))
valorCamisetas = float(input("Informe o valor das Camisetas: "))
qntKitsCoffee = float(input("Informe a quantidade de Kits para o Coffe Break: "))
valorUnitKits = float(input("Informe o valor unitário dos Kits: "))
valorAluguel = float(input("Informe o valor do aluguel do auditório: "))
valorPatrocinio = float(input("Informe o valor do patrocínio: "))
    
totalGasto = valorCamisetas + (qntKitsCoffee * valorUnitKits) + valorAluguel
totalPpatrocinio = totalGasto - valorPatrocinio
valorPorAluno = totalPpatrocinio / qntAlunos

if (totalGasto > valorPatrocinio): 
    totalPpatrocinio = totalGasto - valorPatrocinio
    if not totalGasto: 0

if (qntAlunos > 0):
    valorPorAluno = totalPpatrocinio / qntAlunos
    if not valorPorAluno: 0

print("-----Dados do Evento-----")
print(f"O total gasto do evento foi: {totalGasto}")
print(f"O total após o patrocinio é: {totalPpatrocinio}")
print(f"O total por patrocinio foi: {valorPorAluno}")