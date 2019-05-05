from corretor import *
from formal_arvore import formal
from informal_arvore import informal
import time
import unidecode
import re
repeater = True
while repeater:
    palavras = [re.sub("[^a-zA-Z]+","",re.sub('[\"\']+',"",word)) for word in unidecode.unidecode(input("Insira a frase: ")).split()]
    temp_1=time.time()
    erradas,informais = identifica(palavras,formal,informal)
    sugestoes,niveis = corretor_frase(erradas,formal)
    print ("")
    peso(palavras,sugestoes,niveis,informais)
    temp_2=time.time()
    demora=float(format(temp_2-temp_1, '.2f'))
    print ("")
    print ("Demorou %s segundos" %(demora))
    print ("")
