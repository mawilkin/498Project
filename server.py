from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ThreadingMixIn
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment
from tweetsentiments import tweetsentiments
# from query2topic_emotion import findstuffaboutquery
from twitterizer import twitterizer
import json

twit = twitterizer()

# handle first response here
# return string (or otherwise) 
def feelings(s):
    print 'feeling module'
    res = dict()
    res['focus'] = giveMeSentiment(s)['swag']
    res['emotion'] = 'yolo'
    return res

def twitter(s):
    print 'twitter module'
    lst = list()
    lst.append(s)
    tweets = twit.top10Tweets( lst )
    res = dict()
    res['emotion'] = 'love'
    res['tweets'] = tweets
    return res

def bing(s): 
    print 'bing module'
    corpus = URLtoCorpus()
    links = bing_search( s ,'Web')
    corpus.numToRead = len(links)
    corpus.openURLsfromlist(links)
    s = corpus.wordsToString()
    sentiment = giveMeSentiment(s)
    res = dict()
    res['score'] = sentiment['sentiment']['docSentiment']
    res['image'] = bing_search( sentiment['swag'] ,'Image')
    return res


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        if self.path == '/feelings':
            self.wfile.write( json.dumps(feelings(s)) )
        elif self.path == '/twitter':
            self.wfile.write( json.dumps(twitter(s)) )
        elif self.path == '/bing':
            self.wfile.write( json.dumps(bing(s)) )
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
ThreadedHTTPServer(('0.0.0.0', 3000), Handler).serve_forever()
