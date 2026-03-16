DistanciaTotal = int(input("Digite a distancia total da viagem em (km): "))
ConsumoMedio = int(input("Digite o consumo medio do carro em (km/l): "))
PrecoGasolina = float(input("Digite o preço da gasolina em (R$): "))

print(f"Você precisará de {DistanciaTotal / ConsumoMedio:.2f} litros de gasolina e o custo dessa viagem será de R$ {(DistanciaTotal / ConsumoMedio) * PrecoGasolina:.2f}")