## 
## Dom Parise 3/20/14
## Text classifier
## Contains the Classification and Classifier classes
##   Create a Classification with the proper arguments, and it will calculated relevent probabilities
##	 then call Classification.evaluate(tokens) to produce a logarithmic score based on the input
##
##   Create a Classifier to expose the train and test methods. 
##   Pass Classifier.train(classDocs) a dictionary with Class names as keys and lists of documents as values to train it
##   Then call Classifier.test(doc) to produce a classification for the given document 
##
import os, math
from preprocessor import PreProcessor

# pp = PreProcessor('stopwords.txt')

class Classification:

	# req: (str,list,int,dict,str)
	def __init__ (self, label, docs, numDocs, vocab, kind):
		self.pp = PreProcessor()
		self.kind = kind
		self.label = label
		self.getVocabValues(docs)
		self.prob = float(len(docs)) / float(numDocs)
		self.termProbs = dict()
		for doc in docs:
			if self.kind == 'language':
				tokens = self.pp.processForLanguage(doc)
			else:
				tokens = self.pp.processForLies(doc)
			for token in tokens:
				if token in self.vocab:
					self.termProbs[token] = ( tokens[token] + 1.0 ) / ( self.vocab[token] + len(vocab) )
				else:
					self.termProbs[token] = 1.0 / len(vocab)
	
	def getVocabValues (self, docs):
		self.numDocs = len(docs)
		for doc in docs:
			if self.kind == 'language':
				tokens = self.pp.processForLanguage(doc)
			else:
				tokens = self.pp.processForLies(doc)
		self.vocab = self.pp.tokens.counts

	def evaluate (self, tokens):
		score = math.log( self.prob )
		for token in tokens:
			if token in self.termProbs:
				score += math.log( self.termProbs[token] )
		return score


class Classifier:

	# req: str  -- use 'language' for biword probabilities
	def __init__ (self, kind):
		self.pp = PreProcessor()
		self.numDocs = 0
		self.kind = kind

	# dict with class[class] = list()
	def train (self, classDocs):
		self.classes = dict()
		for className in classDocs:
			self.numDocs += len(classDocs[className])
			for doc in classDocs[className]:
				if self.kind == 'language':
					tokens = self.pp.processForLanguage(doc)
				else:
					tokens = self.pp.processForLies(doc)
		for className in classDocs:
			self.classes[className] = Classification(className, classDocs[className], self.numDocs, self.pp.tokens.counts, self.kind)

	def test (self, doc):
		scores = dict()
		maxScore = (0.0,'-')
		if self.kind == 'language':
			tokens = self.pp.processForLanguage(doc)
		else:
			tokens = self.pp.processForLies(doc)
		for c in self.classes:
			score = self.classes[c].evaluate(tokens)
			scores[c] = score
			if maxScore[0] == 0.0:
				maxScore = (score,c)
			if score < maxScore[0]:
				maxScore = (score,c)
		return maxScore[1]
