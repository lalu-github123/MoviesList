from django.db import models

# Create your models here.
class Movielist(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    desc = models.CharField(max_length=250)
    img  = models.ImageField()

    def __str__(self):
        return self.name