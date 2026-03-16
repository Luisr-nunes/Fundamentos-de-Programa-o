programa{
	funcao inicio(){
		
		inteiro numeroDeDias
		inteiro totalGarrafas = 0
		real mediaProducao = 0.0
		cadeia mensagemDesempenho

		escreva("--- Registro de Produção ---\n")

		faca {
			escreva("Informe a quantidade de dias de produção você deseja registrar: ")
			leia(numeroDeDias)
			se (numeroDeDias <= 0) {
				escreva("--> O número de dias deve ser pelo menos 1.\n")
			}
		} enquanto (numeroDeDias <= 0)

		para (inteiro dia = 1; dia <= numeroDeDias; dia++) {
			inteiro garrafasDoDia

			faca {
				escreva("Informe a produção do dia ", dia, ": ")
				leia(garrafasDoDia)
				se (garrafasDoDia < 0) {
					escreva("--> A produção não pode ser um número negativo.\n")
				}
			} enquanto (garrafasDoDia < 0)
		
			totalGarrafas = totalGarrafas + garrafasDoDia
		}

		se (numeroDeDias > 0) {
			mediaProducao = totalGarrafas / numeroDeDias
		}

		se (mediaProducao < 1000.0) {
			mensagemDesempenho = "Produção baixa"
		} senao se (mediaProducao <= 2000.0) {
			mensagemDesempenho = "Produção satisfatória"
		} senao {
			mensagemDesempenho = "Produção excelente"
		}

		escreva("\n--- Relatório de Produção ---\n")
		escreva("Período analisado: ", numeroDeDias, " dia(s)\n")
		escreva("Total de garrafas produzidas: ", totalGarrafas, "\n")
		escreva("Média de produção por dia: ", mediaProducao, " garrafas\n")
		escreva("Desempenho: ", mensagemDesempenho, "\n")

	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 780; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */