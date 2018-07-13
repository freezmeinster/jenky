import os
import platform
from libs.response import http_response, json_response, template_response
from libs import config

def index(request):
    http_response(request, "welcome to jenky")
    
def ayam(request):
    template_response(request, "ayam.html")
    
def version(request):
    version = {
        "apps": open(os.path.join(config.BASE_DIR, "VERSION")).read(),
        "python": platform.python_version()
    }
    json_response(request, version)