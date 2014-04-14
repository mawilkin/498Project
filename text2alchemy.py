#TEAM
#SENTIMENT

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
alchemyapi = AlchemyAPI()

def giveMeSentiment(demo_text):
	returnDic = {}

	response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })
	returnDic['keywords'] = response
	returnDic['number'] = 0
	returnDic['focus'] = 'no clear topic'
	if response['status'] == 'OK':
		for keyword in response['keywords']:
			if(returnDic['number']<keyword['relevance']):
				returnDic['focus'] = keyword['text'].encode('utf-8')
				returnDic['number'] = keyword['relevance']

	response = alchemyapi.sentiment('text',demo_text)
	returnDic['sentiment'] = response

	return returnDic
