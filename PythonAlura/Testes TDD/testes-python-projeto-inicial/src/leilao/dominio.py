import sys
sys.path.insert(0, r'D:/Projetos/Alura/PythonAlura/Testes TDD/testes-python-projeto-inicial/')

from src.leilao.excecoes import LanceInvalido 

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira
    
    def propoe_lance(self, leilao, valor):
        if not self._valor_valido(valor):
            raise LanceInvalido('Não pode propor um lance com o valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        
        self.__carteira -= valor
        
    def _valor_valido(self, valor):
        return valor <= self.__carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0
    
    def propoe(self, lance: Lance):
        #se a lista for vazia ou se o usuário anterior for diferente e o próximo lance for maior
        if self._lance_e_valido(lance): 
            if not self._tem_lances():
                self.menor_lance = lance.valor
                
            self.maior_lance = lance.valor
            
            self.__lances.append(lance)
    
    def _tem_lances(self):
        return self.__lances
    
    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario :
            return True
        raise LanceInvalido("Mesmo usuário não pode realizar dois lances seguidos.")
        
    def _lance_maior_que_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O lance não pode ser menor que o anterior.")
    
    def _lance_e_valido(self,lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance) and 
                                          self._lance_maior_que_anterior(lance))

    @property
    def lances(self):
        return self.__lances[:] #devolve uma cópia rasa da lista