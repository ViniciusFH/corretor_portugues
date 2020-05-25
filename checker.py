import Levenshtein
import json

with open('./formal.json') as file:
	formal = json.load(file)
	file.close()

with open('./informal.json') as file:
	informal = json.load(file)
	file.close()

class Checker:

	def __init__(self, dictionary):
	    
	    self.trieNode = { 'ends_here': False }
	    self.dictionary = dictionary


	def insert(self, word, dicType):

		if dicType != 'formal' and dicType != 'informal':
			return False

		return self.addWord(self.dictionary[dicType], word)

	def isFormal(self, word):

		return self.checkWord(word, self.dictionary['formal'])


	def isInformal(self, word):

		return self.checkWord(word, self.dictionary['informal'])


	def isWrong(self, word):

		isFormal = self.isFormal(word)

		if isFormal:

			return False

		isInformal = self.isInformal(word)

		if isInformal:

			return False

		return True


	def detectNonFormal(self, words):

		nonFormal = { 'wrong': [], 'informal': [] }

		for w in words:

			if not self.isFormal(w):

				if self.isInformal(w):

					nonFormal['informal'].append(w)
					continue

				nonFormal['wrong'].append(w)

		return nonFormal


	def getMinDistance(self, word):

		distances = []

		possibleWords = self.correct(word)

		if not possibleWords:
			return 3 # A distância 3 entra para a conta de "more".

		for w in possibleWords:

			levDist = Levenshtein.distance(word, w)

			if levDist == 1:
				return 1

			distances.append(levDist)

		return min(distances)


	def countDistances(self, words):

		distances = {}

		for w in words:

			minDistance = self.getMinDistance(w)

			if minDistance not in distances:
				distances[minDistance] = 0

			distances[minDistance] += 1

		return distances


	# Chama a função correctWord passando o dictionary.
	def correct(self, word):

		possibleWords = []

		if not self.isWrong(word):
			possibleWords.append(word)

		lastCorrect = self.getLastCorrect(word)

		correctNode = lastCorrect[0] 
		correctPiece = lastCorrect[1]

		max_distance = len(word) - len(correctPiece)

		possibleWords += self.guessPossibleWords(correctPiece, correctNode, max_distance)

		# possibleWords.sort(key=len)

		return possibleWords
		

	# Chama a função findShortestNode passando o último 
	def shortestNode(self, word):

		lastCorrect = self.getLastCorrect(word)

		correctNode = lastCorrect[0] 
		correctPiece = lastCorrect[1] 

		# Len de correctNode menor que 2 indica que há apenas um 'ends_here' naquele node,
		# ou seja, não há mais opções de palavras a partir dali. "word" ser diferente de sua
		# parte correta indica que uma parte está errada. Não podemos sugerir um próximo node se
		# há uma parte incorreta.
		if len(correctNode) < 2 or word != correctPiece:
			return []

		return self.findShortestNode(correctNode)






	def addWord(self, dictionary, word):

		if len(word) == 0:

			dictionary['ends_here'] = True
			return True

		ch = word[0] 

		if ch not in dictionary:

			dictionary[ch] = self.trieNode

		self.addWord(dictionary[ch], word[1:])



	# Retorna o endereço do Trie onde a palavra termina. 
	def getLastCorrect(self, word):

		node = self.dictionary['formal']
		correctPiece = ''

		for ch in word:

			if ch not in node:
				break

			node = node[ch]
			correctPiece += ch

		return node, correctPiece

	
	# Retorna um booleano conforme uma string consta ou não no dicionário.
	def checkWord(self, word, node):

		if len(word) == 0:

			if node['ends_here']:			
				return True

			return False

		ch = word[0]

		if ch not in node:
			return False
		
		return self.checkWord(word[1:], node[ch])


	'''
	Recebe uma palavra e retorna uma lista com outras palavras possíveis a partir da parte correta daquela.
	Se a função recebe "testk", por exemplo, ela identifica a parte correta "test" e retorna outras palavras a partir disso. 
	'''
	def guessPossibleWords(self, word, node, max_distance):

		if max_distance == 0:
			return []

		words = []

		for ch in node:

			if ch != 'ends_here':

				possibleWord = word + ch

				if node[ch]['ends_here']:
					words.append(possibleWord)

				words += self.guessPossibleWords(possibleWord, node[ch], max_distance - 1)

		return words


	def findShortestNode(self, node, distance = 1):

		distances = {}

		for l in node:

			if l != 'ends_here':

				if node[l]['ends_here']:

					distances[l] = distance

				else:

					distances[l] = self.findShortestNode(node[l], distance + 1)

		shortestDistance = min(distances.values())

		if distance != 1:

			return shortestDistance

		shortestNodes = []

		for node in distances:
			if distances[node] == shortestDistance:
				shortestNodes.append({"node": node, "distance": shortestDistance})

		return shortestNodes




dictionary = { 'formal': formal, 'informal': informal }
checker = Checker(dictionary)