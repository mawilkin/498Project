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

sys.stdout.encoding.encode('utf-8')
emotionlist = ['#love OR #attached OR #devotion', '#happy OR #elated',
                    '#amused OR #excited OR #firedup',
                    '#blessed OR #grateful', '#sad OR #depressed OR #heartbroken',
                    '#angry OR #mad OR #infuriated', '#afraid OR #scared OR #terrified',
                    '#humiliating OR #embarrassing OR #ashamed']

tweets = sentstotweets()
inputsteeeeez = tweets.top50Tweets()

for words in emotionlist:


  training = inputsteeeeez[words]   # training is list of tweets for each emotion
  readfile = removePunc(str(training))
  #readfile = removeStopWords(readfile)


  readfile = readfile.encode('utf-8').strip()
  test_set = readfile.split()
  with open('tweetlists/' + words+".txt", "a") as myfile:
    myfile.seek(0)
    myfile.write(readfile)
