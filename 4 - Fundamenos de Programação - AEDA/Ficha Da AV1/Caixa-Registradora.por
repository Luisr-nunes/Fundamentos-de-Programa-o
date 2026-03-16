	programa{
	funcao inicio(){

		real precoUnitario, totalDaCompra = 0.0
		caracter continuarCompra
		cadeia nomeDoProduto
		inteiro quantidade
		
		faca {
			escreva("--- Caixa Registradora ---\n")
			
			escreva("Informe o nome do produto: ")
			leia(nomeDoProduto)

			escreva("Informe o preço unitário: R$ ")
			leia(precoUnitario)

			escreva("Informe a quantidade: ")
			leia(quantidade)

			se (precoUnitario > 0.0 e quantidade >= 1) {
				real valorDoItem = precoUnitario * quantidade
				
				totalDaCompra = totalDaCompra + valorDoItem

				escreva("Item registrado com sucesso! (Subtotal do item: R$ ", valorDoItem, ")\n")
			}
			senao {
				escreva("ERRO: Preço ou quantidade informada não é válido. O item não pode ser registrado.\n")
			}

			escreva("\nDeseja registrar outro item? (S/N): ")
			leia(continuarCompra)
			limpa()
		} enquanto (continuarCompra == 'S' ou continuarCompra == 's')

		escreva("--- Registro Finalizado ---\n")
		escreva("Valor total a pagar: R$ ", totalDaCompra, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1014; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */