from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

# Create your views here.
def pindex(request):

    qbs = []
    rbs = []
    wrs = []
    tes = []
    flex = []
    for i in Player.objects.all().order_by('-elo'):
        if(str(i.position) == "QB"):
            qbs.append(i)
        if(str(i.position) == "RB"):
            rbs.append(i)
            flex.append(i)
        if(str(i.position) == "WR"):
            wrs.append(i)
            flex.append(i)
        if(str(i.position) == "TE"):
            tes.append(i)
            flex.append(i)
    template = loader.get_template('players/players.html')
    context = RequestContext(request, {
        'qbs': qbs, 'rbs': rbs, 'wrs': wrs, 'tes': tes,  'flex': flex,
    })
    return HttpResponse(template.render(context))
    