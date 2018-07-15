import os
import platform
from libs.response import http_response, json_response, template_response
from libs import config

def index(request):
    http_response(request, "it's work")
    
def ayam(request):
    template_response(request, "ayam.html")

def crud(request):
    if request.method == "POST":
        print request.POST["username"]
    template_response(request, "crud.html", {"ayam": "ayam"})

def version(request):
    version = {
        "apps": open(os.path.join(config.BASE_DIR, "VERSION")).read(),
        "python": platform.python_version()
    }
    json_response(request, version)