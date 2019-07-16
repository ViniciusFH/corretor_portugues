def nivel_correcao(palavra, dicionario):

# retorna uma lista com a soma do que é
# gerado em insere, exclui e substitui

    import re
    if not re.match("^[a-zA-Z]+$",palavra) and len(palavra)>20:
            return 3
    
    mod = modifica(palavra)
    for i in mod:
            if i in dicionario["formal"]:
                    return 1
    
    if len(palavra)>15:
            return 3
    for i in mod:
            for j in modifica(i):
                    if j in dicionario["formal"]:
                            return 2


           
    return 3



def corretor_frase(erradas, dicionario):

# retorna os níveis de cada erro numa dada frase

    niveis = []
    for erro in erradas:
            niveis.append(nivel_correcao(erro,dicionario))
    return niveis.count(1),niveis.count(2),niveis.count(3)



def identifica(palavras, dicionario):

# identifica palavras erradas e informais
    
    
    erradas, informais = [], []

    for i in palavras:
            if i not in dicionario["formal"]:
                    if i not in dicionario["informal"]:
                            erradas.append(i)
                    else:
                            informais.append(i)

    return erradas, informais



def modifica(palavra):

# faz modificações na palavra para tentar corrigi-la
# devolve um set() com todas as palavras geradas

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    divide = [(palavra[:i], palavra[i:])    for i in range(len(palavra) + 1)]
    
    deleta = [E + D[1:]                     for E, D in divide if D]
    troca = [E + D[1] + D[0] + D[2:]        for E, D in divide if len(D)>1]
    substitui = [E + c + D[1:]              for E, D in divide if D for c in alfabeto]
    insere = [E + c + D                     for E, D in divide for c in alfabeto]
    
    return set(deleta + troca + substitui + insere)