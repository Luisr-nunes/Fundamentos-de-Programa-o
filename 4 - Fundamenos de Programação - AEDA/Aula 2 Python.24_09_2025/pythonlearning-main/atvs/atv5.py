peso = float(input(f"Digite seu peso(kg): "))
altura = float(input(f"Digite sua altura(m): "))
IMC = peso / (altura ** 2)

print(f"Seu IMC é: {IMC:.2f}")