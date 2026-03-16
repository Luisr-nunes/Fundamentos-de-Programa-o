programa{
	funcao inicio(){
		
		real horasDeAtividade, pontosGanhos

		escreva("--- Programa de Pontuação por Atividade Física - GymRats ---\n")

		faca {
			escreva("Informe o total de horas de atividade física no mês: ")
			leia(horasDeAtividade)

			se (horasDeAtividade < 0) {
				escreva("--> Valor inválido. Por favor, digite um número igual ou maior que zero.\n")
			}
		} enquanto (horasDeAtividade < 0)

		
		se (horasDeAtividade <= 10.0) {
			pontosGanhos = horasDeAtividade * 2
		}
		senao se (horasDeAtividade <= 20.0) {
			pontosGanhos = horasDeAtividade * 5
		}
		senao {
			pontosGanhos = horasDeAtividade * 10
		}

		escreva("\n--- Pontuação total ---\n")
		escreva("Horas de atividade informadas: ", horasDeAtividade, " horas\n")
		escreva("Total de pontos ganhos: ", pontosGanhos, " pontos\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 416; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */