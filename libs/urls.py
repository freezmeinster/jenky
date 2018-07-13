from controllers import info
from controllers import console

urlpatterns = {
    "/" : info.index,
    "/version" : info.version,
    "/console": info.index
}