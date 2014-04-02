#TEAM
#SENTIMENT

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
alchemyapi = AlchemyAPI()

def giveMeSentiment(demo_text):
	returnDic = {}
	'''
	print ('')
	print ('')

	print('Processing text: ', demo_text)
	print('')
	'''
	response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })
	returnDic['keywords'] = response
	returnDic['number'] = 0
	returnDic['swag'] = 'no clear topic'
	if response['status'] == 'OK':
		for keyword in response['keywords']:
			if(returnDic['number']<keyword['relevance']):
				returnDic['swag'] = keyword['text'].encode('utf-8')
				returnDic['number'] = keyword['relevance']

			'''
			print('text: ', keyword['text'].encode('utf-8'))
			print('relevance: ', keyword['relevance'])
			print('sentiment: ', keyword['sentiment']['type'])
			if 'score' in keyword['sentiment']:
				print('sentiment score: ' + keyword['sentiment']['score'])
			print('')
	else:
		print('Error in keyword extaction call: ', response['statusInfo'])


	print('')
	'''
	response = alchemyapi.sentiment('text',demo_text)
	returnDic['sentiment'] = response
	'''
	if response['status'] == 'OK':

		print('')
		print('## Document Sentiment ##')
		print('type: ', response['docSentiment']['type'])

		if 'score' in response['docSentiment']:
			print('score: ', response['docSentiment']['score'])
			print('')
			print('')

		# return response['docSentiment']['score']
	# else:
		# return response['statusInfo']
	'''

	return returnDic
