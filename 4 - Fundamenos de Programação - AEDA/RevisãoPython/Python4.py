
distanciaPercorrida = float(input("Informe a distancia total percorrida: "))
qntCombustGasto = float(input("Informe a quantidade de combustivel gasto: "))

if qntCombustGasto <= 0:
    print("O valor fornecido deve ser maior que 0")
    
else:
    consumomedio = distanciaPercorrida / qntCombustGasto
    print(f"consumo médio foi de: {consumomedio} Km/L")
    
    if consumomedio <= 4:
        print("Consumo médio: Muito ruim")
    elif consumomedio <= 8:
        print("Consumo médio: Ruim")
    elif consumomedio <= 12:
        print("Consumo médio: Regular")
    elif consumomedio <= 14:
        print("Consumo médio: Bom")
    else:
        print("Consumo médio: Excelente")
