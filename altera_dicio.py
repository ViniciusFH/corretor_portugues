altera=True
while altera:
    alteracao = input("Adicionar ou remover? ")
    if alteracao=="adicionar" or alteracao=="remover":
        altera=False
palavra = input("Digite exatamente a palavra que quer %s: " %(alteracao))
tipo_dicionario = True
while tipo_dicionario:
    tipo = input("Em qual dicionário? (formal/informal) ")
    if tipo=="formal" or tipo=="informal":
        tipo_dicionario = False
if alteracao == "adicionar":
    if tipo=="formal":
        from formal_arvore import formal
        if len(palavra)>3:
            formal[palavra[0]][palavra[1]][palavra[2]].append(palavra)
        else:
            formal["quatro"].append(palavra)
        formal_novo = "formal = "+str(formal)
        novo = open("formal_arvore.py","w")
        novo.write(formal_novo)
        novo.close()
        print("Feito!")
    else:
        from informal_arvore import informal
        if len(palavra)>3:
            informal[palavra[0]][palavra[1]][palavra[2]].append(palavra)
        else:
            informal["quatro"].append(palavra)
        informal_novo = "informal = "+str(informal)
        novo = open("informal_arvore.py","w")
        novo.write(informal_novo)
        novo.close()
        print("Feito!")

else:
    if tipo=="formal":
        from formal_arvore import formal
        if len(palavra)>3:
            formal[palavra[0]][palavra[1]][palavra[2]].remove(palavra)
        else:
            formal["quatro"].remove(palavra)
        formal_novo = "formal = "+str(formal)
        novo = open("formal_arvore.py","w")
        novo.write(formal_novo)
        novo.close()
        print("Feito!")
    else:
        from informal_arvore import informal
        if len(palavra)>3:
            informal[palavra[0]][palavra[1]][palavra[2]].remove(palavra)
        else:
            informal["quatro"].remove(palavra)
        informal_novo = "informal = "+str(informal)
        novo = open("informal.py","w")
        novo.write(informal_novo)
        novo.close()
        print("Feito!")
