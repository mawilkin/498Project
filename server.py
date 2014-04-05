from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ThreadingMixIn
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment
from tweetsentiments import tweetsentiments
from query2topic_emotion import findstuffaboutquery
from twitterizer import twitterizer

twit = twitterizer()

# handle first response here
# return string (or otherwise) 
def feelings(s):
    return s

def twitter(s):
    return s

def bing(s): 
    return s


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
