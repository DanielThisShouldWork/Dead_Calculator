# models.py
from django.db import models

class LifeExpectancy(models.Model):
    country = models.CharField(max_length=100)
    expectancy_years = models.FloatField()  # Anni di vita media

    def __str__(self):
        return f"{self.country} - {self.expectancy_years} anni"


