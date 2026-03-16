# ARQUIVO 3: FUNÇÕES E ESCOPO
# Aprendendo a criar e usar funções em Python

print("=" * 50)
print("FUNÇÕES E ESCOPO EM PYTHON")
print("=" * 50)

# Exemplo 1: Função básica
print("\n1. FUNÇÕES BÁSICAS")
print("-" * 25)

def saudacao():
    print("Olá! Bem-vindo ao Python!")

# Chamando a função
saudacao()

# Exemplo 2: Função com parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem-vindo!")

saudacao_personalizada("Maria")
saudacao_personalizada("João")

# Exemplo 3: Função com múltiplos parâmetros
def apresentacao(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")
    print("-" * 20)

apresentacao("Ana", 25, "São Paulo")
apresentacao("Carlos", 30, "Rio de Janeiro")

# Exemplo 4: Função com valor de retorno
def soma(a, b):
    return a + b

resultado = soma(10, 5)
print(f"10 + 5 = {resultado}")

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media_aluno = calcular_media(8.5, 7.0, 9.5)
print(f"Média do aluno: {media_aluno:.2f}")

# Exemplo 5: Função com parâmetros default
def saudacao_completa(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

print(saudacao_completa("Maria"))  # Usa saudação default
print(saudacao_completa("João", "Bom dia"))  # Saudação personalizada

def criar_usuario(nome, idade=18, ativo=True):
    return {
        "nome": nome,
        "idade": idade,
        "ativo": ativo
    }

usuario1 = criar_usuario("Ana")
usuario2 = criar_usuario("Bruno", 25, False)
print(f"Usuário 1: {usuario1}")
print(f"Usuário 2: {usuario2}")

# Exemplo 6: Função com argumentos nomeados
def descrever_pessoa(nome, idade, profissao="desempregado", cidade="São Paulo"):
    return f"{nome} tem {idade} anos, é {profissao} e mora em {cidade}."

# Chamadas com argumentos nomeados
descricao1 = descrever_pessoa("Maria", 28)
descricao2 = descrever_pessoa("João", 35, profissao="engenheiro")
descricao3 = descrever_pessoa("Ana", 22, cidade="Rio", profissao="designer")

print(descricao1)
print(descricao2)
print(descricao3)

# Exemplo 7: Função com número variável de argumentos
def somar_todos(*numeros):
    total = sum(numeros)
    return total

print(f"Soma de 1, 2, 3: {somar_todos(1, 2, 3)}")
print(f"Soma de 10, 20, 30, 40, 50: {somar_todos(10, 20, 30, 40, 50)}")

def exibir_informacoes(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

print("\nInformações do usuário:")
exibir_informacoes(nome="Maria", idade=28, cidade="São Paulo", profissao="Engenheira")

# Exemplo 8: Função lambda (funções anônimas)
duplicar = lambda x: x * 2
print(f"Duplicar 5: {duplicar(5)}")

calcular_imposto = lambda salario: salario * 0.15 if salario > 5000 else salario * 0.10
print(f"Imposto sobre salário de 3000: {calcular_imposto(3000)}")
print(f"Imposto sobre salário de 8000: {calcular_imposto(8000)}")

# Exemplo 9: Escopo de variáveis
print("\n2. ESCOPO DE VARIÁVEIS")
print("-" * 25)

variavel_global = "Global"

def funcao_exemplo():
    variavel_local = "Local"
    print(f"Dentro da função: {variavel_local}")
    print(f"Acessando global dentro: {variavel_global}")

funcao_exemplo()
print(f"Fora da função: {variavel_global}")

# Erro: variavel_local não existe fora da função
try:
    print(variavel_local)
except NameError as e:
    print(f"Erro: {e}")

# Exemplo 10: Modificando variáveis globais
contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador dentro: {contador}")

print(f"\nContador inicial: {contador}")
incrementar()
incrementar()
print(f"Contador final: {contador}")

# Exemplo 11: Funções dentro de funções
def operacao_matematica(operador):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    
    def dividir(a, b):
        return a / b if b != 0 else "Erro: divisão por zero"
    
    if operador == "+":
        return somar
    elif operador == "-":
        return subtrair
    elif operador == "*":
        return multiplicar
    elif operador == "/":
        return dividir
    else:
        return None

# Usando a função
operacao = operacao_matematica("+")
print(f"\n5 + 3 = {operacao(5, 3)}")

operacao = operacao_matematica("*")
print(f"4 * 6 = {operacao(4, 6)}")

# Exemplo 12: Docstrings (documentação de funções)
def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    Args:
        peso (float): Peso da pessoa em quilogramas
        altura (float): Altura da pessoa em metros
    
    Returns:
        float: Valor do IMC calculado
        str: Classificação do IMC
    """
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    
    return imc, classificacao

# Usando a função com docstring
imc_resultado, classificacao = calcular_imc(70, 1.75)
print(f"\nIMC: {imc_resultado:.2f}")
print(f"Classificação: {classificacao}")

# Acessando a documentação
print(f"\nDocumentação da função:")
print(calcular_imc.__doc__)

# Exemplo 13: Recursão
print("\n3. RECURSÃO")
print("-" * 15)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fatorial de 5: {fatorial(5)}")
print(f"10º termo de Fibonacci: {fibonacci(10)}")

# Exemplo 14: Funções como objetos
def executar_operacao(funcao, a, b):
    return funcao(a, b)

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

print(f"\nExecutando operações:")
print(f"Adicionar: {executar_operacao(adicionar, 10, 5)}")
print(f"Subtrair: {executar_operacao(subtrair, 10, 5)}")

print("\n" + "=" * 50)
print("FIM DOS EXEMPLOS")
print("=" * 50)