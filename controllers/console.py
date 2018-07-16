from libs.response import http_response, json_response, template_response, static_response

def index(request):
    template_response(request, "console.html")
    
def component(request, path):
    static_response(request, path, base_dir="templates/component")