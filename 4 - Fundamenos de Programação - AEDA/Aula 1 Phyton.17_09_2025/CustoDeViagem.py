distancia = float(input("Informe a Distância da viagem em KM: "))
consumo = float(input("Informe o consumo médio de gasolina por KM: "))
valorlitro = float(input("Informe o valor do litro de gasolina: "))

litrosdegasolina = distancia / consumo
custototal = litrosdegasolina * valorlitro

print (f"Você precisará de {litrosdegasolina} litros de gasolina")
print (f"O custo total de viagem será R$: {custototal}")

