from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PrimaryMeal(models.Model):

    name = models.CharField(max_length=100)
    kitchen = models.CharField(max_length=100)
    body = models.TextField()
    mark = models.CharField(max_length=6)
    price = models.FloatField()
    image = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self) -> str:
        return self.name

class GeneralMeal(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.FloatField()
    types = models.CharField(max_length=100)
    body = models.TextField()
    srok = models.DateTimeField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name

class Wine(models.Model):
    TYPES = (
        ('1', '1'),
        ('2', '2')
    )

    name = models.CharField(max_length=100)
    types = models.CharField(max_length=30, choices=TYPES, default=TYPES[0][0])
    image = models.CharField(max_length=255)
    body = models.TextField()
    types_sugar = models.CharField(max_length=100)
    types_color = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


