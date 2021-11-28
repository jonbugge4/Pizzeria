from django.db import models


class Pizza(models.Model):
    names = models.CharField(max_length=20)
    
    def __str__(self):
        return self.names


class Toppings(models.Model):
    types = models.CharField(max_length=20)

    def __str__(self):
        return self.types

# Create your models here.
