programa{
	funcao inicio(){

		inteiro quantidadeDeAlunosInscritos, quantidadeDeKitsDeCoffeBreak
		real valorDasCamisetas, valorUnitarioDoKitDeCoffeBreak, valorDoAluguelDoLocal, valorDoPatrocinioRecebido
		real totalGasto, gastoTotalComPatrocinio, valorPorAluno

		escreva("--- Orçamento da Semana de Tecnologia CESAR School ---\n\n")

		escreva("Informe a quantidade de alunos inscritos: ")
		leia(quantidadeDeAlunosInscritos)

		escreva("Informe o valor total das camisetas: R$ ")
		leia(valorDasCamisetas)

		escreva("Informe a quantidade de kits de coffe break: ")
		leia(quantidadeDeKitsDeCoffeBreak)

		escreva("Informe o valor unitário de cada kit: R$ ")
		leia(valorUnitarioDoKitDeCoffeBreak)

		escreva("Informe o valor do aluguel do auditório: R$ ")
		leia(valorDoAluguelDoLocal)

		escreva("Informe o valor do patrocínio recebido: R$ ")
		leia(valorDoPatrocinioRecebido)

		totalGasto = valorDasCamisetas + (quantidadeDeKitsDeCoffeBreak * valorUnitarioDoKitDeCoffeBreak) + valorDoAluguelDoLocal

		se (totalGasto > valorDoPatrocinioRecebido){
			gastoTotalComPatrocinio = totalGasto - valorDoPatrocinioRecebido
		}
		senao{
			gastoTotalComPatrocinio = 0.0
		}
		
		se (quantidadeDeAlunosInscritos > 0) {
			valorPorAluno = gastoTotalComPatrocinio / quantidadeDeAlunosInscritos
		} senao {
			valorPorAluno = 0.0
		}


		escreva("\n--- Orçamento Total do Evento ---\n")
		escreva("Gastos Totais do Evento: R$ ", totalGasto, "\n")
		escreva("Gasto Final (após patrocínio): R$ ", gastoTotalComPatrocinio, "\n")
		escreva("Taxa por Aluno: R$ ", valorPorAluno, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1174; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */