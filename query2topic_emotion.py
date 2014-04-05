import example
import math
from lymbix import Lymbix
lymbix = Lymbix('dfcad1488854c47dd26f30d3eb424c77e5606801')

def findstuffaboutquery(query):
  emotionlist = ['anger_loathing', 'enjoyment_elation',
    'amusement_excitement', 'contentment_gratitude', 'humiliation_shame',
    'fear_uneasiness', 'affection_friendliness', 'sadness_grief']
  returnDic = {}

  dic = lymbix.tonalize(query)
  sentiment = example.giveMeSentiment(query)

  emotion =  dic["dominant_emotion"]
  clarity =  dic ["clarity"]

  sentimentPosOrNeg = sentiment['sentiment']['docSentiment']['type']
  mainfocusWord = sentiment['swag']

  high = float(0)
  domEmotion = emotion
  for emotion in emotionlist:
    num = float(dic[emotion])
    if math.fabs(num)>high:
      high = math.fabs(num)
      domEmotion = emotion

  returnDic["emotion"]=domEmotion
  returnDic["focus"]=mainfocusWord
  print domEmotion
  print mainfocusWord
  return returnDic

bang = findstuffaboutquery("I really just dont like spiders. They are creepy and slimey.")
