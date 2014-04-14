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
    res['emotion'] = getEmotion(s)
    res['image'] = bing_search( res['focus'] ,'Image')
    return res

def twitter(s):
    print 'twitter module'
    res = dict()
    tweets = twit.top10Tweets( [s] )
    s = ''.join(tweets)
    res['emotion'] = getEmotion(s)
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
