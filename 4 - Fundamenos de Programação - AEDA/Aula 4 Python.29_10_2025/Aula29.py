temperaturas = []

while True:
    temp = float(input("Informe a temperatura: "))
    temperaturas.append(temp)
    resposta = input("Você deseja incluir outra temperatura? ")
    if resposta.lower() == "nao":
        break

media = sum(temperaturas)/len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

print("Temperatura média:", media)
print("\nTemperatura máxima:", maxima)
print("\nTemperatura mínima:", minima)
temperaturas.sort()
print(temperaturas)