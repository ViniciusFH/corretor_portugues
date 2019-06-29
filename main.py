from corretor import *
from grande_dicionario import dicionario
import time
import unidecode
import re
repeater = True
while repeater:
    score = 1.0
    palavras = [word.lower() for word in unidecode.unidecode(re.sub('[\"\'\,\;\.\:\(\)]+',"",input("Insira a frase: "))).split()]
    temp_1=time.time()
    score = 0.0
    if len(palavras)>0 and len(palavras)<15:
        erradas,informais = identifica(palavras,dicionario)
        corretas = len(palavras)-(len(erradas)+len(informais))
        um, dois, impossiveis = corretor_frase(erradas,dicionario)
        score = peso(len(palavras),corretas,um,dois,impossiveis,len(informais))
        
    temp_2=time.time()
    demora = float(format(temp_2-temp_1, '.2f'))



    print ("")
    print ("Número de palavras: "+str(len(palavras)))
    print ("Corretas: "+str(corretas))
    print ("Completamente erradas: "+str(impossiveis))
    print ("Com erro nivel um: "+str(um))
    print ("Com erro nivel dois: "+str(dois))
    print ("Informais: "+str(len(informais)))
    print ("")
    print ("Score: "+str(float(format(score, '.2f'))))
    print ("")
    print (demora)
