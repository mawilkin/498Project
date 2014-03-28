from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):
        # handle a request by reading in the string then returning the reverse of it     
        s = self.rfile.read( int(self.headers.getheader('content-length')) )
        self.wfile.write( s[::-1] )

HTTPServer( ("", 3000), Handler).serve_forever()