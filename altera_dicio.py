from grande_dicionario import dicionario
altera=True
while altera:
    alteracao = input("Adicionar ou remover? ")
    if alteracao=="adicionar" or alteracao=="remover":
        altera=False
tipo_dicionario = True
while tipo_dicionario:
    tipo = input("Em qual dicionário? (formal/informal) ")
    if tipo=="formal" or tipo=="informal":
        tipo_dicionario = False
palavras = []
frase = "Digite exatamente a palavra que quer %s: " %(alteracao)
outra = True
if alteracao=="remover":
    while outra:
        word = input(frase)
        if word == "xxx":
            outra = False
            break
        elif word in dicionario[tipo]:
            palavras.append(word)
            frase = "Quer remover outra? (digite xxx se nao): "
        else:
            print ("Esta palavra não está no dicionário %s" %(tipo))
else:
    while outra:
        word = input(frase)
        if word == "xxx":
            outra = False
            break
        else:
            palavras.append(word)
            frase = "Quer adicionar outra? (digite xxx se nao): "
        
if alteracao == "adicionar":
    if tipo=="formal":
        for w in palavras:
            dicionario["formal"].add(w)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("grande_dicionario.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")
    else:
        for w in palavras:
            dicionario["informal"].add(w)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("grande_dicionario.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")

else:
    if tipo=="formal":
        for w in palavras:
            dicionario["formal"].remove(w)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("grande_dicionario.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")
    else:
        for w in palavras:
            dicionario["informal"].remove(w)
        dicionario_novo = "dicionario = "+str(dicionario)
        novo = open("grande_dicionario.py","w")
        novo.write(dicionario_novo)
        novo.close()
        print("Feito!")
