# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:14:52 2020

@author: Cainã
"""

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
         return self.__likes

    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
          

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
    
    @property
    def likes(self):
         return self.__likes

    def dar_like(self):
        self.__likes += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


if __name__ == '__main__':
    
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
    f'- Duração: {vingadores.duracao}')
    
    atlanta = Serie('atlanta', 2018, 2)
    
    print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
    f'- Temporadas: {atlanta.temporadas}')