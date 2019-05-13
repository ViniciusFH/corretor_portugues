# gera uma lista de palavras inserindo cada letra
# do alfabeto em cada posiçao da palavra 


def insere(entrada, alfabeto):

        possibilidades = []
        exemplo = ""
        for pos in range(len(entrada)+1):
                for letra in alfabeto:
                        exemplo = entrada[:pos] + letra + entrada[pos:]
                        possibilidades.append(exemplo)
                        exemplo = ""
        return possibilidades


# gera uma lista de palavras excluindo
# uma letra por vez da palavra


def exclui(entrada):

        possibilidades = []
        exemplo = ""
        for i in range(len(entrada)):
                for j in range(len(entrada)):
                        if j != i:
                                exemplo += entrada[j]
                possibilidades.append(exemplo)
                exemplo = ""

        return possibilidades



# gera uma lista de palavras substituindo cada
# letra da palavra por uma letra do alfabeto


def substitui(entrada, alfabeto):
        
        possibilidades = []
        exemplo = ""

        for i in range(len(entrada)):
                exemplo = entrada[:i]
                for l in alfabeto:
                        exemplo += l
                        exemplo += entrada[i+1:]
                        possibilidades.append(exemplo)
                        exemplo = entrada[:i]

        return possibilidades



# gera uma lista de palavras trocando cada letra
# da palavra original com as suas vizinhas


def troca(entrada):

        possibilidades = []
        trocado = ""
        for i in range(len(entrada)-1):
                trocado += entrada[i+1]
                trocado += entrada[i]
                for j in range(i+2,len(entrada)):
                               trocado += entrada[j]
                possibilidades.append(trocado)
                trocado = ""
                for k in range(i+1):
                        trocado += entrada[k]
        return possibilidades




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

        sugestoes = {}
        niveis = []
        for erro in erradas:
                sugestoes[erro],nivel = corretor_palavra(erro,dicionario)
                niveis.append(nivel)
        return sugestoes,niveis

        
# retorna uma lista com a soma do que é
# gerado em insere, exclui e substitui


def corretor_palavra(palavra, dicionario):

        alfabeto = ["a","b","c","d","e","f","g","h",
                    "i","j","k","l","m","n","o","p",
                    "q","r","s","t","u","v","x","w","y","z"]

        nivel = 1

        possiveis = []
        possiveis += [
                w for w in insere(palavra, alfabeto)
                if w in dicionario["formal"] or w in dicionario["informal"]
                ]
        possiveis += [
                w for w in exclui(palavra)
                if w in dicionario["formal"] or w in dicionario["informal"]
                ]
        possiveis += [
                w for w in substitui(palavra, alfabeto)
                if w in dicionario["formal"] or w in dicionario["informal"]
                ]
        possiveis += [
                w for w in troca(palavra)
                if w in dicionario["formal"] or w in dicionario["informal"]
                ]
        
        """
        inserir = insere(palavra, alfabeto)
        excluir = exclui(palavra)
        substituir = substitui(palavra, alfabeto)
        trocar = troca(palavra)


        
        for word in inserir:
                if word in dicionario["formal"] or word in dicionario["informal"]:
                        possiveis.append(word)
        for word in excluir:
                if word in dicionario["formal"] or word in dicionario["informal"]:
                        possiveis.append(word)
        for word in substituir:
                if word in dicionario["formal"] or word in dicionario["informal"]:
                        possiveis.append(word)
        for word in trocar:
                if word in dicionario["formal"] or word in dicionario["informal"]:
                        possiveis.append(word)
        """

        if len(possiveis)==0:

                nivel += 1

                possiveis += [
                        insere(w, alfabeto) for w in insere(palavra, alfabeto)
                        if w in dicionario["formal"] or w in dicionario["informal"]
                        ]
                possiveis += [
                        exclui(w) for w in exclui(palavra)
                        if w in dicionario["formal"] or w in dicionario["informal"]
                        ]
                possiveis += [
                        substitui(w, alfabeto) for w in substitui(palavra, alfabeto)
                        if w in dicionario["formal"] or w in dicionario["informal"]
                        ]
                possiveis += [
                        troca(w) for w in troca(palavra)
                        if w in dicionario["formal"] or w in dicionario["informal"]
                        ]

                """
                
                for i in inserir:
                        lista = insere(i,alfabeto)
                        for word in lista:
                                if word in dicionario["formal"] or word in dicionario["informal"]:
                                        possiveis.append(word)
                for i in excluir:
                        lista = exclui(i)
                        for word in lista:
                                if word in dicionario["formal"] or word in dicionario["informal"]:
                                        possiveis.append(word)
                for i in substituir:
                        lista = substitui(i,alfabeto)
                        for word in lista:
                                if word in dicionario["formal"] or word in dicionario["informal"]:
                                        possiveis.append(word)

                for i in trocar:
                        lista = troca(i)
                        for word in lista:
                                if word in dicionario["formal"] or word in dicionario["informal"]:
                                        possiveis.append(word)
                """


                if len(possiveis)==0:
                        nivel = 3
                        

               
        return possiveis, nivel



# score de uma frase


def peso(palavras, corretas, um, dois, impossiveis, informais):

        if palavras>0 and palavras<15:
                score = 1.0
                informal = 0.1
                nivel_um = 0.2
                nivel_dois = 0.3
                impossivel = 0.5
                score -= (
                        impossiveis*impossivel+
                        um*nivel_um+
                        dois*nivel_dois+
                        informais*informal
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
        
