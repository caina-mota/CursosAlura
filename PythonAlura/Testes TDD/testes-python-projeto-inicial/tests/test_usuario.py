# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:29:51 2020

@author: Cainã
"""
import sys
sys.path.insert(0, r'D:/Projetos/Alura/PythonAlura/Testes TDD/testes-python-projeto-inicial/')

from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido 
import  pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0
    

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini, leilao):
    
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0
    
def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini, leilao):
    #mesma ideia da utilização do self.assertRaises() do unittest, ou seja,
    #se o trecho de código abaixo gerar erro, o teste é aprovado
    with pytest.raises(LanceInvalido):
  
        vini.propoe_lance(leilao, 200.0)
