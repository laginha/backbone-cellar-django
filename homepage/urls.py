from django.conf.urls.defaults import *

urlpatterns = patterns('homepage.views',
    url(r'^$', 'home', name='home'),
)
