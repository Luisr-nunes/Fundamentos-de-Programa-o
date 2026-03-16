programa{	
	funcao inicio(){
//Pode Dirigir? Idade=>18 e habilitação="sim"

inteiro idade, habilitacao
cadeia resposta
	
		escreva ("Informe sua idade: ")
		leia (idade)
		escreva ("Você é habilitado? (sim/não) ")
		leia (resposta)

		se (idade >=18 e resposta == "sim"){
			escreva ("Você pode dirigir!")
		} senao {
			escreva ("você não pode dirigir")

		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 374; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */