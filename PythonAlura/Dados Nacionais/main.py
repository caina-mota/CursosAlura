# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:13:22 2020

@author: Cainã
"""
from cpf_cnpj import CpfCnpj

cpf_um = CpfCnpj("15316264754",'cpf')
print(cpf_um)


exemplo_cnpj = "35379838000112"
documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)