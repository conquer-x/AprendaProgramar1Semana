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
    Théo
    Júlia
    Pedro
    Heloísa
    Gabriel
    Luiza
    Enzo
    Maria Luiza
    Matheus
    Lorena
    Lucas
    Lívia
    Benjamin
    Giovanna
    Nicolas
    Maria Eduarda
    Guilherme
    Beatriz
    Rafael
    Maria Clara
    Joaquim
    Cecília
    Samuel
    Eloá
    Enzo Gabriel
    Lara
    João Miguel
    Maria Júlia
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
Aparício
Apolinário
Araújo
Arruda
Assis
Assunção
Ávila
Azambuja
Baptista
Barreto
Barros
Beira-Mar
Belchior
Belém
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
Conceição
Corte Real
Cortês
Coutinho
Crespo
Cunha
Curado
Custódio
Córdoba
Damásio
Dantas
Dias
Dinís
Domingues
Dorneles
dos Reis
Drumond
D’Ávila
Escobar
Espinosa
Esteves
Evangelista
Farias
Ferrari
Figueiredo
Figueiroa
Flores
Fogaça
Freitas
Frutuoso
Furtado
Félix
Galvão
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
Guimarães
Guterres
Góis
Hernandes
Hilário
Hipólito
Ibrahim
Ilha
Infante
Jaques
Jesus
Jordão
Lacerda
Lancastre
Leiria
Lessa
Machado
Maciel
Magalhães
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
Nóbrega
Ornélas
Oliveira
Ourique
Pacheco
Padilha
Paiva
Paraíso
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
    # cria a variável com o texto
    lista_nome_sobrenome = [
        "{} - {} {}".format(id+1000000, nome.strip(), sobrenome.strip())
        for id, (nome, sobrenome) in enumerate(zip(random.choices(nomes, k=numero_buscar), 
                                   random.choices(sobrenomes, k=numero_buscar)))
    ]

    return lista_nome_sobrenome