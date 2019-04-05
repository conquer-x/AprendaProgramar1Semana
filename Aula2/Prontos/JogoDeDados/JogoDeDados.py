#!/usr/bin/python
# -*- coding: 'latin-1' -*-
#
# Conquer X: Conversão do jogo de dados da aula de Portugol para o Python
#
# importamos as bibliotecas que iremos usar.
# Dica: Coloque todas as importações aqui
import random


def imprimirResultadoJogador(valor1, valor2, total, nome):
    """
    Funcao que recebe os resultados do jogo de um jogador e imprime os mesmos.
    params:
        valor1: valor do dado1
        valor2: valor do dado2
        total: total da soma dos dados
        nome: nome do jogador
    """
    print("Os dados do jogador {} foram:\t{}\t{}".format(nome, valor1, valor2))
    print("Total do jogo:\t{}".format(total))    

def jogarDadosImprimir(nome):
    """
    Joga os dados de um jogador e imprime o resultado
    params:
        nome: nome do jogador
    """
    # joga os dados
    valor1, valor2 = random.randint(1,6), random.randint(1,6)
    total = valor1 + valor2

    # imprime o resultado
    imprimirResultadoJogador(valor1, valor2, total, nome)

    return total

if __name__ == "__main__":
    """
    Função principal. Somente entrará aqui se for rodado como script
    """
    # entra no loop de jogo
    while True:
        # inicia as variáveis
        total1, total2 = 0, 0

        # pede para digitar o nome
        nome = input("Digite seu nome ou escreva sair. Aperte enter para começar!\n")

        # verifica se e para sair do jogo
        if (nome=="sair"):
            break

        # joga os dados e imprime o resultado
        total1 = jogarDadosImprimir(nome)

        # joga os dados da máquina
        total2 = jogarDadosImprimir("Maquina")

        if total1>=total2:
            print("Parabéns, você ganhou!!")
        else:
            print("Que pena, você perdeu!")
