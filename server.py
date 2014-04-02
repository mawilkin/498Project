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
        dic = json.loads(s)
        returnDic = findstuffaboutquery( dic['query'] )
        s = returnDic["focus"]
        emotion = returnDic["emotion"]
        if dic['which'] == 'feelings':
            lst = list()
            lst.append(dic['query'])
            querySentiment = tweetsentiments( lst )
            queryEmotion = querySentiment.findMax()
            returnStr = 'It seems you feel ' + emotion + ' about ' + s
            self.wfile.write( returnStr )
        elif dic['which'] == 'twitter':
            lst = list()
            lst.append(s)
            tweets = twit.top50Tweets( lst )
            tweetSentiment = tweetsentiments( tweets )
            tweetEmotion = tweetSentiment.findMax()
            print tweetEmotion
            tweetEmotion = 'Twitter feels ' + str(tweetEmotion) + ' about ' + s
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
