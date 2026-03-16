programa{
	funcao inicio(){
		
		inteiro totalDeAlunos, i, aulasFrequentadas
		inteiro contadorDeAprovados = 0
		real porcentagemDeAprovados = 0.0
		cadeia listaDeAprovados = ""
		cadeia nomeDoAluno

		escreva("--- Controle de Presença do Curso de Análise e Desenvolvimento de Sistemas 2025.2 - Noite ---\n\n")

		totalDeAlunos = 0
		enquanto (totalDeAlunos <= 0) {
			escreva("Informe o número total de alunos a serem registrados: ")
			leia(totalDeAlunos)
			se (totalDeAlunos <= 0) {
				escreva("--> O número de alunos deve ser pelo menos 1.\n")
			}
		}

		para (i = 1; i <= totalDeAlunos; i++) {
			escreva("\n--- Registro do Aluno(a) ", i, " de ", totalDeAlunos, " ---\n")
			
			escreva("Digite o nome do(a) aluno(a): ")
			leia(nomeDoAluno)
			
			aulasFrequentadas = -1
			enquanto (aulasFrequentadas < 0 ou aulasFrequentadas > 10) {
				escreva("Digite a quantidade de encontros frequentados (0 a 10): ")
				leia(aulasFrequentadas)
				se (aulasFrequentadas < 0 ou aulasFrequentadas > 10) {
					escreva("--> Valor inválido. A frequência deve ser entre 0 e 10.\n")
				}
			}

			se (aulasFrequentadas >= 6) {
				contadorDeAprovados = contadorDeAprovados + 1
				listaDeAprovados = listaDeAprovados + " - " + nomeDoAluno + "\n"
			}
		}
	
		se (totalDeAlunos > 0) {
			porcentagemDeAprovados = (contadorDeAprovados * 100.0) / totalDeAlunos
		}

		escreva("\n\n--- Relatório Final do Curso ---\n")
		escreva("Alunos com direito ao certificado:\n")
		
		se (contadorDeAprovados > 0) {
			escreva(listaDeAprovados)
		} senao {
			escreva("Nenhum aluno atingiu a frequência necessária.\n")
		}

		escreva("\nTotal de alunos: ", totalDeAlunos)
		escreva("\nTotal de aprovados: ", contadorDeAprovados)
		escreva("\nPorcentagem de alunos aprovados: ", porcentagemDeAprovados, "%\n")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1088; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */