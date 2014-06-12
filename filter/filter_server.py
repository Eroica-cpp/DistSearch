from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def _writeheaders(self):
        # print self.path
        # print self.headers
        self.send_response(200);
        self.send_header('Content-type','text/html');
        self.end_headers()
    
    def do_Head(self):
        self._writeheaders()
    
    def do_GET(self):
        self._writeheaders()
        self.wfile.write("Hello World!")
        print "in do_GET!"
        print "type(self.headers):", type(self.headers)
        print "self.path =", self.path

addr = ('', 8000)
server = HTTPServer(addr,RequestHandler)
server.serve_forever()