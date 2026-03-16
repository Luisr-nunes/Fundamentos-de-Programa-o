programa{
	funcao inicio(){
		
		inteiro contadorHomens = 0
		inteiro contadorMulheres = 0
		inteiro idadeMulherMaisVelha = 0
		inteiro somaIdades = 0
		inteiro contadorMulheresMaisDe20 = 0
		real mediaIdades = 0.0
		inteiro idade
		caracter sexo
		
		escreva("Cadastro")

		para (inteiro i = 1; i <= 5; i++) {
			escreva("\n")
			escreva("Dados da ", i, "a Pessoa")
			escreva("\n")

			faca {
				escreva("Informe a idade: ")
				leia(idade)
				se (idade < 0 ou idade > 120) {
					escreva("Idade inválida. Tente novamente.")
					escreva("\n")
				}
			} enquanto (idade < 0 ou idade > 120)

			faca {
				escreva("Informe o sexo (M/F): ")
				leia(sexo)
				
				se ( nao (sexo == 'M' ou sexo == 'm' ou sexo == 'F' ou sexo == 'f') ) {
					escreva("Sexo inválido. Digite M ou F.\n")
				}
			} enquanto ( nao (sexo == 'M' ou sexo == 'm' ou sexo == 'F' ou sexo == 'f') )

			somaIdades = somaIdades + idade
			
			se (sexo == 'M' ou sexo == 'm') {
				contadorHomens = contadorHomens + 1
			} senao {
				contadorMulheres = contadorMulheres + 1

				se (idade > idadeMulherMaisVelha) {
					idadeMulherMaisVelha = idade
				}
				se (idade > 20) {
					contadorMulheresMaisDe20 = contadorMulheresMaisDe20 + 1
				}
			}
		}

		se(somaIdades > 0){
			mediaIdades = somaIdades / 5.0
		}
		
		escreva("\n")		
		escreva("--- Resultado do Cadastro ---\n")
		escreva("Homens cadastrados: ", contadorHomens, "\n")
		
		se (contadorMulheres > 0) {
			escreva("Mulher mais velha: ", idadeMulherMaisVelha, " anos\n")
		} senao {
			escreva("Nenhuma mulher foi cadastrada.\n")
		}
		
		escreva("Idade média do grupo: ", mediaIdades, " anos\n")
		escreva("Mulheres com mais de 20 anos: ", contadorMulheresMaisDe20, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 384; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */