# -*- coding: utf-8 -*-
from api import models
from dagny import Resource, action
from dagny.renderer import Skip
#from django.contrib.auth import forms, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.core import serializers

import simplejson
import ast


class Wine(Resource):

    @action
    def index(self):
        print "indexing... "
        self.wines = models.Wine.objects.all()
        x = [wine_to_dict(wine) for wine in self.wines]
        return json_response(self.request, x)

    @index.render.json
    def index(self):
        print "indexing...2"
        return json_response([wine_to_dict(wine) for wine in self.wines])

    #@action
    #def new(self):
    #    self.form = forms.WineCreationForm()

    @action
    def create(self):
        print "creating..."
        string      = str(self.request.POST.keys()[0])
        string      = string.replace( 'null', 'None' )
        wine_fields = ast.literal_eval( string )
        
        wine = models.Wine(**wine_fields)
        wine.save()
        print wine.values()
        return json_response(self.request, [wine.values()])
        

    @action
    def show(self, wine_id):
        print "showing..."
        self.wine = get_object_or_404(models.Wine, id=int(wine_id))
        return json_response(self.request, [self.wine.values()])

    @action
    def update(self, wine_id):
        print "updating..."
        print wine_id
        self.wine = get_object_or_404(models.Wine, id=int(wine_id))
        
        self.wine.update(self.request.POST)
        self.wine.save()
        return self.wine

    @action
    def destroy(self, wine_id):
        print "destroying..."
        self.wine = get_object_or_404(models.Wine, id=int(wine_id))
        self.wine.delete()
        return HttpResponse(status = 200)

def json_response(req, data):
    """
    - JSONP builder
    """
    def json_string():
        return simplejson.dumps( data, indent=2 )

    def _response_(key):
        response['Content-Type'] = 'text/javascript; charset=utf-8'
        response.content = "%s(%s)" %( req.GET[key], response.content )
        return response 

    response = HttpResponse( json_string(), content_type='application/json' )
    if response.status_code == 200:
        for key in ['callback', 'jsonp']:
            if key in req.GET:
                return _response_( key )
    return response

#def json_response(data):
#    return HttpResponse(content=simplejson.dumps(data),
#                        content_type='application/json')

def wine_to_dict(wine):
    return wine.values()
#    data = serializers.serialize("json", wine)
#    return data