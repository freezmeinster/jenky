import re
import cgi
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

from config import get_config
from urls import urlpatterns
from response import http_response

class ThreadedHTTPServer(HTTPServer):
    def process_request(self, request, client_address):
        thread = Thread(target=self.__new_request, args=(self.RequestHandlerClass, request, client_address, self))
        thread.start()
    def __new_request(self, handlerClass, request, address, server):
        handlerClass(request, address, server)
        self.shutdown_request(request)

class HttpHandler(BaseHTTPRequestHandler):
    
    POST = None
    FILES = dict()
    method = "GET"
    
    def do_GET(self):
        url_prog = []

        for item in urlpatterns:
            prog = re.compile(item[0])
            url_prog.append((prog, item[1]))
        
        match = None
        for item in url_prog:
            res = item[0].match(self.path)
            if res:
                match = (res, item[1])
        if match:
            match[1].__call__(self, **match[0].groupdict())
        else:
            http_response(self, "url not found", code=404)
            
    def do_POST(self):
        self.method = "POST"
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        post_data = dict()
        for field in form.keys():
            item = form[field]
            if item.filename:
                self.FILES[fields] = item.file.read()
            else:
                post_data[field] = item.value
        self.POST = post_data
        url_prog = []

        for item in urlpatterns:
            prog = re.compile(item[0])
            url_prog.append((prog, item[1]))
        
        match = None
        for item in url_prog:
            res = item[0].match(self.path)
            if res:
                match = (res, item[1])
        if match:
            match[1].__call__(self, **match[0].groupdict())
        else:
            http_response(self, "url not found", code=404)

def serve_httpd():
    PORT = get_config("server", "port", "int")
    HOST = get_config("server", "host")

    httpd = ThreadedHTTPServer((HOST, PORT), HttpHandler)
    print "Serving in http://%s:%s" % (HOST, PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Receiving Terminate Signal"
    httpd.server_close()