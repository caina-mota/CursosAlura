# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:27:53 2020

@author: Cainã
"""

class ExtratorArgumentoURL:
    def __init__(self,url):
        if self.stringEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida")
    
    @staticmethod
    def stringEhValida(url):
        if url:
            return True
        else:
            return False

    def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        
        moedaOrigem = self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

        if moedaOrigem == "moedadestino":
            moedaOrigem = self.verificaMoedaOrigem(buscaMoedaOrigem)
            
            inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
            finalSubstringMoedaOrigem = self.url.find("&")
            
        inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        
        moedaDestino = self.url[inicioSubstringMoedaDestino:finalSubstringMoedaDestino]
        
    
        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
            return self.url.find(moedaOuValor) + len(moedaOuValor) 
    
    def retornaValor(self):
        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]
        return valor

    def verificaMoedaOrigem(self, buscaMoedaOrigem):
       self.url = self.url.replace("moedadestino", "real", 1)  # primeiro vou fazer sem o 1 e depois vou usa-lo
       inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
       finalSubstringMoedaOrigem = self.url.find("&")
       return self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

    def __str__(self):
        moedaOrigem,moedaDestino = self.extraiArgumentos()
        representacaoString2 = "Valor:" + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString  = "Valor: {}\n Moeda Origem: {} \n Moeda Destino: {} \n".format(self.extraiValor(),moedaOrigem,moedaDestino)
        return representacaoString
    
    def __len__(self):
      return len(self.url)
  
    def __eq__(self,outraInstancia):
      return self.url == outraInstancia.url

if __name__ == '__main__':
    url ="https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=150"
    cambio = ExtratorArgumentoURL(url)
    moedaOrigem,moedaDestino=cambio.retornaMoedas()
    valor = cambio.retornaValor()
    print(moedaOrigem,moedaDestino,valor)
    #Aqui ta tudo bem, teste agora o caso em que “moedaorigem=moedadestino”.
    url ="https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=150"
    cambio = ExtratorArgumentoURL(url)
    moedaOrigem,moedaDestino=cambio.retornaMoedas()
    valor = cambio.retornaValor()
    print(moedaOrigem,moedaDestino,valor)