from django.db import models

class Marker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)
    commemorated_year = models.IntegerField()
    inscription = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

