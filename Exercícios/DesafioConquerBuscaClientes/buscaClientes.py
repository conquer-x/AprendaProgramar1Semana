#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Você recebeu uma lista de clients e seus IDs no Sistema, Conforme este modelo:

# 100000 – Diego Almeida
# 100001 – Paula Macedo
# 100002 – Adam Silva
# ….

# Criar um programa que permita:
# 	- achar o nome associado com um ID
# 	- achar o ID associado com um nome

# importe as bibliotecas necessárias aqui
from listaDeClientes import buscaClientes

if __name__ == "__main__":
    # busca a lista de 30 clientes, você pode buscar quantos clientes quiser
    lista_clientes = buscaClientes(30)
    for cliente in lista_clientes:
        print("{}".format(cliente))
    

