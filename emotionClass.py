#Patrick Wilson
#EECS 498 HW 3


#!/usr/bin/env python
import re
import sys
import os
import operator
import math
import cProfile
import numpy
from sentstotweets import sentstotweets




def spacePeriod(input):
    final_string = ''
    for tweet in input:
      pattern = re.sub("\. "," . ",tweet)
      final_string = final_string + pattern
    return final_string

def spaceCommaApos(input):
    pattern = re.sub("\,"," , ",input)
    pattern = re.sub("\'"," ' ",pattern)
    return pattern

def removePunc(input):
    pattern = re.sub("\@","",input)
    pattern = re.sub("\!","",pattern)
    pattern = re.sub("\&","",pattern)
    pattern = re.sub("\+","",pattern)
    pattern = re.sub("\?","",pattern)
    pattern = re.sub("',","",pattern)
    pattern = re.sub("\'","",pattern)
    pattern = re.sub("u'","",pattern)
    pattern = re.sub("\$","",pattern)
    pattern = re.sub("\(","",pattern)
    pattern = re.sub("\)","",pattern)
    pattern = re.sub("\#","",pattern)
    pattern = re.sub("\*","",pattern)
    pattern = re.sub("\/","",pattern)
    pattern = re.sub("\.","",pattern)
    pattern = re.sub("\,","",pattern)
    pattern = re.sub("\=","",pattern)
    pattern = re.sub("\-","",pattern)
    pattern = re.sub("\_","",pattern)
    pattern = re.sub("\:","",pattern)
    pattern = re.sub("\;","",pattern)
    pattern = re.sub("\"","",pattern)
    pattern = re.sub("\[","",pattern)
    pattern = re.sub("\]","",pattern)
    pattern = re.sub(r"http","",pattern)
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


def getEmotion(query):
  queryList = query.split()
  emotionlist = ['#love OR #attached OR #devotion', '#happy OR #elated',
                      '#amused OR #excited OR #firedup',
                      '#blessed OR #grateful', '#sad OR #depressed OR #heartbroken',
                      '#angry OR #mad OR #infuriated', '#afraid OR #scared OR #terrified',
                      '#humiliating OR #embarrassing OR #ashamed']
  complete = {}
  total = {}
  totalwords = 0
  wordsperclass = {}
  count = 0
  for words in emotionlist:
    tempdic = {}
    numwords=0
    training = emotionlist[count]
    count +=1
    test_set = []
    wordsofclass = ''
    with open('tweetlists/' + training+".txt") as f:
        for line in f:
            test_set = line.split()
            wordsofclass = wordsofclass + ' ' + line
    wordsperclass[words] = wordsofclass
    totalwords = populate(total,test_set,totalwords)

  count = 0
  for words in emotionlist:
    tempdic = {}
    numwords=0
    training = emotionlist[count]
    count+=1
    readfile = spacePeriod(wordsperclass[training])
    readfile = spaceCommaApos(readfile)
    readfile = removePunc(readfile)
    #readfile = removeStopWords(readfile)
    test_set = readfile.split()
    numwords = populate(tempdic,test_set,numwords)
    prepare(tempdic,totalwords,len(total),numwords)
    tempdic['numberofwordsinthisclass']=numwords
    complete[words] = tempdic


  problist = []
  for word in emotionlist:
    prob = calcProb(complete[word],queryList,float(1)/len(emotionlist),len(total),complete[word]['numberofwordsinthisclass'])
    problist.append(prob)

  print max(problist)

  num = 0
  finalemotion = ''
  for thing in emotionlist:

    if (max(problist)==problist[num]):
      finalemotion = thing
      print str(problist[num]) + " " + finalemotion

    num+=1
  return finalemotion
