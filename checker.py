import re
from dictionary import dicionario

def correctionLevel(word, dictionary):

# Retorna a quantidade de vezes que uma palavra precisa ser corrigida.
# Se seu tamanho é maior do que 15, não tetamos corrigí-la.

    if len(word) > 15:
        return 3

    mod = correct(word)

    for i in mod:
        if i in dictionary["formal"]:
            return 1

    for i in mod:
        for j in correct(i):
            if j in dictionary["formal"]:
                return 2


           
    return 3



def sentenceCorrection(wrong, dictionary):

# Retorna os níveis de erro de cada uma das palavras.

    level = []

    for w in wrong:
        level.append(correctionLevel(w,dictionary))

    return level.count(1),level.count(2),level.count(3)



def detectNonFormal(words, dictionary):

# Identifica palavras erradas e informais.


    wrong, informal = [], []

    for i in words:

        if i not in dictionary["formal"]:

            if i not in dictionary["informal"]:
                wrong.append(i)
            else:
                informal.append(i)

    return wrong, informal



def correct(word):

    # Faz modificações na palavra para tentar corrigi-la
    # devolve um set() com todas as words geradas.

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    divide = [(word[:i], word[i:])          for i in range(len(word) + 1)]

    delete = [E + D[1:]                     for E, D in divide if D]
    change = [E + D[1] + D[0] + D[2:]       for E, D in divide if len(D)>1]
    replace = [E + c + D[1:]                for E, D in divide if D for c in alphabet]
    insert = [E + c + D                     for E, D in divide for c in alphabet]

    return set(delete + change + replace + insert)