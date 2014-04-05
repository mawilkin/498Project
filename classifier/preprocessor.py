#
# Dom Parise - 2/4/14
# Text Tokenizer. Creates a counted set of tokens
#

import re 

# checks for SGML tags
def markup (line):
	return re.match(r'<\S+>',line)

def quote (s, counts):
	if ( "'" not in s ) and ( '"' not in s ) or s == None:
		return s
	s = s.strip('"')
	if "'" not in s:									 # "words"
		return s
	w = s.strip("'")
	if ( "'" in w ) or ( s[-1] == "'" and s[0] != "'" ): # posessive
		add("'s",counts)
	return w.split("'")[0]

def punct (s):
	if s == ',' or s == '.' or s == '!' or s == '?':
		raise None
	if s[-1] == ',' or s[-1] == '.' or s[-1] == '!' or s[-1] == '?':
		return s[:-1]
	return s

def paren (s):
	if s[0] == '(':
		s = s[1:]
	if s != '' and s[-1] == ')':
		s = s[:-1]
	return s

def eq (s):
	ret = list()
	if '=' not in s or s == None:
		ret.append(s)
		return ret
	if s == '=':
		raise None
	ret.extend( s.split('=') )	
	return ret

def dash (lst):
	if lst == None:
		raise None
	ret = list()
	for s in lst:
		ret.append(s)
		if '-' not in s or s == None:
			continue
		ret.extend(s.split('-'))
	return ret


def slash (lst):
	if lst == None:
		raise None
	ret = list()
	for s in lst:
		if s == None:
			continue
		if '/' not in s:
			ret.append(s)
			continue
		tokens = s.split('/')
		allAlpha = True
		for w in tokens:
			if not w.isalpha():
				allAlpha = False
		if not allAlpha:									# date num/num/num
			ret.append(s)
			continue
		ret.extend(tokens)
	return ret


def add (s, counts):
	if s in counts:
		counts[s] += 1
	else:
		counts[s] = 1
	return


class TokenSet:
	
	def __init__ (self):
		self.counts = dict()
		self.count = 0;
		return

	def process (self, s):
		self.count += 1
		if not markup(s):
			s = s.lower()
			try:
				if re.match(r'\.+$',s):
					raise None
				s = quote(s, self.counts)
				s = punct(s)
				s = paren(s)
				s = eq(s)
				s = dash(s)
				s = slash(s)
				return s
			except:
				return None

	def add (self, s):
		add(s,self.counts)
		return

	def report (self):
		print ('Processed: '+ str(self.count) )
		print ('Total words in collection: ' + str(sum( self.counts.values() )) )
		print ('Vocabulary size: ' + str(len( self.counts )) )
		return


#
# Dom Parise - 2/22/14
# Text preprocessor from assignment1
#
import os

class PreProcessor:

	def __init__ (self):
		self.tokens = TokenSet()
	
	def addToSet (self, s, counts):
		if s in counts:
			counts[s] += 1
		else:
			counts[s] = 1
		return

	def processForLies (self, line):
		tokens = dict()
		if line != None:
			for s in line.split():
				w = self.tokens.process(s)  
				if w != None:
					for t in w:
						self.tokens.add(t) 
						self.addToSet(t,tokens)
		return tokens


	def processForLanguage (self, text):
		tokens = dict()
		for i in range(len(text) - 2):
			self.tokens.add(text[i:i+2])
			self.addToSet(text[i:i+2],tokens)
		return tokens