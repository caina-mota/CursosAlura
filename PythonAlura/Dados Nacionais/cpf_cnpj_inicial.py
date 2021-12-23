# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:13:22 2020

@author: Cainã
"""
from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.format_cpf()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()

    def cnpj_eh_Valido(self, cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
            
if __name__ == '__main__':

    cpf_um = CpfCnpj("15316264754",'cpf')
    print(cpf_um)
    
    
    exemplo_cnpj = "35379838000112"
    documento = CpfCnpj(exemplo_cnpj, 'cnpj')
    print(documento)