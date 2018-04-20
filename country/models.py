from django.db import models

# Create your models here.
class CountryModel(models.Model):
    name = models.CharField(max_length=200)
    population = models.PositiveSmallIntegerField()
    president = models.CharField(max_length=200)
    continent = models.ForeignKey('continents.ContinentModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name