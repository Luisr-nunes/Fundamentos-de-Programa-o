programa {
	funcao inicio() {

		real largura, altura, area, quantidadeExataDeLatas
		inteiro latas, parteInteira

		escreva("--- Consumo de tinta por parede ---\n")

		escreva("Informe a largura de sua parede: ")
		leia(largura)

		escreva("Informe a altura de sua parede: ")
		leia(altura)
	
		se (largura > 0 e altura > 0) {
			area = largura * altura
			quantidadeExataDeLatas = area / 10.0
			parteInteira = quantidadeExataDeLatas

			
			se (quantidadeExataDeLatas > parteInteira) {
				latas = parteInteira + 1
			} senao {
				latas = parteInteira
			}

			escreva("\n--- Resultado ---\n")
			escreva("Dimensões da parede:\n")
			escreva(" -> Altura: ", altura, " m\n")
			escreva(" -> Largura: ", largura, " m\n\n")
			escreva("Área total: ", area, " m²\n")
			escreva("Quantidade de latas necessárias: ", latas, "\n")
		} senao {
			escreva("\n--> Valores inválidos. A largura e altura devem ser maiores que zero.\n")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 394; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */