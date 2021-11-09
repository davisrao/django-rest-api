from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    jersey_number = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} #{self.jersey_number}"

class Season(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.IntegerField()
    ppg = models.DecimalField(max_digits=3, decimal_places=1)
    rpg = models.DecimalField(max_digits=3, decimal_places=1)
    apg = models.DecimalField(max_digits=3, decimal_places=1)
    spg = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.player} in {self.year}"

