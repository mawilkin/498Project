#TEAM #SENTIMENT
#

# may require running:
# cd requests/kennethreitz-requests-b8128d6/
# python setup.py install
#

import urllib
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment

"""
class ServerHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
    	# converts html query to string
    	query = urllib.unquote_plus(self.path[19:]) 
    	links = bing_search(query,'Web')
    	corpus.openURLsfromlist(links)
    	s = corpus.wordsToString()
    	swag = giveMeSentiment(s)
    	print swag
        SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler
httpd = BaseHTTPServer.HTTPServer(('127.0.0.1',8000), Handler)
print "serving at port 8000"
httpd.serve_forever()
"""

corpus = URLtoCorpus()
query = 'justin bieber' 
links = bing_search(query,'Web')
corpus.numToRead = len(links)
corpus.openURLsfromlist(links)
s = corpus.wordsToString()
result = giveMeSentiment(s)