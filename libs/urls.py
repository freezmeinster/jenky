from controllers import info
from controllers import console
from response import static_response

urlpatterns = [
    ("/$", info.index),
    ("^/version$", info.version),
    ("^/console/$", console.index),
    ("^/static/(?P<path>.*?)$", static_response)
]
