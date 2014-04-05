#Patrick Wilson
#EECS 498 HW 3


#!/usr/bin/env python
import re
import sys
import os
import operator
import porter
import math
import cProfile
import numpy




def spacePeriod(input):
    pattern = re.sub("\. "," . ",input)
    return pattern

def spaceCommaApos(input):
    pattern = re.sub("\,"," , ",input)
    pattern = re.sub("\'"," ' ",pattern)
    return pattern

def removePunc(input):
    pattern = re.sub("\."," ",input)
    pattern = re.sub("\,"," ",pattern)
    pattern = re.sub("\'"," ",pattern)
    pattern = re.sub("\+"," ",pattern)
    pattern = re.sub("\?"," ",pattern)
    pattern = re.sub("\$"," ",pattern)
    pattern = re.sub("\("," ",pattern)
    pattern = re.sub("\)"," ",pattern)
    pattern = re.sub("\*"," ",pattern)
    pattern = re.sub("\/"," ",pattern)
    pattern = re.sub("\="," ",pattern)
    pattern = re.sub("\-"," ",pattern)
    pattern = re.sub("\:"," ",pattern)
    pattern = re.sub("\;"," ",pattern)
    pattern = re.sub("\""," ",pattern)
    #pattern = re.sub("\\","",pattern)
    return pattern

stopwordlist = ["a","all","an","and","any","are","as","be","been",
"but","by","few","for","have","he","her","here","him","his","how",
"i","in","is","it","its","many","me","my","none","of","on","or",
"our","she","some","the","their","them","there","they","that",
"this","us","was","what","when","where","which","who","why","will",
"with","you","your","to","at","from"]

def isStopword(word):
    for stopword in stopwordlist:
        if (word==stopword):
            return True
    return False

def removeStopWords(input):
    remove = '|'.join(stopwordlist)
    regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
    out = regex.sub("", input)
    return out

def stem(readfile):
  output = ''
  word = ''
  line = readfile
  if line == '':
    return
  for c in line:
    if c.isalpha():
      word += c.lower()
    else:
      if word:
        output += p.stem(word, 0,len(word)-1)
        word = ''
      output += c.lower()
  return output

def populate(dictionary,words,num):
  for word in words:
    num+=1
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
  return num



def calcProb(dic,words,okno,numwords,x):
  num = math.log(okno)
  for word in words:
    if word in dic:
      num += math.log(dic[word])
    else:
      num += math.log(float(1)/(x+numwords))
  return num

def prepare(dic,totalnum,numwords,x):
  for key in dic:
      first = float((dic[key]+1))/(x+numwords)
      dic[key]=first




emotionlist = ['anger_loathing', 'enjoyment_elation',
    'amusement_excitement', 'contentment_gratitude', 'humiliation_shame',
    'fear_uneasiness', 'affection_friendliness', 'sadness_grief']
bangerz = "I seriously dislike kitchens"
readfile = spacePeriod(bangerz)
readfile = spaceCommaApos(readfile)
readfile = removePunc(readfile)
readfile = removeStopWords(readfile)
#readfile = stem(readfile)
#note in read me about stemming vs non
queryList = readfile.split()

complete = {}
total = {}
totalwords = 0
for words in emotionlist:
  tempdic = {}
  numwords=0
  training = "This will be the list I can promise you that swag"
  readfile = spacePeriod(training)
  readfile = spaceCommaApos(readfile)
  readfile = removePunc(readfile)
  readfile = removeStopWords(readfile)
  test_set = readfile.split()
  totalwords = populate(total,test_set,totalwords)


for words in emotionlist:
  tempdic = {}
  numwords=0
  training = "This will be the list I can promise you that swag"
  readfile = spacePeriod(training)
  readfile = spaceCommaApos(readfile)
  readfile = removePunc(readfile)
  readfile = removeStopWords(readfile)
  test_set = readfile.split()
  numwords = populate(tempdic,test_set,numwords)
  prepare(tempdic,totalwords,len(total),numwords)
  tempdic['numberofwordsinthisclass']=numwords
  complete[words] = tempdic


problist = []
for word in emotionlist:
  prob = calcProb(complete[word],queryList,float(1)/len(emotionlist),len(total),complete[word]['numberofwordsinthisclass'])
  problist.append(prob)








'''


numtw=0
numlw=0
totalwords=0
happy = {}
sad = {}
total = {}


words = "I love happy peace woo like"
readfile = spacePeriod(words)
readfile = spaceCommaApos(readfile)
readfile = removePunc(readfile)
readfile = removeStopWords(readfile)
#readfile = stem(readfile)
#note in read me about stemming vs non
test_set = readfile.split()
numlw = populate(happy,test_set,numlw)
totalwords = populate(total,test_set,totalwords)


words = "I hate sad worry dislike"
readfile = spacePeriod(words)
readfile = spaceCommaApos(readfile)
readfile = removePunc(readfile)
readfile = removeStopWords(readfile)
#readfile = stem(readfile)
#note in read me about stemming vs non
test_set = readfile.split()
numtw = populate(sad,test_set,numtw)
totalwords = populate(total,test_set,totalwords)


prepare(sad,totalwords,len(total),numtw)
prepare(happy,totalwords,len(total),numlw)

sadprob = calcProb(sad,queryList,.5,len(total),numtw)
happyprob = calcProb(happy,queryList,.5,len(total),numlw)

if (sadprob>happyprob):
  print "SAD"
else:
  print "HAPPY"


'''
