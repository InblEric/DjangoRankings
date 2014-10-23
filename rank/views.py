from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

def index(request):
    player = Player.objects.get(pk=1)
    
    return HttpResponse("Hello, world. You're at the rankings index." + " Players: " +str(player) )