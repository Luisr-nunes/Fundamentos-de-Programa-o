programa
{
	//Estrutras de decisão
	//Simples -> Se () {} Tenho Apenas Uma Saida
	//Composta -> Se (){} senao (){} Tenho Duas saidas
	//Aninhada -> Se (){} senao se (){} senao se (){}.... tem várias saidas
	//Multipla Escolha -> Escolha caso 
	funcao inicio()
	{
	inteiro idade
	
		escreva ("Informe sua idade: ")
		leia (idade)

		se (idade >=18){
			escreva ("Maior de idade!")
		} senao {
			escreva ("Menor de idade!")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 353; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */