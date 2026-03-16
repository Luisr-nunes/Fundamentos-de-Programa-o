
aporteInicial = float(input("Informe o valor do aporte inicial: "))
jurosAnual = float(input("Informe a taxa de juros ao ano:  "))
anosRetidos = float(input("Informe quantos anos deseja deixar o dinheiro rendendo: "))
correcaodojuros = jurosAnual / 100

print(f"Seu rendimento poderá ser de: {(aporteInicial * correcaodojuros) * anosRetidos + aporteInicial}")