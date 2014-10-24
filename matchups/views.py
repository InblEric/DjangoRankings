from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

# Create your views here.
def mindex(request):
    template = loader.get_template('matchups/matchups.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))