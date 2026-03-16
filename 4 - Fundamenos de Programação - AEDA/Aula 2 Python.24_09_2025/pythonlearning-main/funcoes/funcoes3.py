def menu():
    print("------ Loja de Peças ------")
    print("1 - Bateria")
    print("2 - Pneu")
    print("3 - Filtro de Óleo")
    print("4 - Pastilha de Freio")
    print("5 - Sair")


def definir(opcao):
    match opcao:
        case 1:
            print("O valor da Bateria é: 200.00 R$")
            return False
        case 2:
            print("350.00 R$")
            return False
        case 3:
            print("50.00 R$")
            return False
        case 4:
            print("100.00 R$")
            return False
        case 5:
            print()
            return False
        case _:
            print("Opção Inválida")
    return True


def main():
    menu()
    opcao = int(input("Digite uma opção: "))
    if definir(opcao):
        main()


main()
