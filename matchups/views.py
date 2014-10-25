from django.shortcuts import render
from django.template import RequestContext, loader
import logging

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

# Create your views here.
def mindex(request):
    mlist = list(Matchup.objects.all())
    template = loader.get_template('matchups/matchups.html')
    context = RequestContext(request, {'mlist':mlist})
    return HttpResponse(template.render(context))
    
def get(request, id):
    names = []
    mList = list(Matchup.objects.all())
    matchup = None
    try:
        matchup = mList[int(id)-1]
        names.append(str(matchup.player1.first_name) + " " + str(matchup.player1.last_name))
        names.append(str(matchup.player2.first_name) + " " + str(matchup.player2.last_name))        
    except:
        pass#return HttpResponse("invalid matchup")    
    template = loader.get_template('matchups/specific.html')
    context = RequestContext(request, {'id':id, 'names':names, 'matchup':matchup, 'mlist':mList,})
    return HttpResponse(template.render(context))
    
def vote1(request, id):
    names = []
    mList = list(Matchup.objects.all())
    try:
        matchup = mList[int(id)-1]
    except:
        return HttpResponse("invalid matchup")    
    matchup.p1Votes = matchup.p1Votes + 1
    matchup.save()
    #newid = str(int(id)+1)
    uri = "/matchups/"+int(id)
    js = "window.location = '" + uri + "'"
    resp = HttpResponse()    
    resp.write("<body onload='myFunction()'>")
    resp.write("<script> function myFunction() {"+js+"}</script>")
    resp.write("thanks for voting, player 1 has " + str(matchup.p1Votes) +  " votes!")
    resp.write("</body>")
    return resp
    
def vote2(request, id):
    names = []
    mList = list(Matchup.objects.all())
    try:
        matchup = mList[int(id)-1]
    except:
        return HttpResponse("invalid matchup")    
    matchup.p2Votes = matchup.p2Votes + 1
    matchup.save()
    #newid = str(int(id)+1)
    uri = "/matchups/"+int(id)
    js = "window.location = '" + uri + "'"
    resp = HttpResponse()    
    resp.write("<body onload='myFunction()'>")
    resp.write("<script> function myFunction() {"+js+"}</script>")
    resp.write("thanks for voting, player 1 has " + str(matchup.p1Votes) +  " votes!")
    resp.write("</body>")
    return resp