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


def identifica(palavras, dicionario, informal):
    
    
    erradas = []
    informais = []
    for i in palavras:
            if len(i)<5:
                    if i not in dicionario["quatro"]:
                            if i in informal["quatro"]:
                                    informais.append(i)
                            else:
                                    erradas.append(i)
            elif i not in dicionario[i[0]][i[1]][i[2]][i[3]]:
                    if i in informal[i[0]][i[1]][i[2]][i[3]]:
                            informais.append(i)
                    else:
                            erradas.append(i)

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

        inserir = insere(palavra, alfabeto)
        excluir = exclui(palavra)
        substituir = substitui(palavra, alfabeto)
        trocar = troca(palavra)


        for word in inserir:
                
                if len(word)<5:
                        if word in dicionario["quatro"]:
                                possiveis.append(word)
                else:
                        if word in dicionario[word[0]][word[1]][word[2]][word[3]]:
                                possiveis.append(word)
                
        for word in excluir:
                
                if len(word)<5:
                        if word in dicionario["quatro"]:
                                possiveis.append(word)
                else:
                        if word in dicionario[word[0]][word[1]][word[2]][word[3]]:
                                possiveis.append(word)
                
        for word in substituir:

                if len(word)<5:
                        if word in dicionario["quatro"]:
                                possiveis.append(word)
                else:
                        if word in dicionario[word[0]][word[1]][word[2]][word[3]]:
                                possiveis.append(word)

        for word in trocar:

                if len(word)<5:
                        if word in dicionario["quatro"]:
                                possiveis.append(word)
                else:
                        if word in dicionario[word[0]][word[1]][word[2]][word[3]]:
                                possiveis.append(word)



        if len(possiveis)==0:

                nivel += 1
                
                for i in inserir:
                        lista = insere(i,alfabeto)
                        for word in lista:
                                if len(word)<5:
                                        if word in dicionario["quatro"] and word not in possiveis:
                                                possiveis.append(word)
                                else:
                                        if word in dicionario[word[0]][word[1]][word[2]][word[3]] and word not in possiveis:
                                                possiveis.append(word)
                for i in excluir:
                        lista = exclui(i)
                        for word in lista:
                                if len(word)<5:
                                        if word in dicionario["quatro"] and word not in possiveis:
                                                possiveis.append(word)
                                else:
                                        if word in dicionario[word[0]][word[1]][word[2]][word[3]] and word not in possiveis:
                                                possiveis.append(word)
                for i in substituir:
                        lista = substitui(i,alfabeto)
                        for word in lista:
                                if len(word)<5:
                                        if word in dicionario["quatro"] and word not in possiveis:
                                                possiveis.append(word)
                                else:
                                        if word in dicionario[word[0]][word[1]][word[2]][word[3]] and word not in possiveis:
                                                possiveis.append(word)

                for i in trocar:
                        lista = troca(i)
                        for word in lista:
                                if len(word)<5:
                                        if word in dicionario["quatro"] and word not in possiveis:
                                                possiveis.append(word)
                                else:
                                        if word in dicionario[word[0]][word[1]][word[2]][word[3]] and word not in possiveis:
                                                possiveis.append(word)


        if len(possiveis)==0:
                nivel = 3
                        

               
        return possiveis, nivel



# classifica em niveis o quanto uma frase está próxima do dicionário


def peso(palavras, sugestoes, niveis, informais):

        score = 1.0
        informal = 0.2
        nivel_um = 0.3
        nivel_dois = 0.4
        impossivel = 0.5
        impossiveis = len([impossivel for impossivel in sugestoes if len(sugestoes[impossivel])==0])
        possiveis = len([possivel for possivel in sugestoes if len(sugestoes[possivel])>0])
        informais = len(informais)
        um = len([nivel for nivel in niveis if nivel==1])
        dois = len([nivel for nivel in niveis if nivel==2])
        if len(palavras)>15 or impossiveis==len(palavras):
                score = 0.0
        else:
                score -= (impossiveis*impossivel)+(um*nivel_um)+(dois*nivel_dois)+(informais*informal)

        
        print ("Corretas: "+str((len(palavras)-len(sugestoes))-informais))
        print ("Completamente erradas: "+str(impossiveis))
        print ("Com erro nivel um: "+str(um))
        print ("Com erro nivel dois: "+str(dois))
        print ("Informais: "+str(informais))
        print ("")
        print ("Score: "+str(float(format(score, '.2f'))))
        


        """

        print(informais)

        if len(sugestoes)==0:
                print("Tudo certo. Nota 1.0")
                return

        if len(palavras)>15:
                print("Frase muito grande. Nota 0")
                return

        impossiveis = [impossivel for impossivel in sugestoes if len(sugestoes[impossivel])==0]
        if len(impossiveis)>0:
                print("Pelo menos 1 palavra impossível de ser corrigida. Nota 0.")
                return
        
        if len(palavras)==len(sugestoes):
                print("Todas as palavras estão erradas. Nota 0.")
                return
        
        if len(palavras)>2:

                possiveis = [possivel for possivel in sugestoes if len(sugestoes[possivel])>0]
                certas = len(palavras)-len(sugestoes)

                if (certas*100)/len(palavras)>=80:
                        print("%s%s das palavras estão certas. Nota 0.7" %(int((certas*100)/len(palavras)),"%"))
                        return
                if (certas*100)/len(palavras)>=50:
                        print("%s%s das palavras estão certas. Nota 0.5" %(int((certas*100)/len(palavras)),"%"))
                        return
                if (certas*100)/len(palavras)<50:
                        print("%s%s das palavras estão certas. Nota 0.3" %(int((certas*100)/len(palavras)),"%"))
                        return
        else:
                print("Frase com duas palavras e uma delas está errada. Nota 0.3")
                return




 
        print ("%s palavras" %(len(palavras)))
        print ("%s erradas" %(len(sugestoes)))
        print ("%s pode(m) ser corrigida(s)" %(len(possiveis)))
        print ("%s em Nivel 1 de correçao" %(len(nivel_um)))
        print ("%s em Nivel 2 de correçao" %(len(nivel_dois)))
        print ("%s nao pode(m) ser corrigida(s)" %(len(impossiveis)))
                                

                nivel_um = [nivel for nivel in niveis if nivel==1]
                nivel_dois = [nivel for nivel in niveis if nivel==2]


        if len(sugestoes)<len(palavras):
                

                if len(impossiveis)==0:
                        classificacao = "Nivel B: %s de %s tokens sao palavras, e todos podem ser corrigidos em primeira instancia." %((len(palavras)-len(possiveis)),len(palavras))

                elif len(possiveis)==0:
                        classificacao = "Nivel D: %s de %s tokens sao palavras, mas nenhum pode ser corrigido em primeira instancia." %((len(palavras)-len(impossiveis)),len(palavras))
                
                else:
                        classificacao = "Nivel C: %s de %s tokens sao palavras, %s pode(m) ser corrigido(s) em primeira instancia, e %s nao." %((len(palavras)-(len(possiveis)+len(impossiveis)),len(palavras),len(possiveis),len(impossiveis)))
        

        else:
                if len(impossiveis)==0:
                        classificacao = "Nivel E: Nenhum token é uma palavra, mas todos podem ser corrigidos em primeira instancia."
                elif len(possiveis)==0:
                        classificacao = "Nivel G: Nenhum token é uma palavra e nenhum pode ser corrigido em primeira instancia."
                else:
                        classificacao = "Nivel F: nenhum token é uma palavra mas %s pode(m) ser corrigido(s) em primeira instancia" %(len(possiveis))


        print (classificacao)
"""
