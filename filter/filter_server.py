import result_filter
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler

host = "http://192.168.31.143:8983"

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
        # self.wfile.write("Hello World!")
        # print "type(self.headers):", type(self.headers)
        # print "self.path =", self.path
        # if self.path.find("select") > 0:
        json_data = result_filter.get_json(host + self.path)
        self.wfile.write(json_data)

addr = ("", 8000)
server = HTTPServer(addr,RequestHandler)
server.serve_forever()