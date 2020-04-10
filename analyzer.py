import unidecode
import re
from checker import detectNonFormal, sentenceCorrection
from dictionary import dicionario as dictionary


def sortScore(scores, order):

	if order.lower() == 'asc':
		return sorted(scores, key = lambda i: i["score"])

	return sorted(scores, key = lambda i: i["score"], reverse=True)


def filterScore(scores, operator, value):

    if operator == "equal" or operator == "=":
    	return [s for s in scores if f["score"] == value]

    elif operator == "greater" or operator == ">":
    	return [s for s in scores if f["score"] > value]

    elif operator == "less" or operator == "<":
    	return [s for s in scores if f["score"] < value]

    elif operator == "less or equal" or operator == "<=":
    	return [s for s in scores if f["score"] <= value]

    elif operator == "greater or equal" or operator == ">=":
    	return [s for s in scores if f["score"] >= value]

    return scores
       

def getScores(sentences):

	scores = []

	for s in sentences:

		# Divide a frase em palavras, aceitando ,;.:()?!.
		words = list(filter(None,re.split('[\"\'\,\;\.\:\(\)\?\! ]+',unidecode.unidecode(s.lower()))))

		if not words:
			scores.append({"sentence": s, "score": 0.0})
			continue

		# Identifica palavras com erro ou informais. 
		wrong, informal = detectNonFormal(words,dictionary)

		# Divide as palavras com erro conforme o nível de correção necessário.
		one, two, more = sentenceCorrection(wrong, dictionary)

		# Calcula o score da frase.
		sentenceScore = calculateScore(len(words), one, two, more, len(informal))

		scores.append({"sentence": s, "score": sentenceScore})

	return scores


def calculateScore(words, one, two, more, informal):
        
    return float(format(1.0 - (0.5*informal+
                   0.7*one+
                   0.8*two+
                   more
                  )/ words, ".2f"))


def score(sentences, order='desc', operator='=', value=None):

	sentencesScore = getScores(sentences)

	if value and (type(value) == 'int' or type(value) == 'float'):
		sentencesScore = filterScore(sentencesScore, operator, value)

	sortedScores = sortScore(sentencesScore, order)

	print(sortedScores)

	return sortedScores


sentences = '¨¨¨¨'.split('$$')

print(getScores(sentences))