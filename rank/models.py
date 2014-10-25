from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __unicode__(self):
        return self.first_name + " " + self.last_name + ", " + self.position

class Matchup(models.Model):
    created_at = models.DateTimeField()
    player1 = models.ForeignKey(Player, related_name='player_1')
    player2 = models.ForeignKey(Player, related_name='player_2')
    position = models.CharField(max_length=100) #QB/RB/WR/TE/FLEX/DST/K
    p1Votes = models.IntegerField()
    p2Votes = models.IntegerField()
    week = models.IntegerField()    
    
    def matchupLeader(self):
        if(self.p1Votes > self.p2Votes):
            return "in week " + str(self.week) + ", " + self.player1.__unicode__() + " wins by " + str(self.p1Votes-self.p2Votes) + " votes against " + self.player2.__unicode__()
        elif(self.p2Votes > self.p1Votes):
            return "in week " + str(self.week) + ", " + self.player2.__unicode__() + " wins by " + str(self.p2Votes-self.p1Votes) + " votes against " + self.player1.__unicode__()
        else:
            return "in week " + str(self.week)+ ", " + "Tie between " + self.player1.__unicode__() + " and " + self.player2.__unicode__()
    
    def __unicode__(self):
        player1name = self.player1.__unicode__()
        player2name = self.player2.__unicode__()        
        return player1name + " vs " + player2name