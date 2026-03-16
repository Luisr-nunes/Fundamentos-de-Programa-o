# ARQUIVO 4: LISTAS E ESTRUTURAS DE DADOS
# Aprendendo a trabalhar com listas, tuplas, dicionários e conjuntos

print("=" * 60)
print("LISTAS E ESTRUTURAS DE DADOS EM PYTHON")
print("=" * 60)

# Exemplo 1: Listas básicas
print("\n1. LISTAS BÁSICAS")
print("-" * 20)

# Criando listas
frutas = ["maçã", "banana", "laranja", "uva"]
numeros = [1, 2, 3, 4, 5]
misturada = [1, "dois", 3.0, True, [1, 2, 3]]

print(f"Lista de frutas: {frutas}")
print(f"Lista de números: {numeros}")
print(f"Lista misturada: {misturada}")

# Acessando elementos
print(f"\nPrimeira fruta: {frutas[0]}")
print(f"Última fruta: {frutas[-1]}")
print(f"Segunda fruta: {frutas[1]}")
print(f"Penúltima fruta: {frutas[-2]}")

# Fatiamento (slicing)
print(f"\nFrutas do índice 1 ao 3: {frutas[1:3]}")
print(f"Frutas do início ao índice 2: {frutas[:2]}")
print(f"Frutas do índice 2 ao final: {frutas[2:]}")
print(f"Todas as frutas: {frutas[:]}")

# Exemplo 2: Métodos de listas
print("\n2. MÉTODOS DE LISTAS")
print("-" * 25)

# Adicionando elementos
alunos = ["Ana", "Bruno"]
print(f"Lista inicial: {alunos}")

alunos.append("Carlos")  # Adiciona no final
print(f"Após append: {alunos}")

alunos.insert(1, "Daniel")  # Insere na posição específica
print(f"Após insert: {alunos}")

# Removendo elementos
alunos.remove("Bruno")  # Remove pelo valor
print(f"Após remove: {alunos}")

removido = alunos.pop()  # Remove e retorna o último
print(f"Após pop: {alunos}")
print(f"Elemento removido: {removido}")

removido = alunos.pop(0)  # Remove e retorna pelo índice
print(f"Após pop(0): {alunos}")
print(f"Elemento removido: {removido}")

# Ordenação
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nNúmeros originais: {numeros}")

numeros.sort()  # Ordena em ordem crescente
print(f"Ordenados: {numeros}")

numeros.sort(reverse=True)  # Ordena em ordem decrescente
print(f"Ordenados decrescente: {numeros}")

# Outros métodos úteis
print(f"Comprimento da lista: {len(numeros)}")
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")
print(f"Soma: {sum(numeros)}")

# Contando elementos
lista_numeros = [1, 2, 2, 3, 3, 3, 4]
print(f"\nLista: {lista_numeros}")
print(f"Quantidade de 2's: {lista_numeros.count(2)}")
print(f"Índice do primeiro 3: {lista_numeros.index(3)}")

# Exemplo 3: Tuplas (imutáveis)
print("\n3. TUPLAS")
print("-" * 15)

# Criando tuplas
coordenadas = (10, 20)
ponto = (5,)
rgb = (255, 0, 0)
meses = ("Jan", "Fev", "Mar", "Abr")

print(f"Coordenadas: {coordenadas}")
print(f"Ponto: {ponto}")
print(f"RGB: {rgb}")
print(f"Meses: {meses}")

# Acessando elementos
print(f"\nPrimeiro mês: {meses[0]}")
print(f"Último mês: {meses[-1]}")
print(f"Coordenada X: {coordenadas[0]}")
print(f"Coordenada Y: {coordenadas[1]}")

# Desempacotamento de tuplas
x, y = coordenadas
print(f"\nDesempacotado: x={x}, y={y}")

a, b, c = rgb
print(f"RGB: R={a}, G={b}, B={c}")

# Exemplo 4: Dicionários
print("\n4. DICIONÁRIOS")
print("-" * 15)

# Criando dicionários
pessoa = {
    "nome": "Maria Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheira"
}

print(f"Dicionário pessoa: {pessoa}")

# Acessando valores
print(f"\nNome: {pessoa['nome']}")
print(f"Idade: {pessoa.get('idade')}")
print(f"Cidade: {pessoa.get('cidade', 'Não informado')}")

# Adicionando e atualizando
pessoa["email"] = "maria@email.com"  # Adiciona nova chave
pessoa["idade"] = 31  # Atualiza valor existente

print(f"\nDicionário atualizado: {pessoa}")

# Removendo elementos
del pessoa["profissao"]
print(f"Após remover profissão: {pessoa}")

email_removido = pessoa.pop("email")
print(f"Email removido: {email_removido}")
print(f"Dicionário final: {pessoa}")

# Métodos úteis
print(f"\nChaves: {list(pessoa.keys())}")
print(f"Valores: {list(pessoa.values())}")
print(f"Itens: {list(pessoa.items())}")
print(f"Comprimento: {len(pessoa)}")

# Exemplo 5: Conjuntos (Sets)
print("\n5. CONJUNTOS (SETS)")
print("-" * 20)

# Criando conjuntos
frutas_set = {"maçã", "banana", "laranja"}
numeros_set = {1, 2, 3, 4, 5, 5, 4, 3}  # Remove duplicatas

print(f"Conjunto de frutas: {frutas_set}")
print(f"Conjunto de números: {numeros_set}")

# Operações com conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

print(f"\nConjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")

# União
print(f"União: {conjunto_a | conjunto_b}")
print(f"União (método): {conjunto_a.union(conjunto_b)}")

# Interseção
print(f"Interseção: {conjunto_a & conjunto_b}")
print(f"Interseção (método): {conjunto_a.intersection(conjunto_b)}")

# Diferença
print(f"Diferença A - B: {conjunto_a - conjunto_b}")
print(f"Diferença B - A: {conjunto_b - conjunto_a}")

# Adicionando e removendo
conjunto_a.add(7)
print(f"\nApós adicionar 7: {conjunto_a}")

conjunto_a.remove(1)
print(f"Após remover 1: {conjunto_a}")

# Exemplo 6: List comprehension avançado
print("\n6. LIST COMPREHENSION AVANÇADO")
print("-" * 35)

# Com condições
numeros = range(1, 21)
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
multiplos_3 = [x for x in numeros if x % 3 == 0]

print(f"Numeros de 1 a 20: {list(numeros)}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Múltiplos de 3: {multiplos_3}")

# Com if/else
classificacao = ["par" if x % 2 == 0 else "ímpar" for x in range(1, 11)]
print(f"\nClassificação: {classificacao}")

# Com múltiplas condições
numeros_especiais = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print(f"Números divisíveis por 3 e 5: {numeros_especiais}")

# Exemplo 7: Estruturas aninhadas
print("\n7. ESTRUTURAS ANINHADAS")
print("-" * 25)

# Lista de dicionários
alunos = [
    {"nome": "Ana", "idade": 20, "notas": [8.5, 7.0, 9.0]},
    {"nome": "Bruno", "idade": 22, "notas": [6.0, 8.5, 7.5]},
    {"nome": "Carla", "idade": 21, "notas": [9.0, 9.5, 8.0]}
]

print("Lista de alunos:")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{aluno['nome']} - {aluno['idade']} anos - Média: {media:.2f}")

# Dicionário com listas
estoque = {
    "frutas": ["maçã", "banana", "laranja"],
    "verduras": ["alface", "tomate", "cenoura"],
    "grãos": ["arroz", "feijão", "milho"]
}

print("\nEstoque:")
for categoria, itens in estoque.items():
    print(f"{categoria}: {', '.join(itens)}")

# Exemplo 8: Métodos úteis para strings
print("\n8. MÉTODOS ÚTEIS PARA STRINGS")
print("-" * 30)

texto = "  Python é incrível!  "
print(f"Texto original: '{texto}'")
print(f"Strip (remove espaços): '{texto.strip()}'")
print(f"Upper (maiúsculas): '{texto.upper()}'")
print(f"Lower (minúsculas): '{texto.lower()}'")
print(f"Title (título): '{texto.title()}'")

# Dividindo e juntando
frase = "Python é uma linguagem de programação"
palavras = frase.split()
print(f"\nFrase: {frase}")
print(f"Palavras: {palavras}")
print(f"Junta com '_': '{'_'.join(palavras)}'")

# Substituição
print(f"\nSubstituir 'Python' por 'Java': {frase.replace('Python', 'Java')}")
print(f"Começa com 'Python': {frase.startswith('Python')}")
print(f"Termina com 'programação': {frase.endswith('programação')}")
print(f"Contém 'linguagem': {'linguagem' in frase}")

print("\n" + "=" * 60)
print("FIM DOS EXEMPLOS")
print("=" * 60)