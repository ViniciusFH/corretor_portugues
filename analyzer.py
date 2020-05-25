import unidecode
import re
from checker import checker


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

def threeDistances(words):

	one, two, more = 0, 0, 0

	distances = checker.countDistances(words)

	if 1 in distances:
		one = distances[1]
		del distances[1]
      
	if 2 in distances:
		one = distances[2]
		del distances[2]

	for d in distances:
		more += distances[d]

	return one, two, more


def getScores(sentences):

	scores = []

	for s in sentences:

		# Divide a frase em palavras, aceitando ,;.:()?!.
		words = list(filter(None,re.split('[\"\'\,\;\.\:\(\)\?\! ]+',unidecode.unidecode(s.lower()))))

		if not words:
			scores.append({"sentence": s, "score": 0.0})
			continue

		nonFormal = checker.detectNonFormal(words)

		# Identifica palavras com erro ou informais. 
		wrong, informal = nonFormal['wrong'], nonFormal['informal']

		# Divide as palavras com erro níveis: um, dois ou mais.
		one, two, more = threeDistances(wrong)

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


