from django.conf.urls.defaults import *
from api.views                 import WinesResource, WineResource

urlpatterns = patterns('',
    url(r'^wines$',                     WinesResource(), ),
    url(r'^wines/(?P<wine_id>[0-9]+)$', WineResource(),  ),
)


