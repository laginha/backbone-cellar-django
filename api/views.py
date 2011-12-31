# Create your views here.

from django.http import HttpResponse
from api.utils   import Resource, method
from api.models  import Wine
import ast

def query_to_dict( x ):
    x = str( x.items()[0][0] )
    x = x.replace( 'null', 'None' ) 
    return ast.literal_eval( x )

class WinesResource(Resource):

    @method
    def GET(request):
        return Wine.objects.all()

    @method
    def POST(request, *args, **kwargs):
        fields = query_to_dict( request.POST )
        wine   = Wine( **fields )
        wine.save()
        return wine
        

class WineResource(Resource):

    @method
    def GET(request, wine_id):
        return Wine.objects.get( id=int(wine_id) )
    
