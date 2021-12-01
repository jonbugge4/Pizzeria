from django.db import models


class Pizza(models.Model):
    names = models.CharField(max_length=20)
    
    def __str__(self):
        return self.names


class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name, #self.pizza

# Create your models here.
