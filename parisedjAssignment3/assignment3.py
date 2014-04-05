# Dom Parise 3/20/14
#	calculations produced by my classifier
#
import os
from classifier import Classifier
	
docs = dict()
docs['lie'] = set()
docs['truth'] = set()
names = dict()
docset = set()

# produce the documents in a way that satisfies the inputs
for dirEntry in os.listdir ('./bestfriend.deception.training'):
	f = open( './bestfriend.deception.training/'+str(dirEntry) )
	doc = f.read()
	names[doc] = dirEntry
	if dirEntry[0] == 'l':
		docs['lie'].add(doc)
		docset.add(doc)
	else:
		docs['truth'].add(doc)
		docset.add(doc)

count = 0.0

# iterate through the documents, plucking a single test case from the set and training then testing it
for d in docset:
	
	if names[d][0] == 'l':
		docs['lie'].remove(d)
	else:
		docs['truth'].remove(d)

	lieDetector = Classifier('lies')
	classDocs = dict()
	classDocs['lie'] = list(docs['lie'])
	classDocs['truth'] = list(docs['truth'])
	lieDetector.train(classDocs)

	if lieDetector.test(d)[0] == names[d][0]:
		count += 1.0

	if names[d][0] == 'l':
		docs['lie'].add(d)
	else:
		docs['truth'].add(d)

# first output is 
print 'Resulting precision for deception data set'
print count / float(len(docset)) 

docs = dict()

f = open('./language.identification/training/English')
docs['English'] = f.read().split('\n')

f = open('./language.identification/training/French')
docs['French'] = f.read().split('\n')

f = open('./language.identification/training/Italian')
docs['Italian'] = f.read().split('\n')

c = Classifier('language')
c.train(docs)

solution = list()
f = open('./language.identification/solution')
for line in f:
	solution.append(line.strip().split()[1])

f = open('./language.identification/test')
count = 0.0
i = 0
for line in f:
	if c.test(line) == solution[i]:
		count += 1
	i += 1
# second output is this
print 'Resulting precision for language detection'
print str( count / 300.0 )
