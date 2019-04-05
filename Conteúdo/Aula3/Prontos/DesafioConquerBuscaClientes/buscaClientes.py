#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Você recebeu uma lista de clients e seus IDs no Sistema, Conforme este modelo:

# 100000 ? Diego Almeida
# 100001 ? Paula Macedo
# 100002 ? Adam Silva
# ?.

# Criar um programa que permita:
# 	- achar o nome associado com um ID
# 	- achar o ID associado com um nome

# importe as bibliotecas necessárias aqui
from listaDeClientes import buscaClientes
import readline
import pudb

class MyCompleter(object):
    """
    From: https://stackoverflow.com/questions/7821661/how-to-code-autocompletion-in-python
    Completa o texto que você está digitando
    """

    # Completa o que voce faz

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        # pudb.set_trace()
        if state == 0:  # busca os possiveis nomes no primeiro clique
            if text:
                # entradas que podem ser
                self.matches = [s for s in self.options
                                    if s and s.lower().startswith(text.lower())]
            else:
                # sem texto, todas as entradas sao possiveis
                self.matches = self.options[:]

        # retorna o que achou
        try:
            return self.matches[state]
        except IndexError:
            return None

if __name__ == "__main__":
    id_cliente = {}
    cliente_id = {}

    # busca a lista de 30 clientes, você pode buscar quantos clientes quiser
    lista_clientes = buscaClientes(30)
    for cliente in lista_clientes:
        # separa a lista em id e cliente
        id, nome_cliente = cliente.split('-')

        # cria um dicionário
        id_cliente[id.strip()] = cliente
        cliente_id[nome_cliente.strip()] = id

        print(cliente)


    # criará a interface para fazer a consulta
    todas_chaves = list(cliente_id.keys())+list(id_cliente.keys())
    completer = MyCompleter(todas_chaves)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    while True:
        entrada_usuario = input("Digite o ID ou o Nome da Pessoa: (tecle ctrl+d para parar)\n")

        # como so temos ids com numeros, se houver somente numeros e uma id, se nao um nome
        try:
            # converte para inteiro e busca no dicionario de ids
            id_digitado = int(entrada_usuario)
            res = id_cliente.get(str(id_digitado), "Desculpe, não encontrei este id")
        except:
            res = cliente_id.get(str(entrada_usuario), None)
            if not res:
                res = "Desculpe, não encontrei este nome"


        print("Resultado da pesquisa: {}".format(res))





    

