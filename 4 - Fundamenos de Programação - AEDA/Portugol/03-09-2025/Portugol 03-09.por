programa{
	funcao inicio(){
	inteiro num1, num2, resultado
	inteiro opcao 

	escreva("Infome dois números: ")
	leia (num1,num2)

	escreva("1 - Soma")
	escreva("\n2 - Subtração")
	escreva("\n3 -Multiplicação")
	leia(opcao) 

	escolha (opcao){
	caso 1:
		resultado = num1 + num2
		pare
	caso 2:
		resultado = num1 - num2 
		pare
	caso 3:
		resultado = num1*num2
		pare
	caso contrario: 
		escreva ("Opção inválida")
		
		}
	escreva ("\nResultado: ",resultado)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 454; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */