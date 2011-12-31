# Create your views here.

from django.http import HttpResponse
from api.utils   import Resource, method
from api.models  import Wine
import ast

str_to_dict   = lambda x: ast.literal_eval( x.replace( 'null', 'None' )  )
query_to_dict = lambda x: str_to_dict( str( x.items()[0][0] ) )
    

class WinesResource(Resource):

    @method
    def GET(request):
        return Wine.objects.all()

    @method
    def POST(request):
        fields = query_to_dict( request.POST )
        wine   = Wine( **fields )
        wine.save()
        return wine
        
        

class WineResource(Resource):

    @method
    def GET(request, wine_id):
        return Wine.objects.get( id = int( wine_id ) )
    
    @method
    def PUT(request, wine_id):
        fields = str_to_dict( request.raw_post_data )
        wine   = Wine( **fields )
        wine.save()
        
    @method
    def DELETE(request, wine_id):
        wine = Wine.objects.get( id = int( wine_id ) )
        wine.delete()

"""
Q: Why am i not using django's generic class based views?
R: I don't like the idea of having state on a view. Maybe i'm just being stuborn.

ex:

urlpatterns = patterns('',
    url( r'^someresource$', SomeResource.as_view() ),
)

from django.views.generic.base import View

class SomeResource( View ):
    #http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options', 'trace']

    def get(self, request):
        return HttpResponse( status=200 )
  
    def post(self, request):
        return HttpResponse( status=200 )
"""

      
        