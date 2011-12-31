# Create your views here.

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    # it searches within the templates folder automatically
    return template(request, 'index.html')
	
def template(request, templ, data={}):
    return render_to_response(templ,data, context_instance=RequestContext(request))