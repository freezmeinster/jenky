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
    
def template_response(request, template, code=200):
    template_path = os.path.join(BASE_DIR, "templates/%s" % template)
    return_response(request, open(template_path).read(), code=code)