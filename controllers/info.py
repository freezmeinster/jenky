from libs.response import http_response, json_response, template_response

def index(request):
    http_response(request, "test")
    
def ayam(request):
    template_response(request, "ayam.html")
    
def version(request):
    json_response(request, {"version" : 1})