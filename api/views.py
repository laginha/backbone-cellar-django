# Create your views here.

from django.http import HttpResponse
from api.utils   import Resource, method
from api.models  import Wine

class WinesResource(Resource):

    @method
    def GET(request):
        return Wine.objects.all()

class WineResource(Resource):

    @method
    def GET(request, wine_id):
        return Wine.objects.get( id=int(wine_id) )

