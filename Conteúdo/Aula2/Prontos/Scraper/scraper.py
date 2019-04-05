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
import pandas as pd

dir_paginas = 'paginas'

logging.basicConfig()
logging.getLogger('root').setLevel(logging.INFO)

if __name__ == "__main__":
    # busca a página e os produtos
    texto_pagina = pc.buscarPagina('https://escolaconquer.com.br')
    links_produtos = pc.encontrarUrls(texto_pagina, 'https://escolaconquer.com.br/produto/')

    # usaremos este para não gerar sobrecarga nos servidores
    # links_produtos = [
    # 'https://escolaconquer.com.br/produto/grow-your-business/cwb/',
    # 'https://escolaconquer.com.br/produto/alta-performance-poa/',
    # 'https://escolaconquer.com.br/produto/alta-performance-rj/',
    # 'https://escolaconquer.com.br/produto/alta-performance-bh/',
    # 'https://escolaconquer.com.br/produto/alta-performance-sp/'
    # ]

    # para cada um dos produtos
    lista_produtos = []
    for lp in links_produtos:
        
        # imprime algo para saber que está funcionando
        print('###########')
        print("Processando página {}".format(lp))
        
        # pelo URL, identifica o nome do produto e o local
        url_dividido = lp.split('/')
        produto, cidade = url_dividido[4:6]
        produto = produto.split("-")  
        
        # busca a página
        texto_produto = pc.buscarPagina(lp)

        # verifica o tipo da página
        if len(url_dividido) == 7:
            # tipo de página novo
            produto = " ".join(produto).capitalize()
            
            # busca as informacoes
            local, data, freq, hora, preco = pc.infoPaginaNova(texto_produto)[0]
            curso = CursoConquer(produto, cidade, local, data, freq, preco)
            lista_produtos.append(curso)
            
        else:
            # tipo de página antigo        
            cidade = produto[-1]
            produto = produto[:-1]
            produto = " ".join(produto).capitalize()

            # busca as informações
            lista_cursos = pc.infoPaginaAntiga(texto_produto)
            for info_curso in lista_cursos:
                local, data, freq, hora, preco = info_curso
                curso = CursoConquer(produto, cidade, local, data, freq, preco)
                lista_produtos.append(curso)

    # imprime como uma tabela
    df = pd.DataFrame([ dict(prod) for prod in lista_produtos])
    print(df)