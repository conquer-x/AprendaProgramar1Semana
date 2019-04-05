# -*- coding: 'latin-1' -*-
#
# ConquerX: Introducao a programacao - Python
# Script com utilitários para tratar as páginas da Conquer
#
import requests
import os, sys
import logging
import time
import traceback
from bs4 import BeautifulSoup 

# definição do dicionário
dir_paginas = 'paginas'

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

def buscarPagina(url):
    """
    Faz o download de 1 página passada como parâmetro
    
    Args:
        url: url a ser buscada
    
    Returns:
        texto da página
        
    Examples:
        buscarPagina('https://escolaconquer.com.br/xxxxx/')
    """
    # primeiro verifica se existe a pagina
    try:
        # gera o nome completo do arquivo com o caminho da máquina
        nome = url.replace('/', '#').replace('.', '#').replace(':', '#')
        diretorio_arquivo = os.path.dirname(os.path.abspath(__file__))
        diretorio_arquivo = os.path.split(diretorio_arquivo)[0]
        arquivo = os.path.join(diretorio_arquivo, dir_paginas, nome + '.htm')
        
        # abre o arquivo e lê as informações
        if os.path.exists(arquivo):
            logging.debug("Lendo do arquivo {}".format(arquivo))
            with open(arquivo, 'r') as f:
                data = f.read()

            # espera 1 segundo para dar emocao, parecendo que esta lendo da web.
            time.sleep(1)
            return data
        else:
            logging.debug("Buscando página de {}".format(url))
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
            html_resp = requests.get(url, headers=headers)

            logging.debug("Salvando arquivo {}".format(arquivo))
            with open(arquivo, 'w') as f:
                f.write(html_resp.text)

            dormir = 5
            logging.debug("Dormindo por {}s".format(dormir))
            time.sleep(dormir)
            return html_resp.text
    except:
        print("Erro ao ler a página")
        traceback.print_tb(sys.exc_info()[2])
        sys.exit(-1)

def encontrarUrls(texto, url):
    """
    Encontra uma URL no texto.
    Args:
        texto: texto da página
        url: url a ser buscada
    Returns:
        lista de urls encontradas na página que contenham a url passada
        
    Examples:
        encontrarUrls(html_resp.text, 'https://escolaconquer.com.br/xxxxx/')
    """
    # cria um objeto beautifulsoup para poder procurar como html
    soup = BeautifulSoup(texto, 'html.parser')
    
    # procura todos os links que possuem o url mencionado
    links = soup.find_all('a', href=lambda href: href and url in href)
    
    # retorna uma lista com todos os links
    ret = [link.attrs['href'] for link in links]
    return ret

def _infoCards(soup):
    """
    Dado uma estrutura já montado do Soup, busca as iformações contidas nos cards
    Args:
        soup: uma estrutura do soup que será buscada pelas classes do card
    Returns:
        lista dos os valores encontrados no card
            [(data, freq, hora, preco)]
    
    """
    cards = soup.find_all('div', {"class": "card-product-offers"})
    for card in cards:
        # turma = card.select('.card-product-offers-title')[0].text 
        titulos = card.select('.card-product-offers-item-title')
        data = titulos[0].text.strip()
        freq = titulos[1].text.strip()
        hora = titulos[2].text.strip()

        yield [data, freq, hora]
    
def infoPaginaAntiga(html):
    """
    Busca os dados da página antiga.
    Args: 
        html: html em uma string
    Returns:
    lista com as seguintes informaçoes
        [(data, freq, hora, preco)]

    Examples:
        infoPaginaAntiga(html_text)
    """
    # transforma a página em soup para melhorar a busca
    soup = BeautifulSoup(html, 'html.parser')

    # coleta a informação de preço
    preco = soup.select('.price-installment')[0].text
    
    # verifica é uma página com mais de um local (ex:SP)
    locais = soup.select('[id*="childrenContent"]')
    
    # para cada um dos cards de disponibilidade, pega as informações
    if len(locais)==0:
        # para cada um dos cards
        for info in _infoCards(soup):
            local = ""
            data, freq, hora = info
            yield (local, data, freq, hora, preco)
    else:
        # existe mais de um local. Acha o card deles individualmente
        for local in locais:
            # pega o titulo do local
            nome_local = local.h4.strong.text
            
            # pega as outras informações
            for info in _infoCards(local):
                data, freq, hora = info
                yield (nome_local, data, freq, hora, preco)

def infoPaginaNova(html):
    """
    Busca os dados da página antiga.
    Args: 
        html: html em uma string
    Returns:
        lista com os cursos da conquer

    Examples:
        infoPaginaAntiga(html_text)
    """
    # transforma a página em soup para melhorar a busca
    soup = BeautifulSoup(html, 'html.parser')

    # coleta a informação de preco
    preco = soup.select('.investimento-preco')[0].text

    # coleta as informacoes dos horarios
    turmas = soup.select('#turmas-mob')[0]
    for info in turmas.select('div.wpb_content_element'):
        # este código é bem específico para esta página, já que não há ids
        if(info.h3):
            local = info.h3.text.split("::")[0]
        else:
            p_list = info.div.select('p')
            if len(p_list) in [5,6]:
                # tira as informações da tabela
                data = p_list[0].text.replace("\n", " ")
                freq = p_list[1].text.replace("\n", " ")
                hora = p_list[3].text.replace("\n", " ")
            
            # a página da conquerX tem uma divisão diferente, com horários junto à frequencia
            if(len(p_list)==5):
                hora = None

    return [(local, data, freq, hora, preco)]
