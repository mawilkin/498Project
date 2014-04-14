from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ThreadingMixIn
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from text2alchemy import giveMeSentiment
from twitterizer import twitterizer
import json
from emotionClass import getEmotion

twit = twitterizer()

# handle first response here
# return string (or otherwise) 

def feelings(s):
    print 'feeling module'
    res = dict()
    res['focus'] = giveMeSentiment(s)['focus']
    emotion = getEmotion(s)
    type = 'feeling'
    res['emotion'] = formatOutput(emotion, 'feeling')
    res['image'] = bing_search( res['focus'] ,'Image')
    return res

def twitter(s):
    print 'twitter module'
    res = dict()
    tweets = twit.top10Tweets( [s] )
    s = ''.join(tweets)
    emotion = getEmotion(s)
    type = 'twitter'
    res['emotion'] = formatOutput(emotion, 'twitter')
    res['tweets'] = list()
    for tweet in tweets:
        res['tweets'].append( (tweet, getEmotion(tweet),) )
    return res

def bing(s): 
    print 'bing module'
    corpus = URLtoCorpus()
    links = bing_search( s ,'Web')
    corpus.numToRead = len(links)
    corpus.openURLsfromlist(links)
    s = corpus.wordsToString()
    res = dict()
    sentiment = giveMeSentiment(s)
    res['score'] = sentiment['sentiment']['docSentiment']['score']
    return res

'''
#love OR #attached OR #devotion', '#happy OR #elated', 
                                '#amused OR #excited OR #firedup', 
                                '#blessed OR #grateful', '#sad OR #depressed OR #heartbroken',
                                '#angry OR #mad OR #infuriated', '#afraid OR #scared OR #terrified',
                                '#humiliating OR #embarrassing OR #ashamed'''

def formatOutput(emotion, type):
    if type == 'feeling':
        if emotion == '#love OR #attached OR #devotion':
            return ' love '
        elif emotion == '#happy OR #elated':
            return "'re happy about "
        elif emotion == '#amused OR #excited OR #firedup':
            return "'re excited about "
        elif emotion == '#blessed OR #grateful':
            return "'re grateful for "
        elif emotion == '#sad OR #depressed OR #heartbroken':
            return "'re sad about "
        elif emotion == '#angry OR #mad OR #infuriated':
            return "'re angry with "
        elif emotion == '#afraid OR #scared OR #terrified':
            return "'re scared of "
        elif emotion == '#humiliating OR #embarrassing OR #ashamed':
            return "'re embarrassed about "
    else:
        if emotion == '#love OR #attached OR #devotion':
            return ' loves '
        elif emotion == '#happy OR #elated':
            return " is happy with "
        elif emotion == '#amused OR #excited OR #firedup':
            return " is excited about "
        elif emotion == '#blessed OR #grateful':
            return " is grateful for "
        elif emotion == '#sad OR #depressed OR #heartbroken':
            return " is sad about "
        elif emotion == '#angry OR #mad OR #infuriated':
            return " is angry with "
        elif emotion == '#afraid OR #scared OR #terrified':
            return " is scared of "
        elif emotion == '#humiliating OR #embarrassing OR #ashamed':
            return " is embarrassed about "


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        if self.path == '/feelings':
            self.wfile.write( json.dumps( feelings(s)) )
        elif self.path == '/twitter':
            self.wfile.write( json.dumps( twitter(s) ))
        elif self.path == '/bing':
            self.wfile.write( json.dumps( bing(s) ))
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
ThreadedHTTPServer(('0.0.0.0', 3000), Handler).serve_forever()
