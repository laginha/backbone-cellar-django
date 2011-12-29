from django.conf.urls.defaults import *
from dagny.urls import resources, resource, rails, atompub
from django.conf.urls.defaults import *

#from piston.resource import Resource
#from wine_cellar.api.handlers import WineHandler

#wine_handler = Resource(WineHandler)

urlpatterns = patterns('wine_cellar',
    url(r'^wines$', resources('api.resources.Wine', name='Wine')),
    url(r'^wines/$', resources('api.resources.Wine', name='Wine')),
    url(r'^wines/(?P<wine_id>[0-9]+)$', resources('api.resources.Wine', name='Wine')),
    #(r'^users/', resources('users.resources.User', name='User')),
)

#urlpatterns = patterns('',
#   url(r'^wine/(?P<id>[0-9]+)$', wine_handler, { 'emitter_format': 'json' }),
#   url(r'^wines$', wine_handler, { 'emitter_format': 'json' }),
#)

