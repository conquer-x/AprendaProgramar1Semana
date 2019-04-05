programa {
    funcao logico e_bissexto(inteiro ano) {
        // retorna se e ou nao leap year (ano bissexto)
        // formula tirada do Wikipedia
        /// 
        se (ano%400==0) {
            retorne verdadeiro
        } 
        se (ano%100==0) {
            retorne falso
        }
        se (ano%4==0) {
            retorne verdadeiro
        } 
        retorne falso
    }
    
    funcao inteiro dias_no_mes(inteiro mes, inteiro ano) {
        // retorna o numero de dias que existem no mes
        //
        // verifica se é fevereiro, pois temos anos bissextos
        se (mes==2) {
            se (e_bissexto(ano)) {
                retorne 29
            } senao {
                retorne 28
            }
        } senao {
            se (mes==1 ou mes==3 ou mes==5 ou mes==7 ou mes==8 ou mes==10 ou mes==12) {
                retorne 31
            }
        }
        retorne 30
    }
    
    funcao proximo_dia(inteiro &ano, inteiro &mes, inteiro &dia) {
        // funcao para retornar o próximo dia
        //
        se (dia < dias_no_mes(mes, ano)) {
            // estamos progredindo no mes
            dia = dia +1
        } senao {
            se (mes < 12) {
                // chegamos ao ultimo dia do mes. adicione mais um ao mes e vole o dia ao 1
                dia = 1
                mes = mes +1
            } senao {
                // ultimo dia do ano. adicione ao ano e volte o mes e dia ao 1
                dia = 1
                mes = 1
                ano = ano + 1
            }
        }
    }
    
    funcao logico data_e_menor(inteiro ano1, inteiro mes1, inteiro dia1,
                               inteiro ano2, inteiro mes2, inteiro dia2) {
        // funcao para verificar se uma data é menor que a outra
        //
        
        // verifica se o ano é menor
        se (ano1<ano2) {
            retorne verdadeiro
        }
        // se o ano e igual
        se (ano1==ano2) {
            // verifica se o mes e menor
            se (mes1<mes2) {
                retorne verdadeiro
            }
            // se o mes for igual, verifica se o dia e menor
            se (mes1==mes2) {
                retorne dia1<dia2
            }
        }
        
        // se qualquer das situacoes acima falhar, retorna que e maior
        retorne falso
    }
    
    funcao inteiro dias_entre_datas(inteiro &ano1, inteiro &mes1, inteiro &dia1,
                                    inteiro &ano2, inteiro &mes2, inteiro &dia2) {
        // calcula a quantidade de dias entre duas datas
		inteiro dias
		dias = 0
		
		// conta os dias
		enquanto (data_e_menor(ano1,mes1,dia1, ano2,mes2,dia2))
		{
		    // acha a próxima data e soma mais um dia
		    proximo_dia(ano1, mes1, dia1)
		    dias = dias + 1
		}
		
		retorne dias
    }
    
    funcao teste(inteiro &ano1, inteiro &mes1, inteiro &dia1,
                 inteiro &ano2, inteiro &mes2, inteiro &dia2) {
        // faz um conjunto de testes para verificar se o programa está ok 
        //
        inteiro resposta, total_dias 
        total_dias = 0
        escreva("Testes Iniciados\n")
        
        // teste 1
        ano1 = 2011
        mes1 = 1
        dia1 = 1
        ano2 = 2011
        mes2 = 1
        dia2 = 30
        resposta = 29
		total_dias = dias_entre_datas(ano1, mes1, dia1, ano2, mes2, dia2)
        se (total_dias!=resposta){
            escreva("Teste 1 falhou\nValor esperado: "+resposta+"\tValor encontrado: " + total_dias + "\n")
        }
        
        // teste 2
        ano1 = 2011
        mes1 = 1
        dia1 = 1
        ano2 = 2012
        mes2 = 1
        dia2 = 1
        resposta = 365
		total_dias = dias_entre_datas(ano1, mes1, dia1, ano2, mes2, dia2)
        se (total_dias!=resposta){
            escreva("Teste 2 falhou\nValor esperado: "+resposta+"\tValor encontrado: " + total_dias+ "\n")
        }
        
        // teste 3
        ano1 = 2012
        mes1 = 2
        dia1 = 1
        ano2 = 2012
        mes2 = 3
        dia2 = 1
        resposta = 29
		total_dias = dias_entre_datas(ano1, mes1, dia1, ano2, mes2, dia2)
        se (total_dias!=resposta){
            escreva("Teste 3 falhou\nValor esperado: "+resposta+"\tValor encontrado: " + total_dias+ "\n")
        }
        escreva("Testes Finalizados")
    }
        
	funcao inicio() {
		// funcao para contar a idade dada a data de nascimento e a data de cálculo
		inteiro ano1, mes1, dia1
		inteiro ano2, mes2, dia2
		inteiro total_dias
		
		// esta variável controla se os testes acontecerao ou nao
		logico testar
		testar = falso
		
		se (testar==falso) {
		    // le as datas de inicio e fim 
		    escreva("Por favor digite o ano, mes e dia inicial (nesta ordem):")
		    leia(ano1, mes1, dia1)
		    escreva("Por favor digite o ano, mes e dia final (nesta ordem):")
		    leia(ano2, mes2, dia2)
		    total_dias = dias_entre_datas(ano1, mes1, dia1, ano2, mes2, dia2)
		    
		    // imprima o resultado
		    escreva("O total de dias é " + total_dias)
		} senao {
		    teste(ano1, mes1, dia1, ano2, mes2, dia2)
		}
		
	}
}
