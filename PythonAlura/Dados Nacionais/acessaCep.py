# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:49:16 2020

@author: Cainã
"""
import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_Valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.format_cep()

    def cep_eh_Valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])
    
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (dados['bairro'], dados['localidade'], dados['uf'])
    
if __name__ == '__main__':
    cep = "93054000"
    objeto_cep = BuscaEndereco(cep)
    print(objeto_cep)
    
    bairro, cidade, uf = objeto_cep.acessa_via_cep()
    print(bairro, cidade, uf)