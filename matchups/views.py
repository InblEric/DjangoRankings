from django.shortcuts import render
from django.template import RequestContext, loader
import logging

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

# Create your views here.
def mindex(request):
    template = loader.get_template('matchups/matchups.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
    
def get(request, id):
    names = ["none","none"]
    mList = list(Matchup.objects.all())
    try:
        matchup = mList[int(id)-1]
    except:
        return HttpResponse("invalid matchup")    
    names[0] = (str(matchup.player1.first_name) + " " + str(matchup.player1.last_name))
    names[1] = (str(matchup.player2.first_name) + " " + str(matchup.player2.last_name))        
    template = loader.get_template('matchups/specific.html')
    context = RequestContext(request, {'id':id, 'names':names,})
    return HttpResponse(template.render(context))