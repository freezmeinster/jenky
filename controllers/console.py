from libs.response import http_response, json_response, template_response, static_response

def index(request):
    template_response(request, "console.html")