from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment
from tweetsentiments import tweetsentiments
import json
from query2topic_emotion import findstuffaboutquery
from twitterizer import twitterizer
from pygoogle import pygoogle

twit = twitterizer()

class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):
        # handle a request by reading in the string then returning the reverse of it
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        print s
        if self.path == '/feelings':
            self.wfile.write( 'yolo' )
        elif self.path == '/twitter':
            self.wfile.write( 'dolo' )
        elif self.path == '/bing':
            self.wfile.write( 'dev' )

 
HTTPServer( ("", 3000), Handler).serve_forever()

#styling to use all data from tweet: ie show favorites and retweets
