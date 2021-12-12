from django.db import models


class Pizza(models.Model):
    names = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
        
    def __str__(self):
        return self.names


class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    


    def __str__(self):
        return self.name #self.pizza


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete= models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:150]}..."

class Image(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

# Create your models here.
