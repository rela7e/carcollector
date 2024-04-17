from django.db import models
from django.urls import reverse
# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    colour = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f'{self.make} {self.model} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    
class Accolade(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
    