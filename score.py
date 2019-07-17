from corretor import *
from dicionario import dicionario
import unidecode
import re


def filtro(scores, operador, valor):

# permite filtrar as frases do bruce por score

    if operador == "igual" or operador == "=":
            return [f for f in scores if f["score"]==valor]
    elif operador == "maior" or operador == ">":
            return [f for f in scores if f["score"]>valor]
    elif operador == "menor" or operador == "<":
            return [f for f in scores if f["score"]<valor]



def score(frases):

    scores = []
    for f in frases:
        palavras = [word.lower() for word in unidecode.unidecode(re.sub('[\"\'\,\;\.\:\(\)]+',"",f)).split()]
        if len(palavras)>0 and len(palavras)<15:
            erradas,informais = identifica(palavras,dicionario)
            corretas = len(palavras)-(len(erradas)+len(informais))
            um, dois, impossiveis = corretor_frase(erradas,dicionario)
            score = peso(len(palavras),corretas,um,dois,impossiveis,len(informais))
            scores.append({"frase": f, "score": score})

    return scores



def peso(palavras, corretas, um, dois, impossiveis, informais):
        
    return float(format(1.0 - (0.5*informais+
                   0.7*um+
                   0.8*dois+
                   impossiveis
                  )/ palavras, ".2f"))
