#!/usr/bin/python
# -*- coding: 'latin-1' -*-
#
# Programa que ira contar quantas vezes cada palavra aparece em um texto
from texto import lerTexto

if __name__ == "__main__":
    """
    Função que será executada quando executarmos 'python contagemPalavras.py'
    """
    text = lerTexto()
    print(text)

    # divide a string em uma lista
    listaPalavras = text.split()

    # cria um dicionário e para cada palavra, adiciona a palavra ou soma mais 1
    resumo = {}
    for palavra in listaPalavras:
        resumo[palavra] = resumo.get(palavra, 0) + 1

    # imprime um sumário da quantidade de palavras
    emOrdem = sorted([ (k,v) for k,v in resumo.items() ], key=lambda x: -x[1])
    print("Quantidade total de palavras: {}".format(len(resumo.keys())))
    print(emOrdem[:15])
