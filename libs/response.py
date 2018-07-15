import json
import os

from config import BASE_DIR

def return_response(request,msg, type="html", code=200):
    request.send_response(code)
    if type == "json":
        header = "application/json"
    else:
        header = "text/html"
    request.send_header("Content-type", header)
    request.end_headers()
    request.wfile.write(msg)
    
def http_response(request, msg, code=200):
    return_response(request, msg, code=code)
    
def json_response(request, msg, code=200):
    return_response(request, json.dumps(msg), "json", code=code)
    
def template_response(request, template, payload={}, code=200):
    template_path = os.path.join(BASE_DIR, "templates/%s" % template)
    return_response(request, open(template_path).read(), code=code)
    
def static_response(request, path):
    static_path  = os.path.join(BASE_DIR, "static")
    path = os.path.join(static_path, path)
    if os.path.isfile(path):
        with open(path, 'rb') as content_file:
            request.send_response(200)
            # request.send_header('Content-type', 'application/javascript')
            request.end_headers()
            request.wfile.write(content_file.read())   
    else:
        http_response(request, "file not found", code=400)
        