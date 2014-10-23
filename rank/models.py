from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

class Matchup(models.Model):
    player1 = models.ForeignKey(Player, related_name='player_1')
    player2 = models.ForeignKey(Player, related_name='player_2')
    position = models.CharField(max_length=100) #QB/RB/WR/TE/FLEX/DST/K
    p1Votes = models.IntegerField()
    p2Votes = models.IntegerField()