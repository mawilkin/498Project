import operator
from lymbix import Lymbix
lymbix = Lymbix('dfcad1488854c47dd26f30d3eb424c77e5606801')


samplelist = ['I wish Steve Harvey was my father and guardian angel', 
			'Greek yogurt is so so excellent',
			'Word on the street is that you are obsessed with rodents',
			'OMG I LOVE GREEK YOGURT',
			'I am blessed to know you as a person']

class tweetsentiments:

	def __init__(self, samplelist):

		self.tweetlist = samplelist
		self.emotionlist = ['anger_loathing', 'enjoyment_elation',
			'amusement_excitement', 'contentment_gratitude', 'humiliation_shame',
			'fear_uneasiness', 'affection_friendliness', 'sadness_grief']
		self.sentiments = {}
		self.averages = {}

	def calcAvg(self):

		for tweet in self.tweetlist:
			self.sentiments[tweet] = {}		#sentiments[tweet][emotion] == number
			dic = lymbix.tonalize(tweet)

			for emotion in self.emotionlist:
				self.sentiments[tweet][emotion] = dic[emotion]
				if emotion in self.averages:
					self.averages[emotion] += abs(self.sentiments[tweet][emotion])
				else:
					self.averages[emotion] = abs(self.sentiments[tweet][emotion])
		
		for emotion in self.averages:
			self.averages[emotion] = float(self.averages[emotion])/len(self.tweetlist)

	def findMax(self):
		self.calcAvg()
		maximum = max(self.averages.iteritems(), key=operator.itemgetter(1))[0]
		return maximum

# usage
#tweets = tweetsentiments(samplelist)
#print tweets.findMax()