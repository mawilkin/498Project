from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ThreadingMixIn
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment
from tweetsentiments import tweetsentiments
from query2topic_emotion import findstuffaboutquery
from twitterizer import twitterizer
import json

twit = twitterizer()

# handle first response here
# return string (or otherwise) 
def feelings(s):
    print 'feeling module'
    # res = findstuffaboutquery(s)
    res = dict()
    return json.dumps( res )

def twitter(s):
    print 'twitter module'
    lst = list()
    lst.append(s)
    tweets = twit.top10Tweets( lst )
    tweetSentiment = tweetsentiments( tweets )
    tweetEmotion = tweetSentiment.findMax()
    res = dict()
    res['emotion'] = tweetSentiment.findMax()
    res['tweets'] = tweets
    return json.dumps( res )

def bing(s): 
    print 'bing module'
    corpus = URLtoCorpus()
    links = bing_search( s ,'Web')
    corpus.numToRead = len(links)
    corpus.openURLsfromlist(links)
    s = corpus.wordsToString()
    result = giveMeSentiment(s)
    return json.dumps( result )


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        if self.path == '/feelings':
            self.wfile.write( feelings(s) )
        elif self.path == '/twitter':
            self.wfile.write( twitter(s) )
        elif self.path == '/bing':
            self.wfile.write( bing(s) )
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
ThreadedHTTPServer(('0.0.0.0', 3000), Handler).serve_forever()
