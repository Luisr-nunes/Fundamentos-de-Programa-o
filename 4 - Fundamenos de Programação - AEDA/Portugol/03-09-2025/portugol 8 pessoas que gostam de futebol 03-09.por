programa{
		funcao inicio(){
			inteiro contador = 0
			cadeia opcao
			
			faca{
				escreva("Você gosta de futebol? (s/n) ")
				leia(opcao)
				
				se (opcao == "s"){
					contador++
				}
			} enquanto (opcao == "s")

			escreva ("\n Essa é a quantidade de pessoas que gostam de futebol: ", contador)
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 312; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */