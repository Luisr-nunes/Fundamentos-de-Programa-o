programa{
	funcao inicio() {
		inteiro quantidade_filhos , contador=0 , contador_filho1=0 , contador_filho2=0

		enquanto (contador<=9){
			escreva ("Informe a quantidade de filhos: ")
			leia(quantidade_filhos)
			contador++

		se (quantidade_filhos<=2){
			contador_filho1++
		}
		senao {
			contador_filho2++
		}
	}
	escreva ("Mulheres que possuem até 2 filhos: ", contador_filho1)
	escreva ("\nMulheres que possuem mais de 2 filhos: ", contador_filho2)
}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 295; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */