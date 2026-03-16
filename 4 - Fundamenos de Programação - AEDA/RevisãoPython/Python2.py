largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

# Validação simples (sem try/except, como solicitado)
if largura <= 0 or altura <= 0:
    print("Largura e altura devem ser maiores que zero.")
else:
    # Calcula a área
    area_total = largura * altura

    # Cada lata pinta 10 metros quadrados
    cobertura_por_lata = 10.0

    # Quantidade exata (pode ser decimal)
    qnt_latas_decimal = area_total / cobertura_por_lata

    # Parte inteira (por exemplo, int(2.3) == 2)
    parte_inteira = int(qnt_latas_decimal)

    # Se houver qualquer parte decimal > 0, precisamos de mais 1 lata
    if qnt_latas_decimal > parte_inteira:
        latas = parte_inteira + 1
    else:
        latas = parte_inteira

    print("-----Resultado-----")
    print(f"Largura da parede é: {largura}")
    print(f"Altura da parede é: {altura}")
    print(f"Área total da parede é: {area_total}")
    # 'latas' é inteiro e já está arredondado para cima quando necessário
    print(f"Quantidade de latas necessárias: {latas}")


