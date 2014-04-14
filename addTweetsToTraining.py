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



sys.stdout.encoding.encode('utf-8')
emotionlist = ['#love OR #affection OR #devotion',
'#enjoy OR #elation',
'#amused OR #excited OR #firedup',
'#content OR #grateful',
'#sad OR #grief OR #heartbroken',
'#angry OR #loathe',
'#fear OR #scared OR #uneasy',
'#humiliating OR #embarrassing OR #shame']

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
