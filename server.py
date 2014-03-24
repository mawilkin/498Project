#TEAM #SENTIMENT
#
import urllib
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class ServerHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
    	# converts html query to string
    	query = urllib.unquote_plus(self.path[18:]) 
    	print query
        SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler
httpd = BaseHTTPServer.HTTPServer(('127.0.0.1',8000), Handler)
print "serving at port 8000"
httpd.serve_forever()