from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from config import get_config
from urls import urlpatterns
from response import http_response

class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        function = urlpatterns.get(self.path)
        if function:
            function.__call__(self)
        else:
            http_response(self, "URL NOT FOUND", code=404)

def serve_httpd():
    PORT = get_config("server", "port", "int")
    HOST = get_config("server", "host")

    httpd = HTTPServer((HOST, PORT), HttpHandler)
    print "Serving in http://%s:%s" % (HOST, PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Receiving Terminate Signal"
    httpd.server_close()