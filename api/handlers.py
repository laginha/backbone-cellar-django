from piston.handler import BaseHandler
from api.models import Wine

class WineHandler(BaseHandler):
    allowed_methods = ('GET', 'PUT', 'DELETE', 'POST')
    model = Wine
    exclude = ()

    def read(self, request, **kwargs):
        wine = Wine.objects
        
        if kwargs:
            return wine.get(**kwargs)
        else:
            return wine.all()

    def create(self, request, *args, **kwargs):
        print "creating..."
        print args
        print kwargs
        print request
        
        wine = Wine(**kwargs)
        wine.save()     
        return wine
        
    def update(self, request, *args, **kwargs):
        print "updating... "
        # post.title = request.PUT.get('title')
        # post.save()
        print request.PUT
        wine = Wine.objects.get(id=kwargs.pop('id')).update(**kwargs)
        wine.save()
        return wine
        
    def delete(self, request, *args, **kwargs):
        print "deleting..."
        wine = Wine.objects.get(**kwargs)
        wine.delete()
        return rc.DELETED # returns HTTP 204