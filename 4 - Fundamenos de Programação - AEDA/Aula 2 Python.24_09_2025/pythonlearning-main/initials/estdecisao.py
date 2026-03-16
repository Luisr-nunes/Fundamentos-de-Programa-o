idade = int(input(f"Digite sua idade: "))

if idade < 16:
    print("Não eleitor")
elif 16 <= idade < 18 or idade > 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")