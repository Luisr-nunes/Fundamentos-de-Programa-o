def menu():
    print("------ Loja de Peças ------")
    print("1 - Bateria")
    print("2 - Pneu")
    print("3 - Filtro de Óleo")
    print("4 - Pastilha de Freio")
    print("5 - Finalizar e Sair")


def definir(opcao: int, total: float):
    match opcao:
        case 1:
            print("Adicionado: Bateria (200.00 R$)")
            total += 200.00
        case 2:
            print("Adicionado: Pneu (350.00 R$)")
            total += 350.00
        case 3:
            print("Adicionado: Filtro de Óleo (50.00 R$)")
            total += 50.00
        case 4:
            print("Adicionado: Pastilha de Freio (100.00 R$)")
            total += 100.00
        case 5:
            print(f"Compra finalizada! Total: {total:.2f} R$")
            return False, total
        case _:
            print("Opção Inválida")
    print(f"Subtotal até agora: {total:.2f} R$")
    return True, total


def main():
    continuar = True
    total = 0.0
    while continuar:
        menu()
        try:
            entrada: str = input("Digite uma opção: ")
            opcao: int = int(entrada)
            continuar, total = definir(opcao, total)
        except ValueError:
            print("Digite apenas números válidos!")


main()
