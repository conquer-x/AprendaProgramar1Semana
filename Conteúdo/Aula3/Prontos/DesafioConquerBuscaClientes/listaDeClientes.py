#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# Arquivo para "esconder" os clientes 
import random

nomes = """Alice
    Miguel
    Sophia
    Arthur
    Helena
    Bernardo
    Valentina
    Heitor
    Laura
    Davi
    Isabella
    Lorenzo
    Manuela
    Th�o
    J�lia
    Pedro
    Helo�sa
    Gabriel
    Luiza
    Enzo
    Maria Luiza
    Matheus
    Lorena
    Lucas
    L�via
    Benjamin
    Giovanna
    Nicolas
    Maria Eduarda
    Guilherme
    Beatriz
    Rafael
    Maria Clara
    Joaquim
    Cec�lia
    Samuel
    Elo�
    Enzo Gabriel
    Lara
    Jo�o Miguel
    Maria J�lia
    Henrique
    Isadora
    Gustavo"""
nomes = nomes.split("\n")

sobrenomes = """Agostinho
Aguiar
Albuquerque
Alegria
Alencastro
Almada
Alves
Alvim
Amorim
Andrade
Antunes
Apar�cio
Apolin�rio
Ara�jo
Arruda
Assis
Assun��o
�vila
Azambuja
Baptista
Barreto
Barros
Beira-Mar
Belchior
Bel�m
Bernardes
Bittencourt
Boaventura
Bonfim
Botelho
Brites
Brito
Caetano
Calixto
Camacho
Camilo
Capelo
Castro
Cavalcante
Chaves
Concei��o
Corte Real
Cort�s
Coutinho
Crespo
Cunha
Curado
Cust�dio
C�rdoba
Dam�sio
Dantas
Dias
Din�s
Domingues
Dorneles
dos Reis
Drumond
D?�vila
Escobar
Espinosa
Esteves
Evangelista
Farias
Ferrari
Figueiredo
Figueiroa
Flores
Foga�a
Freitas
Frutuoso
Furtado
F�lix
Galv�o
Garcia
Gaspar
Gentil
Geraldes
Gil
Godinho
Gomes
Gonzaga
Goulart
Gouveia
Guedes
Guimar�es
Guterres
G�is
Hernandes
Hil�rio
Hip�lito
Ibrahim
Ilha
Infante
Jaques
Jesus
Jord�o
Lacerda
Lancastre
Leiria
Lessa
Machado
Maciel
Magalh�es
Maia
Maldonado
Marinho
Marques
Martins
Medeiros
Meireles
Mello
Mendes
Menezes
Mesquita
Modesto
Monteiro
Morais
Moreira
Morgado
Moura
Muniz
Neves
Nogueira
Novais
N�brega
Orn�las
Oliveira
Ourique
Pacheco
Padilha
Paiva
Para�so
Paris
Peixoto
Peralta
Peres
Pilar
Pimenta
Pinheiro
Portela
Quaresma
Quarteira
Queiroz
Ramires
Ramos
Rebelo
Resende
Ribeiro
Salazar
Sales
Salgado
Salgueiro
Sampaio
Sanches
Santana
Siqueira
Soares
Subtil
Tavares
Taveira
Teixeira
Teles
Torres
Trindade
Varela
Vargas
Vasconcelos
Vasques
Veiga
Veloso
Vidal
Vieira
Vilela
Xavier
Ximenes
Xisco
Zagalo
Zanette
Zaganelli"""
sobrenomes =  sobrenomes.split("\n")


def buscaClientes(numero_buscar=20):
    """
    Retorna o texto a ser processado. Mais tarde, este arquivo pode receber
    leitura diretamtne de um arquivo
    """
    # cria a vari�vel com o texto
    lista_nome_sobrenome = [
        u"{} - {} {}".format(id+1000000, nome.strip(), sobrenome.strip())
        for id, (nome, sobrenome) in enumerate(zip(random.choices(nomes, k=numero_buscar), 
                                   random.choices(sobrenomes, k=numero_buscar)))
    ]

    return lista_nome_sobrenome