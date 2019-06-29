def bruce (subrede):

	import re
	import unidecode
	from grande_dicionario import dicionario
	r = open("bruce_"+subrede+".txt", "r", encoding="utf-8")
	text = r.read()
	lower = text.lower()
	no_special = unidecode.unidecode(lower)
	frases = re.findall('data-msgtopost="([\w ]+)', no_special)
	palavras = set()
	for f in frases:
		for word in f.split():
			palavras.add(word)
	erradas = set()
	for p in palavras:
		if p not in dicionario["formal"]:
			erradas.add(p)

	return frases, palavras, erradas