programa{
	funcao inicio(){

		real valorInicial, taxaJurosAnual, valorAtual, taxaDecimal, jurosPorAno
		inteiro numeroDeAnos, ano
		caracter continuarSimulacao
		
		faca {
			limpa()
			escreva("--- Simulador de Juros Simples ---\n")
			
			faca {
				escreva("Informe o valor do aporte inicial: R$ ")
				leia(valorInicial)
				se (valorInicial <= 0) {
					escreva("--> O aporte inicial deve ser maior que zero.\n")
				}
			} enquanto (valorInicial <= 0)

			faca {
				escreva("Informe a taxa de juros anual (%): ")
				leia(taxaJurosAnual)
				se (taxaJurosAnual < 0) {
					escreva("--> A taxa de juros não pode ser negativa.\n")
				}
			} enquanto (taxaJurosAnual < 0)

			faca {
				escreva("Informe a quantidade de anos que o investimento ficará rendendo: ")
				leia(numeroDeAnos)
				se (numeroDeAnos <= 0) {
					escreva("--> O período deve ser de pelo menos 1 ano.\n")
				}
			} enquanto (numeroDeAnos <= 0)
			
			taxaDecimal = taxaJurosAnual / 100.0
			jurosPorAno = valorInicial * taxaDecimal
			valorAtual = valorInicial

			escreva("\n--- Visão Parcial do Investimento ---\n")
			escreva("Valor Inicial: R$ ", valorInicial, "\n")
			escreva("Taxa de Juros: ", taxaJurosAnual, "% ao ano\n")
			escreva("-------------------------------------\n")

			para (ano = 1; ano <= numeroDeAnos; ano++) {
				valorAtual = valorAtual + jurosPorAno
				escreva("Saldo após o ano ", ano, ": R$ ", valorAtual, "\n")
			}
			escreva("\n")

			escreva("Deseja realizar outra simulação? (S/N): ")
			leia(continuarSimulacao)

		} enquanto (continuarSimulacao == 'S' ou continuarSimulacao == 's')
		
		limpa()
		escreva("Obrigado por usar o simulador de investimentos!\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 234; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */