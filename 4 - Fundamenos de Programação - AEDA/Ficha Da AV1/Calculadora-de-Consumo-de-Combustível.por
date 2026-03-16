programa{
	funcao inicio(){
		
		real distanciaPercorrida, combustivelGasto, consumoMedio
		cadeia classificacao

		escreva("--- Calculadora de Consumo Médio de Combustível ---\n")
		
		faca {
			escreva("Informe a distância total percorrida (em Km): ")
			leia(distanciaPercorrida)
			se (distanciaPercorrida <= 0) {
				escreva("--> Valor inválido. A distância deve ser maior que zero.\n")
			}
		} enquanto (distanciaPercorrida <= 0)

		faca {
			escreva("Informe a quantidade de combustível gasto (em Litros): ")
			leia(combustivelGasto)
			se (combustivelGasto <= 0) {
				escreva("--> Valor inválido. O combustível deve ser maior que zero para evitar divisão por zero.\n")
			}
		} enquanto (combustivelGasto <= 0)
		
		consumoMedio = distanciaPercorrida / combustivelGasto

		se (consumoMedio < 4.0) {
			classificacao = "Muito ruim"
		}
		senao se (consumoMedio <= 8.0) {
			classificacao = "Ruim"
		}
		senao se (consumoMedio <= 12.0) {
			classificacao = "Regular"
		}
		senao se (consumoMedio <= 14.0) {
			classificacao = "Bom"
		}
		senao {
			classificacao = "Excelente"
		}
		
		escreva("\n--- Resultado ---\n")
		escreva("Distância Percorrida: ", distanciaPercorrida, " Km\n")
		escreva("Combustível Gasto: ", combustivelGasto, " L\n\n")
		escreva("Consumo Médio: ", consumoMedio, " Km/l\n")
		escreva("Classificação de Desempenho: ", classificacao, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1377; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */