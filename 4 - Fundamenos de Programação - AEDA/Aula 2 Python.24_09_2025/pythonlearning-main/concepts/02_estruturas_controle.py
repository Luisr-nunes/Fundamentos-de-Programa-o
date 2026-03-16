# ARQUIVO 2: ESTRUTURAS DE CONTROLE
# Aprendendo if/else, for e while

print("=" * 50)
print("ESTRUTURAS DE CONTROLE EM PYTHON")
print("=" * 50)

# Exemplo 1: Estrutura if/elif/else
print("\n1. ESTRUTURAS CONDICIONAIS (if/elif/else)")
print("-" * 30)

idade = 18

if idade < 0:
    print("Idade inválida!")
elif idade < 12:
    print("Você é uma criança")
elif idade < 18:
    print("Você é um adolescente")
elif idade < 65:
    print("Você é um adulto")
else:
    print("Você é um idoso")

# Testando múltiplas condições
nota = 75

if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
elif nota >= 60:
    conceito = "D"
else:
    conceito = "F"

print(f"Nota: {nota} - Conceito: {conceito}")

# Exemplo 2: Operador ternário
idade = 20
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Status: {status}")

# Exemplo 3: Estrutura for
print("\n2. ESTRUTURA FOR")
print("-" * 20)

# Loop com range
print("Contagem de 1 a 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Loop com string
print("\nLetras da palavra 'Python':")
for letra in "Python":
    print(letra, end=" ")
print()

# Loop com enumerate
print("\nNomes com índices:")
nomes = ["Ana", "Bruno", "Carla", "Daniel"]
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")

# Loop com múltiplos iteráveis
print("\nNomes e idades:")
idades = [25, 30, 22, 28]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# Loop com break e continue
print("\nNúmeros pares de 1 a 10:")
for num in range(1, 11):
    if num % 2 != 0:
        continue  # Pula números ímpares
    print(num, end=" ")
print()

print("\nParando no número 7:")
for num in range(1, 20):
    if num == 7:
        break  # Para o loop
    print(num, end=" ")
print()

# Loop aninhados
print("\nTabuada de multiplicação:")
for i in range(1, 6):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()

# Exemplo 4: Estrutura while
print("\n3. ESTRUTURA WHILE")
print("-" * 20)

# Contagem regressiva
print("Contagem regressiva:")
contador = 5
while contador >= 0:
    print(contador, end=" ")
    contador -= 1
print("FIM!")

# Validação de entrada
print("\nValidação de senha:")
senha_correta = "12345"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso concedido!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativas restantes: {max_tentativas - tentativas}")

if tentativas == max_tentativas:
    print("Acesso bloqueado!")

# Menu interativo
print("\n4. MENU INTERATIVO")
print("-" * 20)

while True:
    print("\nMENU PRINCIPAL")
    print("1. Calcular área do quadrado")
    print("2. Calcular área do círculo")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        lado = float(input("Digite o lado do quadrado: "))
        area = lado ** 2
        print(f"Área do quadrado: {area:.2f}")
    elif opcao == "2":
        raio = float(input("Digite o raio do círculo: "))
        area = 3.14159 * (raio ** 2)
        print(f"Área do círculo: {area:.2f}")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

# Exemplo 5: Compreensão de listas (list comprehension)
print("\n5. COMPREENSÃO DE LISTAS")
print("-" * 30)

# Quadrados dos números de 1 a 10
quadrados = [x**2 for x in range(1, 11)]
print(f"Quadrados: {quadrados}")

# Números pares de 1 a 20
pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Números pares: {pares}")

# Nomes que começam com vogal
vogais_nomes = [nome for nome in nomes if nome[0].upper() in "AEIO"]
print(f"Nomes com vogal: {vogais_nomes}")

print("\n" + "=" * 50)
print("FIM DOS EXEMPLOS")
print("=" * 50)