from corretor import *
from grande_dicionario import dicionario
import time
import unidecode
import re
repeater = True
informal = 0.2
nivel_um = 0.3
nivel_dois = 0.4
impossivel = 0.5
while repeater:
    score = 1.0
    palavras = [re.sub("[^a-zA-Z]+","",re.sub('[\"\']+',"",word)) for word in unidecode.unidecode(input("Insira a frase: ")).split()]
    temp_1=time.time()
    if len(palavras)>15:
        score = 0,0
        temp_2=time.time()
        demora=float(format(temp_2-temp_1, '.2f'))
        print ("")
        print ("Frase muito grande")
        print ("")
        print ("Score: "+str(float(format(score, '.2f'))))
        print ("")
        print ("Demorou %s segundos" %(demora))
        print ("")
        continue
    erradas,informais = identifica(palavras,dicionario)
    if len(erradas)+len(informais)==0:
        temp_2=time.time()
        demora=float(format(temp_2-temp_1, '.2f'))
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
        continue
    sugestoes,niveis = corretor_frase(erradas,dicionario)
    impossiveis = len([impossivel for impossivel in sugestoes if len(sugestoes[impossivel])==0])
    if impossiveis==len(palavras):
        score = 0.0
        temp_2=time.time()
        demora=float(format(temp_2-temp_1, '.2f'))
        print ("")
        print ("Corretas: "+str(len(palavras)))
        print ("Completamente erradas: "+str(impossiveis))
        print ("Com erro nivel um: Nenhuma")
        print ("Com erro nivel dois: Nenhuma")
        print ("Informais: Nenhuma")
        print ("")
        print ("Score: "+str(float(format(score, '.2f'))))
        print ("")
        print ("Demorou %s segundos" %(demora))
        print ("")
        continue
    possiveis = len([possivel for possivel in sugestoes if len(sugestoes[possivel])>0])
    informais = len(informais)
    um = len([nivel for nivel in niveis if nivel==1])
    dois = len([nivel for nivel in niveis if nivel==2])
    score -= (
        impossiveis*(impossivel/len(palavras))+
        um*(nivel_um/len(palavras))+
        dois*(nivel_dois/len(palavras))+
        informais*(informal/len(palavras))
        )
    temp_2=time.time()
    demora=float(format(temp_2-temp_1, '.2f'))
    print ("Corretas: "+str((len(palavras)-len(sugestoes))-informais))
    print ("Completamente erradas: "+str(impossiveis))
    print ("Com erro nivel um: "+str(um))
    print ("Com erro nivel dois: "+str(dois))
    print ("Informais: "+str(informais))
    print ("")
    print ("Score: "+str(float(format(score, '.2f'))))
