from corretor import *
from grande_dicionario import dicionario
import time
import unidecode
import re
repeater = True
while repeater:
    palavras = [re.sub("[^a-zA-Z]+","",re.sub('[\"\']+',"",word)) for word in unidecode.unidecode(input("Insira a frase: ")).split()]
    temp_1=time.time()
    erradas,informais = identifica(palavras,dicionario)
    if len(erradas)+len(informais)==0:
        temp_2=time.time()
        demora=float(format(temp_2-temp_1, '.2f'))
        score = 1.0
        print ("")
        print ("Corretas: "+str(len(palavras)))
        print ("Completamente erradas: Nenhuma")
        print ("Com erro nivel um: Nenhuma")
        print ("Com erro nivel dois: Nenhuma")
        print ("Informais: Nenhuma")
        print ("")
        print ("Score: "+str(float(format(score, '.2f'))))
        print ("")
        print ("Demorou %s segundos" %(demora))
        print ("")
    else:
        sugestoes,niveis = corretor_frase(erradas,dicionario)
        print ("")
        peso(palavras,sugestoes,niveis,informais)
        temp_2=time.time()
        demora=float(format(temp_2-temp_1, '.2f'))
        print ("")
        print ("Demorou %s segundos" %(demora))
        print ("")
