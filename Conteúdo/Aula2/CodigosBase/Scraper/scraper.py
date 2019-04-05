#!/usr/bin/python
# -*- coding: 'latin-1' -*-
#
# ConquerX: Introducao a programacao - Python
# Programa que fará um scraping da página da Conquer, buscando os Produtos
#
import logging

# classes criadas por nós
from utils import paginasConquer as pc
from cursoConquer import CursoConquer

dir_paginas = 'paginas'

logging.basicConfig()
logging.getLogger('root').setLevel(logging.INFO)

if __name__ == "__main__":
    # exemplo de uso das funções
    # busca página
    html = pc.buscarPagina('https://escolaconquer.com.br')
    print("\nResultado da funcao buscarPagina: {}".format(html[1:100]))

    # busca link que contenha a string passada no parâmetro no link
    links = pc.encontrarUrls(html, 'https://escolaconquer.com.br')
    print("\nResultado função encontrarUrls: {}".format(links[1:5]))

    # busca dados das páginas
    html = pc.buscarPagina("https://escolaconquer.com.br/produto/coragem-cwb/")
    dados = pc.infoPaginaAntiga(html)
    print("\nResultado função encontrarUrls: {}".format(list(dados)))

    