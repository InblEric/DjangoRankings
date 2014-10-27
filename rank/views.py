from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup


def index(request):
    """plist = []
    for i in Player.objects.all():
        plist.append(i)
    mlist = []
    for i in Matchup.objects.all(): #if i.week == CURWEEK do something for when this is real
        mlist.append(i)"""
    
    template = loader.get_template('rank/index.html')
    context = RequestContext(request, {
        ''''players': plist, 'matchups': mlist,'''
    })
    return HttpResponse(template.render(context))
    
    #return HttpResponse("Hello, world. You're at the rankings index." + " Players: " +str(plist) )
    


    
"""def QB(request):
    plist = []
    for i in Player.objects.all():
        pass
        if(i.position == "QB"):
            plist.append(str(i.__unicode__()))
    
    return HttpResponse("Hello, world. You're at the Quarterback index." + " Players: " +str(plist) )"""