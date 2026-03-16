# ARQUIVO 5: EXERCÍCIOS PRÁTICOS
# Coleção de exercícios para praticar Python

print("=" * 60)
print("EXERCÍCIOS PRÁTICOS DE PYTHON")
print("=" * 60)

# Exercício 1: Calculadora simples
print("\n1. CALCULADORA SIMPLES")
print("-" * 25)

def calculadora():
    print("Calculadora Simples")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"
    
    return f"Resultado: {num1} {operacao} {num2} = {resultado}"

# Exercício 2: Verificador de números primos
print("\n2. VERIFICADOR DE NÚMEROS PRIMOS")
print("-" * 35)

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def listar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Exercício 3: Sistema de notas
print("\n3. SISTEMA DE NOTAS")
print("-" * 20)

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def sistema_notas():
    nome = input("Nome do aluno: ")
    notas = []
    
    for i in range(3):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)
    
    print(f"\nAluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

# Exercício 4: Jogo de adivinhação
print("\n4. JOGO DE ADIVINHAÇÃO")
print("-" * 25)

import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    print("Jogo de Adivinhação!")
    print(f"Tente adivinhar o número entre 1 e 100.")
    print(f"Você tem {max_tentativas} tentativas.")
    
    while tentativas < max_tentativas:
        palpite = int(input(f"\nTentativa {tentativas + 1}: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            return
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
    
    print(f"\nGame Over! O número era {numero_secreto}.")

# Exercício 5: Gerenciador de tarefas
print("\n5. GERENCIADOR DE TAREFAS")
print("-" * 30)

def gerenciador_tarefas():
    tarefas = []
    
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append({"descricao": tarefa, "concluida": False})
            print("Tarefa adicionada!")
        
        elif opcao == "2":
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(tarefas):
                status = "✓" if tarefa["concluida"] else "○"
                print(f"{i+1}. {status} {tarefa['descricao']}")
        
        elif opcao == "3":
            listar_tarefas()
            indice = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["concluida"] = True
                print("Tarefa marcada como concluída!")
            else:
                print("Índice inválido!")
        
        elif opcao == "4":
            listar_tarefas()
            indice = int(input("Digite o número da tarefa para remover: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                print("Tarefa removida!")
            else:
                print("Índice inválido!")
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

def listar_tarefas():
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["concluida"] else "○"
        print(f"{i+1}. {status} {tarefa['descricao']}")

# Exercício 6: Conversor de temperaturas
print("\n6. CONVERSOR DE TEMPERATURAS")
print("-" * 35)

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def conversor_temperatura():
    print("Conversor de Temperaturas")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    
    opcao = input("Escolha a conversão: ")
    temperatura = float(input("Digite a temperatura: "))
    
    if opcao == "1":
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"{temperatura}°C = {resultado:.2f}°F")
    elif opcao == "2":
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"{temperatura}°F = {resultado:.2f}°C")
    elif opcao == "3":
        resultado = celsius_para_kelvin(temperatura)
        print(f"{temperatura}°C = {resultado:.2f}K")
    elif opcao == "4":
        resultado = kelvin_para_celsius(temperatura)
        print(f"{temperatura}K = {resultado:.2f}°C")
    else:
        print("Opção inválida!")

# Exercício 7: Análise de texto
print("\n7. ANÁLISE DE TEXTO")
print("-" * 25)

def analisar_texto(texto):
    palavras = texto.split()
    
    # Contar caracteres (sem espaços)
    caracteres_sem_espacos = len(texto.replace(" ", ""))
    
    # Contar palavras
    num_palavras = len(palavras)
    
    # Contar frases (terminadas em . ! ?)
    num_frases = sum(texto.count(ponto) for ponto in ['.', '!', '?'])
    
    # Palavra mais longa
    palavra_longa = max(palavras, key=len) if palavras else ""
    
    # Frequência de palavras
    frequencia = {}
    for palavra in palavras:
        palavra = palavra.lower().strip('.,!?;:')
        if palavra:
            frequencia[palavra] = frequencia.get(palavra, 0) + 1
    
    return {
        "caracteres": len(texto),
        "caracteres_sem_espacos": caracteres_sem_espacos,
        "palavras": num_palavras,
        "frases": num_frases,
        "palavra_longa": palavra_longa,
        "frequencia": frequencia
    }

# Exercício 8: Validador de CPF
print("\n8. VALIDADOR DE CPF")
print("-" * 25)

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False
    
    # Calcula primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
    
    if int(cpf[9]) != digito1:
        return False
    
    # Calcula segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0
    
    return int(cpf[10]) == digito2

# Exercício 9: Jogo da forca
print("\n9. JOGO DA FORCA")
print("-" * 20)

def jogo_forca():
    palavras = ["python", "programacao", "computador", "algoritmo", "variavel"]
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    letras_erradas = []
    tentativas = 6
    
    print("Jogo da Forca!")
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    
    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
        
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra!")
            continue
        
        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra!")
            continue
        
        if letra in palavra_secreta:
            for i, letra_palavra in enumerate(palavra_secreta):
                if letra_palavra == letra:
                    letras_descobertas[i] = letra
            print("Boa! Letra encontrada!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra não encontrada!")
    
    if "_" not in letras_descobertas:
        print(f"\nParabéns! Você ganhou! A palavra era {palavra_secreta}.")
    else:
        print(f"\nGame Over! A palavra era {palavra_secreta}.")

# Exercício 10: Sistema bancário simples
print("\n10. SISTEMA BANCÁRIO SIMPLES")
print("-" * 35)

def sistema_bancario():
    contas = {}
    
    while True:
        print("\n=== SISTEMA BANCÁRIO ===")
        print("1. Criar conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Ver saldo")
        print("5. Listar contas")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do titular: ")
            numero = input("Número da conta: ")
            if numero in contas:
                print("Conta já existe!")
            else:
                contas[numero] = {"titular": nome, "saldo": 0.0}
                print("Conta criada com sucesso!")
        
        elif opcao == "2":
            numero = input("Número da conta: ")
            if numero in contas:
                valor = float(input("Valor do depósito: "))
                if valor > 0:
                    contas[numero]["saldo"] += valor
                    print(f"Depósito de R${valor:.2f} realizado!")
                else:
                    print("Valor inválido!")
            else:
                print("Conta não encontrada!")
        
        elif opcao == "3":
            numero = input("Número da conta: ")
            if numero in contas:
                valor = float(input("Valor do saque: "))
                if valor > 0 and valor <= contas[numero]["saldo"]:
                    contas[numero]["saldo"] -= valor
                    print(f"Saque de R${valor:.2f} realizado!")
                else:
                    print("Saldo insuficiente ou valor inválido!")
            else:
                print("Conta não encontrada!")
        
        elif opcao == "4":
            numero = input("Número da conta: ")
            if numero in contas:
                conta = contas[numero]
                print(f"Titular: {conta['titular']}")
                print(f"Saldo: R${conta['saldo']:.2f}")
            else:
                print("Conta não encontrada!")
        
        elif opcao == "5":
            print("\nContas cadastradas:")
            for numero, conta in contas.items():
                print(f"Conta {numero}: {conta['titular']} - R${conta['saldo']:.2f}")
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

# Função principal para executar os exercícios
def menu_principal():
    while True:
        print("\n" + "=" * 60)
        print("MENU DE EXERCÍCIOS")
        print("=" * 60)
        print("1. Calculadora Simples")
        print("2. Verificador de Números Primos")
        print("3. Sistema de Notas")
        print("4. Jogo de Adivinhação")
        print("5. Gerenciador de Tarefas")
        print("6. Conversor de Temperaturas")
        print("7. Análise de Texto")
        print("8. Validador de CPF")
        print("9. Jogo da Forca")
        print("10. Sistema Bancário")
        print("0. Sair")
        
        opcao = input("\nEscolha um exercício: ")
        
        if opcao == "1":
            print(calculadora())
        elif opcao == "2":
            num = int(input("Digite um número para verificar se é primo: "))
            print(f"{num} é primo? {eh_primo(num)}")
            
            limite = int(input("Digite um limite para listar números primos: "))
            primos = listar_primos(limite)
            print(f"Números primos até {limite}: {primos}")
        elif opcao == "3":
            sistema_notas()
        elif opcao == "4":
            jogo_adivinhacao()
        elif opcao == "5":
            gerenciador_tarefas()
        elif opcao == "6":
            conversor_temperatura()
        elif opcao == "7":
            texto = input("Digite um texto para analisar: ")
            resultado = analisar_texto(texto)
            print(f"\nAnálise do texto:")
            print(f"Caracteres: {resultado['caracteres']}")
            print(f"Caracteres (sem espaços): {resultado['caracteres_sem_espacos']}")
            print(f"Palavras: {resultado['palavras']}")
            print(f"Frases: {resultado['frases']}")
            print(f"Palavra mais longa: {resultado['palavra_longa']}")
            print("Frequência de palavras:")
            for palavra, freq in resultado['frequencia'].items():
                print(f"  {palavra}: {freq}")
        elif opcao == "8":
            cpf = input("Digite um CPF para validar: ")
            print(f"CPF válido? {validar_cpf(cpf)}")
        elif opcao == "9":
            jogo_forca()
        elif opcao == "10":
            sistema_bancario()
        elif opcao == "0":
            print("Obrigado por praticar Python!")
            break
        else:
            print("Opção inválida!")

# Executar o menu principal
if __name__ == "__main__":
    menu_principal()