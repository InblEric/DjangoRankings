from django.shortcuts import render
from django.template import RequestContext, loader
import logging
from math import exp
import random

# Create your views here.

from django.http import HttpResponse
from rank.models import Player,Matchup

# Create your views here.
def mindex(request):
    count = Matchup.objects.count()
    template = loader.get_template('matchups/matchups.html')
    context = RequestContext(request, {'count':count})
    return HttpResponse(template.render(context))
    
def get(request, id):
    names = []
    count = Matchup.objects.count()
    #mList = list(Matchup.objects.order_by('created_at'))
    matchup = None
    try:
        #matchup = mList[int(id)-1]
        matchup = Matchup.objects.get(num=id)
        names.append(str(matchup.player1.first_name) + " " + str(matchup.player1.last_name))
        names.append(str(matchup.player2.first_name) + " " + str(matchup.player2.last_name))        
    except:
        pass#return HttpResponse("invalid matchup")    
    template = loader.get_template('matchups/specific.html')
    context = RequestContext(request, {'id':id, 'names':names, 'matchup':matchup, 'count':count, })
    return HttpResponse(template.render(context))
    
def vote1(request, id):
    names = []
    #mList = list(Matchup.objects.order_by('created_at'))
    try:
        #matchup = mList[int(id)-1]
        matchup = Matchup.objects.get(num=id)
    except:
        return HttpResponse("invalid matchup")    
    matchup.p1Votes = matchup.p1Votes + 1
    
    p1 = matchup.player1
    p2 = matchup.player2    
    sep1 = 1 / (exp((p2.elo - p1.elo)/(p1.elo)) + 1)
    sep2 = 1 / (exp((p1.elo - p2.elo)/(p1.elo)) + 1)    
    p1.elo = p1.elo + (k(p1.elo) *(1-sep1))
    p2.elo = p2.elo + (k(p2.elo) *(0-sep2))        
    p1.save()
    p2.save()    

    ################
    #UPDATE ELO HERE
    #PLAYER 1 WINS
    #PLAYER 2 LOSES
    #...
    #p1.save()
    #p2.save()
    ################
    
    matchup.save()
    #CHANGE THIS TO A RANDOM NUMBER
    r = random.randint(1,Matchup.objects.count())
    newid = str(r)
    uri = "/matchups/"+newid
    js = "window.location = '" + uri + "'"
    resp = HttpResponse()    
    resp.write("<body onload='myFunction()'>")
    resp.write("<script> function myFunction() {"+js+"}</script>")
    resp.write("")
    resp.write("</body>")
    return resp
    
def vote2(request, id):
    names = []
    #mList = list(Matchup.objects.order_by('created_at'))
    try:
        #matchup = mList[int(id)-1]
        matchup = Matchup.objects.get(num=id)
    except:
        return HttpResponse("invalid matchup")    
    matchup.p2Votes = matchup.p2Votes + 1
    
    p1 = matchup.player1
    p2 = matchup.player2
    sep1 = 1 / (exp((p2.elo - p1.elo)/(p1.elo)) + 1)
    sep2 = 1 / (exp((p1.elo - p2.elo)/(p1.elo)) + 1)    
    p1.elo = p1.elo + (k(p1.elo) *(0-sep1))
    p2.elo = p2.elo + (k(p2.elo) *(1-sep2))  
    p1.save()
    p2.save()
        
    ################
    #UPDATE ELO HERE
    #PLAYER 1 WINS
    #PLAYER 2 LOSES
    #p1.save()
    #p2.save()    
    ################
    
    matchup.save()
    #CHANGE THIS TO A RANDOM NUMBER
    r = random.randint(1,Matchup.objects.count())
    newid = str(r)
    uri = "/matchups/"+newid
    js = "window.location = '" + uri + "'"
    resp = HttpResponse()    
    resp.write("<body onload='myFunction()'>")
    resp.write("<script> function myFunction() {"+js+"}</script>")
    resp.write("")
    resp.write("</body>")
    return resp
    
def k(elo):
    ans = 116 - (0.04076923076923 * (elo-100))
    return ans