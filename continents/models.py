from django.db import models

# Create your models here.
class ContinentModel(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=15)

    def __str__(self):
        return self.name