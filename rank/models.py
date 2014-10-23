from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

class Matchup(models.Model):
    player1 = models.ForeignKey(Musician)
    player2 = models.ForeignKey(Musician)
    position = models.CharField(max_length=100) #QB/RB/WR/TE/FLEX/DST/K
    p1Votes = models.IntegerField()
    p2Votes = models.IntegerField()