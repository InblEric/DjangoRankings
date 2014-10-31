from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup


def index(request):
    
    
    template = loader.get_template('rank/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
    
    
    


    
