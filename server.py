from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from bing2URL import bing_search
from linksToCorpus import URLtoCorpus
from example import giveMeSentiment
from tweetsentiments import tweetsentiments
import json
from twitterizer import twitterizer
from pygoogle import pygoogle

twit = twitterizer()

class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):
        # handle a request by reading in the string then returning the reverse of it     
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        print s
        dic = json.loads(s)
        if dic['which'] == 'feelings':
            lst = list()
            lst.append(dic['query'])
            querySentiment = tweetsentiments( lst )
            queryEmotion = querySentiment.findMax()
            print queryEmotion
            self.wfile.write( queryEmotion )
        elif dic['which'] == 'twitter':
            tweets = twit.top50Tweets( dic['query'].split() )
            tweetSentiment = tweetsentiments( tweets )
            tweetEmotion = tweetSentiment.findMax()
            print tweetEmotion
            tweetEmotion = 'Twitter feels ' + str(tweetEmotion) + ' about __subject__'
            self.wfile.write( tweetEmotion )
        elif dic['which'] == 'bing':
            corpus = URLtoCorpus()
            links = bing_search( dic['query'] ,'Web')
            corpus.numToRead = len(links)
            corpus.openURLsfromlist(links)
            s = corpus.wordsToString()
            result = giveMeSentiment(s)
            print result
            self.wfile.write( result )
        elif dic['which'] == 'google':
            g = pygoogle( dic['query'] )
            urls = g.get_urls()
            self.wfile.write( urls )

HTTPServer( ("", 3000), Handler).serve_forever()

# corpus = URLtoCorpus()
# query = 'justin bieber' 
# links = bing_search(query,'Web')
# corpus.numToRead = len(links)
# corpus.openURLsfromlist(links)
# s = corpus.wordsToString()
# result = giveMeSentiment(s)

# from pygoogle import pygoogle
# g = pygoogle('justin bieber')
# print g.get_urls()


#styling to use all data from tweet: ie show favorites and retweets
