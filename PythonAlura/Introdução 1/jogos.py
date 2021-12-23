# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:08:28 2020

@author: Cainã
"""

# jogos.py

import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    
    print("(1) Forca (2) Adivinhação")
    
    jogo = int(input("Qual jogo? "))
    
    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
        
if __name__=="__main__":
    escolhe_jogo()
    