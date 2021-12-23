import sys
sys.path.insert(0, r'D:/Projetos/Alura/PythonAlura/Testes TDD/testes-python-projeto-inicial/')


from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido 

class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario('Gui',500.0)
        self.yuri = Usuario('Yuri',500.0)
        self.vini = Usuario('Vini',500.0)
        self.lance_do_vini = Lance(self.vini, 200.0)
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')
    
    def test_quando_adicionados_em_ordem_crescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance) #verifica se o valor recebido é igual ao esperado
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
       
    '''teste inutilizado pela nova regara de negocio'''
      
    # def test_quando_adicionados_em_ordem_decrescente_deve_retornar_o_maior_e_o_menor_valor_de_um_lance(self):

    #     self.leilao.propoe(self.lance_do_gui)
    #     self.leilao.propoe(self.lance_do_yuri)


    #     menor_valor_esperado = 100.0
    #     maior_valor_esperado = 150.0

    #     self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
    #     self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri',500.0)
            lance_do_yuri = Lance(yuri, 100.0)
    
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)
        
    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)


        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)
        
    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_vini)


        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
        
        
    #casos de uso relacionados a quantidade de lances e quem deu o lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)
    
        quantidade_de_lances_recebido = len(self.leilao.lances)
    
        self.assertEqual(1, quantidade_de_lances_recebido)
    
    
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui) 
    
        quantidade_de_lances_recebido = len(self.leilao.lances)
    
        self.assertEqual(2, quantidade_de_lances_recebido)
    
    
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)
    
    #forma de testar utilizando a biblioteca unittest, onde verifica se a função gerou um erro de execução ValueError, 
    #causado a partir da proposta de dois lances da mesma pessoa, ou seja verifica s eo trecho de código identado causou um erro no programa
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
   
    #forma de testar o Value error sem utilizar a biblioteca unittest
        # try:
        #     self.leilao.propoe(self.lance_do_gui)
        #     self.leilao.propoe(lance_do_gui200)
        #     self.fail(msg='Não lançou exceção')
        # except ValueError:
        #     quantidade_de_lances_recebido = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances_recebido)
       