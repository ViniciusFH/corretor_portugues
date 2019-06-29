def peso_bruce(frases):

        from corretor import modifica, identifica, corretor_frase, nivel_correcao, peso
        from grande_dicionario import dicionario
        import unidecode
        import re
        for f in frases:
            score = 1.0
            palavras = [word.lower() for word in unidecode.unidecode(re.sub('[\"\'\,\;\.\:\(\)]+',"",f)).split()]
            score = 0.0
            if len(palavras)>0 and len(palavras)<15:
                erradas,informais = identifica(palavras,dicionario)
                corretas = len(palavras)-(len(erradas)+len(informais))
                um, dois, impossiveis = corretor_frase(erradas,dicionario)
                score = peso(len(palavras),corretas,um,dois,impossiveis,len(informais))


            print (f)
            print ("Score: "+str(float(format(score, '.2f'))))
            print ("")