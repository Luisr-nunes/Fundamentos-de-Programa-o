programa{
	//Calculo de Média
	
	funcao inicio(){
	
	real nota1, nota2, nota3, nota4, media

	escreva ("Informe sua nota AV1:")
	leia (nota1)
	escreva ("\nInforme sua nota AV2:")
	leia (nota2)
	escreva ("\nInforme sua nota AV3:")
	leia (nota3)
	escreva ("\nInforme sua nota AV4:")
	leia (nota4)

	media = (nota1 + nota2 + nota3 + nota4)/4
	
	escreva ("sua media é: ", media)

	se (media>=7){
		escreva("\nAprovado")
	} senao se (media >=3 e media<7){
		escreva ("\nRecuperação")
	
	} senao {
		escreva ("\nReprovado")
	}
	
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 485; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */