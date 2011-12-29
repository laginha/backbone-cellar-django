from django.conf.urls.defaults import *

urlpatterns = patterns('wine_cellar.homepage.views',
    url(r'^$', 'home', name='home'),
)

