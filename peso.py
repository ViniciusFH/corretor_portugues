from corretor import *
from dicionario_arvore import dicionario
import nltk
import time
import unidecode
repeater = True
while repeater:
    frase_bruta = input("Insira a frase: ")
    temp_1=time.time()
    palavras = nltk.word_tokenize(unidecode.unidecode(frase_bruta.lower()))
    erradas = identifica(palavras,dicionario)
    sugestoes,niveis = corretor_frase(erradas,dicionario)
    print ("")
    peso(palavras,sugestoes,niveis)
    temp_2=time.time()
    demora=float(format(temp_2-temp_1, '.2f'))
    print ("")
    print ("Demorou %s segundos" %(demora))
    print ("")
