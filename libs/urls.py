from controllers import info

urlpatterns = {
    "/" : info.index,
    "/version" : info.version,
    "/ayam": info.ayam
}