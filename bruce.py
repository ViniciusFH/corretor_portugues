def filtro(scores, operador, valor):

        if operador == "igual" or "=":
                return [f for f in scores if f[1]==valor]
        elif operador == "maior" or ">":
                return [f for f in scores if f[1]>valor]
        elif operador == "menor" or "<":
                return [f for f in scores if f[1]<valor]





def score(frases):

        from grande_dicionario import dicionario
        import unidecode
        import re
        scores = []
        for f in frases:
            palavras = [word.lower() for word in unidecode.unidecode(re.sub('[\"\'\,\;\.\:\(\)]+',"",f)).split()]
            if len(palavras)>0 and len(palavras)<15:
                erradas,informais = identifica(palavras,dicionario)
                corretas = len(palavras)-(len(erradas)+len(informais))
                um, dois, impossiveis = corretor_frase(erradas,dicionario)
                score = peso(len(palavras),corretas,um,dois,impossiveis,len(informais))
                scores.append((f,score))

        return scores





def frases(subrede):

	import re
	import unidecode
	from grande_dicionario import dicionario
	r = open(subrede+".txt", "r", encoding="utf-8")
	raw = r.read()
	return re.findall('data-msgtopost="([\w ]+)', unidecode.unidecode(raw.lower()))





def peso(palavras, corretas, um, dois, impossiveis, informais):
        
        return float(format(1.0 - (0.5*informais+
                       0.7*um+
                       0.8*dois+
                       impossiveis
                      )/ palavras, ".2f"))





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

        # retorna uma lista de sugestões para correção de
        # cada palavra identificada na função identifica

        niveis = []
        for erro in erradas:
                niveis.append(nivel_correcao(erro,dicionario))
        return niveis.count(1),niveis.count(2),niveis.count(3)





def identifica(palavras, dicionario):

# numa dada frase, identifica quais palavras nao
# pertencem ao dicionario, e devolve uma lista com elas
    
    
    erradas, informais = [], []

    for i in palavras:
            if i not in dicionario["formal"]:
                    if i not in dicionario["informal"]:
                            erradas.append(i)
                    else:
                            informais.append(i)

    return erradas, informais





def modifica(palavra):

        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        
        divide = [(palavra[:i], palavra[i:])    for i in range(len(palavra) + 1)]
        
        deleta = [E + D[1:]                     for E, D in divide if D]
        troca = [E + D[1] + D[0] + D[2:]        for E, D in divide if len(D)>1]
        substitui = [E + c + D[1:]              for E, D in divide if D for c in alfabeto]
        insere = [E + c + D                     for E, D in divide for c in alfabeto]
        
        return set(deleta + troca + substitui + insere)