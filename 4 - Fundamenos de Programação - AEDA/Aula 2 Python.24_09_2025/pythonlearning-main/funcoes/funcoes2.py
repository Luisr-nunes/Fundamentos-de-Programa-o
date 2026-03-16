def menu():
    print("------ Módulo Cliente ------")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Excluir Cliente")
    print("4 - Sair")


def definir(opcao):
    match opcao:
        case 1:
            print("Cadastrando Cliente...")
        case 2:
            print("Listando os Clientes...")
        case 3:
            print("Excluindo o Cliente...")
        case 4:
            print("Saindo do programa...")
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
