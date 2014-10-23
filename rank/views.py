from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

def index(request):
    plist = []
    for i in Player.objects.all():
        pass
        plist.append(str(i.__unicode__()))
    
    return HttpResponse("Hello, world. You're at the rankings index." + " Players: " +str(plist) )