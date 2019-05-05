altera=True
while altera:
    alteracao = input("Adicionar ou remover? ")
    if alteracao=="adicionar" or alteracao=="remover":
        altera=False
palavra = input("Digite exatamente a palavra que quer adicionar: ")
tipo_dicionario = True
while tipo_dicionario:
    tipo = input("Em qual dicionário? (formal/informal) ")
    if tipo=="formal" or tipo=="informal":
        tipo_dicionario = False
if alteracao == "adicionar":
    if tipo=="formal":
        from dicionario_arvore import dicionario
        if len(palavra)>3:
            dicionario[palavra[0]][palavra[1]][palavra[2]].append(palavra)
        else:
            dicionario["tres"].append(palavra)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("formal_arvore.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")
    else:
        from dicionario_informal import dicionario_informal
        if len(palavra)>3:
            dicionario_informal[palavra[0]][palavra[1]][palavra[2]].append(palavra)
        else:
            dicionario_informal["tres"].append(palavra)
        informal_novo = "dicionario = "+str(dicionario_informal)
        novo = open("informal_arvore.py","w")
        novo.write(informal_novo)
        novo.close()
        print("Feito!")

else:
    if tipo=="formal":
        from dicionario_arvore import dicionario
        if len(palavra)>3:
            dicionario[palavra[0]][palavra[1]][palavra[2]].remove(palavra)
        else:
            dicionario["tres"].remove(palavra)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("dicionario_arvore.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")
    else:
        from dicionario_informal import dicionario_informal
        if len(palavra)>3:
            dicionario_informal[palavra[0]][palavra[1]][palavra[2]].remove(palavra)
        else:
            dicionario_informal["tres"].remove(palavra)
        informal_novo = "dicionario = "+str(dicionario_informal)
        novo = open("dicionario_informal.py","w")
        novo.write(informal_novo)
        novo.close()
        print("Feito!")
