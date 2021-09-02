from django.db import models

# Create your models here.

class Travello(models.Model):
	
	name = models.CharField(max_length=100)
	price = models.IntegerField()
	desc = models.TextField()
	img = models.ImageField()
	offer = models.BooleanField(default=False)