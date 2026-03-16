# ARQUIVO 1: CONCEITOS BÁSICOS
# Aprendendo print, variáveis e operações

# Exemplo 1: Print básico
print("Olá, mundo!")
print("Bem-vindo ao Python!")

# Exemplo 2: Variáveis e tipos de dados
# String (texto)
nome = "Maria"
idade = 25
altura = 1.68
estudante = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"É estudante: {estudante}")

# Exemplo 3: Operações matemáticas
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(f"Soma: {a} + {b} = {soma}")
print(f"Subtração: {a} - {b} = {subtracao}")
print(f"Multiplicação: {a} × {b} = {multiplicacao}")
print(f"Divisão: {a} ÷ {b} = {divisao}")
print(f"Divisão inteira: {a} // {b} = {divisao_inteira}")
print(f"Resto da divisão: {a} % {b} = {resto}")
print(f"Potência: {a}^{b} = {potencia}")

# Exemplo 4: Entrada de dados
nome_usuario = input("Qual é o seu nome? ")
idade_usuario = int(input("Qual é a sua idade? "))
peso = float(input("Qual é o seu peso? "))

print(f"\nOlá {nome_usuario}!")
print(f"Você tem {idade_usuario} anos e pesa {peso} kg.")

# Exemplo 5: Conversão entre tipos
numero_str = "42"
numero_int = int(numero_str)
numero_float = float(numero_int)

print(f"String: {numero_str} (tipo: {type(numero_str)})")
print(f"Inteiro: {numero_int} (tipo: {type(numero_int)})")
print(f"Float: {numero_float} (tipo: {type(numero_float)})")

# Exemplo 6: Operadores de comparação
x = 10
y = 20

print(f"{x} == {y}: {x == y}")      # Igual
print(f"{x} != {y}: {x != y}")      # Diferente
print(f"{x} > {y}: {x > y}")        # Maior
print(f"{x} < {y}: {x < y}")        # Menor
print(f"{x} >= {y}: {x >= y}")      # Maior ou igual
print(f"{x} <= {y}: {x <= y}")      # Menor ou igual

# Exemplo 7: Operadores lógicos
tem_sol = True
tem_chuva = False

print(f"Tem sol E tem chuva: {tem_sol and tem_chuva}")
print(f"Tem sol OU tem chuva: {tem_sol or tem_chuva}")
print(f"NÃO tem sol: {not tem_sol}")