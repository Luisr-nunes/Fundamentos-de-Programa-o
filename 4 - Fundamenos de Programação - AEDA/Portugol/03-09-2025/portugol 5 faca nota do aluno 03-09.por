programa
{
	
	funcao inicio()
	{
		real nota1, acumulador=0 
		caracter opcao
		inteiro contador=0

		faca {
		escreva ("Informe a nota do aluno: ")
		leia (nota1)
		acumulador = acumulador + nota1
		escreva ("Deseja continuar informando as notas dos alunos? (S/N)")
		leia (opcao)
		contador=contador+1
		} enquanto (opcao !='N')

		escreva("A quantidade de Notas inseridas foi: ", contador)
		escreva("A média foi: ", acumulador/contador)

		
		
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 32; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */