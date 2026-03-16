def ler_medida_valida(nome_da_medida):
    while True:
        medida = float(input(f"Digite a {nome_da_medida} da parede em metros: "))
        if medida > 0:
            return medida
        else:
            print("Valor inválido! A medida deve ser maior que zero. Tente novamente.")

print("--- Calculadora de Tinta ---")
largura = ler_medida_valida("largura")
altura = ler_medida_valida("altura")

area_total = largura * altura
latas_calculadas = area_total / 10
latas_inteiras = int(latas_calculadas)
if latas_calculadas > latas_inteiras:
    latas_necessarias = latas_inteiras + 1
else:
    latas_necessarias = latas_inteiras


print("\n--- Relatório da Pintura ---")
print(f"Dimensões da parede: {largura:.2f}m de largura e {altura:.2f}m de altura.")
print(f"A área total a ser pintada é de: {area_total:.2f} m².")
print(f"Será(ão) necessária(s) {latas_necessarias} lata(s) de tinta para cobrir a parede.")