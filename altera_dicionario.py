def altera_dicionario(alteracao, tipo, palavras):

    from grande_dicionario import dicionario
    mudanca = False

    if alteracao == "remover":
        for word in palavras:
            if word in dicionario[tipo]:
                dicionario[tipo].remove(word)
                mudanca = True
            else:
                print('"%s" não consta no dicionario %s.' %(word,tipo))

        if not mudanca:
            print("Nenhuma mudança feita.")
            return
                
    elif alteracao == "adicionar":
        for word in palavras:
            dicionario[tipo].add(word)

    novo = open("grande_dicionario.py","w")
    novo.write("dicionario = "+str(dicionario))
    novo.close()
    print("Feito!")


    
                
