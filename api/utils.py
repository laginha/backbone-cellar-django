#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
import simplejson

method = staticmethod


def JsonResponse(req, data):
    #JSONP builder
    json_str = lambda x: simplejson.dumps( x, indent=2 )
    response = HttpResponse( json_str( data ), content_type='application/json' )
    if response.status_code == 200:
        for key in ['callback', 'jsonp']:
            if key in req.GET:
                response['Content-Type'] = 'text/javascript; charset=utf-8'
                response.content = "%s(%s)" %( req.GET[key], response.content )
                return response
    return response



class Resource(object):
    snippet_url = "http://djangosnippets.org/snippets/1071/"

    def __call__(self, request, *args, **kwargs):
        try:
            view     = getattr(self, request.method.upper())
            resource = view(request, *args, **kwargs)
            if resource:
                return JsonResponse( request, [i for i in resource.values()] )
            return JsonResponse( request, {'ok': 'true'} )
        except AttributeError:
            return HttpResponse( status = 405 )

