programa{
	funcao inicio(){
		
		real precoBase = 30.0

		inteiro quantidadeDeInteiraAoDia = 0
		inteiro quantidadeDeMeiaAoDia = 0
		inteiro quantidadeDePromocionalAoDia = 0
		inteiro quantidadeDeGratuitosAoDia = 0
		inteiro totalIngressosAoDia = 0
		real totalArrecadadoAoDia = 0.0
		
		caracter proximoCliente = 'S'
		
		enquanto (proximoCliente == 'S' ou proximoCliente == 's') {
			
			inteiro quantidadeDeIngressosCliente, tipoDeIngresso, idadeDoCliente, metodoDePagamento
			real valorRecebido, precoDoIngresso, totalDoCliente
			cadeia tipoIngressoNome

			limpa()
			escreva("--- Bilheteria do Cinema São Luiz ---\n\n")
			
			quantidadeDeIngressosCliente = 0
			enquanto (quantidadeDeIngressosCliente < 1) {
				escreva("Digite a quantidade de ingressos (mínimo 1): ")
				leia(quantidadeDeIngressosCliente)
				se (quantidadeDeIngressosCliente < 1) {
					escreva("--> Quantidade inválida. Tente novamente.\n")
				}
			}

			idadeDoCliente = -1
			enquanto (idadeDoCliente < 0 ou idadeDoCliente > 120) {
				escreva("Informe a idade do cliente: ")
				leia(idadeDoCliente)
				se (idadeDoCliente < 0 ou idadeDoCliente > 120) {
					escreva("--> Idade inválida. Digite entre 0 e 120.\n")
				}
			}
			
			precoDoIngresso = 0.0
			se (idadeDoCliente < 5) {
				precoDoIngresso = 0.0
				tipoIngressoNome = "Gratuidade (menor de 5 anos)"
				quantidadeDeGratuitosAoDia = quantidadeDeGratuitosAoDia + quantidadeDeIngressosCliente
				escreva("\n-> Gratuidade aplicada!\n")
			}
			senao {
				tipoDeIngresso = 0
				enquanto (tipoDeIngresso < 1 ou tipoDeIngresso > 3) {
					escreva("\nEscolha o tipo de ingresso:\n")
					escreva(" [1] Inteira (R$ ", precoBase, ")\n")
					escreva(" [2] Meia (R$ ", precoBase * 0.5, ")\n")
					escreva(" [3] Promocional (R$ ", precoBase * 0.7, ")\n")
					escreva("Sua opção: ")
					leia(tipoDeIngresso)

					se (tipoDeIngresso < 1 ou tipoDeIngresso > 3) {
						escreva("--> Tipo inválido. Digite 1, 2 ou 3.\n")
					}
				}
				
				se (tipoDeIngresso == 1) {
					precoDoIngresso = precoBase
					tipoIngressoNome = "Inteira"
					quantidadeDeInteiraAoDia = quantidadeDeInteiraAoDia + quantidadeDeIngressosCliente
				}
				senao se (tipoDeIngresso == 2) {
					precoDoIngresso = precoBase * 0.5
					tipoIngressoNome = "Meia"
					quantidadeDeMeiaAoDia = quantidadeDeMeiaAoDia + quantidadeDeIngressosCliente
				}
				senao {
					precoDoIngresso = precoBase * 0.7
					tipoIngressoNome = "Promocional"
					quantidadeDePromocionalAoDia = quantidadeDePromocionalAoDia + quantidadeDeIngressosCliente
				}
			}

			totalDoCliente = quantidadeDeIngressosCliente * precoDoIngresso
			
			escreva("\nTotal do pedido\n")
			escreva("Quantidade de ingressos: ", quantidadeDeIngressosCliente, "\n")
			escreva("Tipo aplicado: ", tipoIngressoNome, "\n")
			escreva("Total a pagar: R$ ", totalDoCliente, "\n")

			se (totalDoCliente > 0.0) {
				metodoDePagamento = 0
				enquanto (metodoDePagamento < 1 ou metodoDePagamento > 2) {
					escreva("\nSelecione o método de pagamento:\n")
					escreva(" [1] Dinheiro\n")
					escreva(" [2] Cartão\n")
					escreva("Sua opção: ")
					leia(metodoDePagamento)
				}

				se (metodoDePagamento == 1) {
					valorRecebido = 0.0
					enquanto (valorRecebido < totalDoCliente) {
						escreva("Digite o valor recebido: R$ ")
						leia(valorRecebido)
						se (valorRecebido < totalDoCliente) {
							escreva("--> Valor insuficiente, tente novamente.\n")
						}
					}
					escreva("Troco: R$ ", valorRecebido - totalDoCliente, "\n")
				}
				senao {
					escreva("--> Transação aprovada no cartão.\n")
				}
				
				totalArrecadadoAoDia = totalArrecadadoAoDia + totalDoCliente
			}

			totalIngressosAoDia = totalIngressosAoDia + quantidadeDeIngressosCliente

			escreva("\n")
			escreva("Atender próximo cliente? (S/N): ")
			leia(proximoCliente)
		}

		limpa()
		escreva("\n--- Encerramento da Bilheteria ---\n")
		escreva("Total de ingressos vendidos: ", totalIngressosAoDia, "\n\n")
		escreva("Detalhes:\n")
		escreva(" - Inteira:......... ", quantidadeDeInteiraAoDia, "\n")
		escreva(" - Meia:............ ", quantidadeDeMeiaAoDia, "\n")
		escreva(" - Promocional:..... ", quantidadeDePromocionalAoDia, "\n")
		escreva(" - Gratuitos:....... ", quantidadeDeGratuitosAoDia, "\n\n")
		escreva("Total arrecadado: R$ ", totalArrecadadoAoDia, "\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 4338; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */