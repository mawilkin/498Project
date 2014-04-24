#!/usr/bin/python
# TEAM #SENTIMENT - EECS 498 - Information Retrieval
# Converts a set of links to a single document corpus. 
# Used to take set of links from bing to produce a single document to be sent to the alchemy API for sentiment analysis.
#

from bs4 import BeautifulSoup
import urllib2
import codecs
import requests
import re
import sys

# have one dictionary to save all words from all links
# have another dictionary to map link to specific corpus
# option to only read so many links

listExample = ['http://www.wikipedia.org', 'http://eecs.umich.edu']
num = 2			#urls to read

class URLtoCorpus:

	def __init__(self):
		self.myList = listExample
		self.urlToWords = {}		#map url to list of words
		self.allWords = []
		self.numToRead = num

	def stopWord(self, word):
		# add this later
		if word in stopWordList:
			return True 

	def createCorpus(self, page):
		self.urlToWords[page] = []

		#need to figure out this error
		try:
			r = requests.get(page)
		except requests.ConnectionError as e:
			return
		soup = BeautifulSoup(r.text)
		for elem in soup.find_all(['script', 'style']):
			elem.extract()
		text = soup.get_text()
		text = text.encode('utf-8')
		for word in text.split():
			# can edit this to match diff characters - currently alphanumeric , .
			if re.match('^[\w\'\,\.]+$', word):
				if word not in self.allWords:
					self.allWords.append(word)
				self.urlToWords[page].append(word)

	# opens URLS from file and extracts text
	def openURLsfromfile(self, filename):
		with open(filename) as pages:
			pages = pages.readlines()
			for i in range(self.numToRead):
				self.createCorpus(pages[i])

	# opens URLs from list and extracts text
	def openURLsfromlist(self, myList):
		for i in range(self.numToRead):
			self.createCorpus(myList[i])

	def printAllWords(self):
		for item in self.allWords:
			print item

	def wordsToString(self):
		s = str()
		for item in self.allWords:
			s += item + ' '
		return s


#USAGE - not sure if we're getting urls from python list or text file

# x = URLtoCorpus()
# x.openURLsfromfile(sys.argv[1])
# x.openURLsfromfile('/Users/nicholaskriete/Desktop/cs2014/498IR/Final_Project/urllist.txt')
# x.printAllWords()


# y = URLtoCorpus()
# y.openURLsfromlist(listExample)
# y.printAllWords()
# print y.urlToWords['http://www.wikipedia.org']
# print y.allWords

