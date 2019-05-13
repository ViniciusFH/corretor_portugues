while True:
    altera=True
    while altera:
        alteracao = input("Adicionar ou remover? ")
        if alteracao=="adicionar" or alteracao=="remover":
            altera=False
    palavra = input("Digite exatamente a palavra que quer %s: " %(alteracao))
    tipo_dicionario = True
    from grande_dicionario import dicionario
    while tipo_dicionario:
        tipo = input("Em qual dicionário? (formal/informal) ")
        if tipo=="formal" or tipo=="informal":
            if palavra in dicionario[tipo] and alteracao == "remover":
                tipo_dicionario = False
            else:
                print ("Esta palavra não está no dicionário %s" %(tipo))
    if alteracao == "adicionar":
        if tipo=="formal":
            dicionario["formal"].add(palavra)
            dicionario_novo = "dicionario = "+str(dicionario)
            novo = open("grande_dicionario.py","w")
            novo.write(dicionario_novo)
            novo.close()
            print("Feito!")
        else:
            dicionario["informal"].add(palavra)
            dicionario_novo = "dicionario = "+str(dicionario)
            novo = open("grande_dicionario.py","w")
            novo.write(dicionario_novo)
            novo.close()
            print("Feito!")

    else:
        if tipo=="formal":
            dicionario["formal"].remove(palavra)
            dicionario_novo = "dicionario = "+str(dicionario)
            novo = open("grande_dicionario.py","w")
            novo.write(dicionario_novo)
            novo.close()
            print("Feito!")
        else:
            dicionario["informal"].remove(palavra)
            dicionario_novo = "dicionario = "+str(dicionario)
            novo = open("grande_dicionario.py","w")
            novo.write(dicionario_novo)
            novo.close()
            print("Feito!")
