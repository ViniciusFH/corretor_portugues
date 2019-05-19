def modifica(palavra):

        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        divide = [(palavra[:i], palavra[i:])    for i in range(len(palavra) + 1)]
        deleta = [E + D[1:]               for E, D in divide if D]
        troca = [E + D[1] + D[0] + D[2:] for E, D in divide if len(D)>1]
        substitui = [E + c + D[1:]           for E, D in divide if D for c in alfabeto]
        insere = [E + c + D               for E, D in divide for c in alfabeto]
        return set(deleta + troca + substitui + insere)


# numa dada frase, identifica quais palavras nao
# pertencem ao dicionario, e devolve uma lista com elas


def identifica(palavras, dicionario):
    
    
    erradas = []
    informais = []

    for i in palavras:
            if i not in dicionario["formal"]:
                    if i not in dicionario["informal"]:
                            erradas.append(i)
                    else:
                            informais.append(i)

    return erradas, informais                                          


# retorna uma lista de sugestões para correção de
# cada palavra identificada na função identifica


def corretor_frase(erradas, dicionario):

        niveis = []
        for erro in erradas:
                niveis.append(nivel_correcao(erro,dicionario))
        return niveis

                
# retorna uma lista com a soma do que é
# gerado em insere, exclui e substitui


def nivel_correcao(palavra, dicionario):

        import re
        if not re.match("^[a-zA-Z]+$",palavra) and len(palavra)>20:
                nivel = 3
                return nivel
        
        nivel = 1
        mod = modifica(palavra)
        for i in mod:
                if i in dicionario["formal"] or i in dicionario["informal"]:
                        return nivel
        
        nivel += 1
        if len(palavra)>15:
                return nivel
        for i in mod:
                for j in modifica(i):
                        if j in dicionario["formal"] or j in dicionario["informal"]:
                                return nivel

        nivel += 1

               
        return nivel



# score de uma frase


def peso(palavras, corretas, um, dois, impossiveis, informais):

        if palavras>0 and palavras<15:
                score = 1.0
                informal = (informais/palavras)*0.5
                nivel_um = (um/palavras)*0.7
                nivel_dois = (dois/palavras)*0.8
                impossivel = (impossiveis/palavras)*1.0
                score -= (informal+
                          nivel_um+
                          nivel_dois+
                          impossivel
                        )
        else:
                score = 0.0

        print ("")
        print ("Número de palavras: "+str(palavras))
        print ("Corretas: "+str(corretas))
        print ("Completamente erradas: "+str(impossiveis))
        print ("Com erro nivel um: "+str(um))
        print ("Com erro nivel dois: "+str(dois))
        print ("Informais: "+str(informais))
        print ("")
        print ("Score: "+str(float(format(score, '.2f'))))
        print ("")
        
