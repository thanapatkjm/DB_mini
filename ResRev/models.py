from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Reviewer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    like = models.IntegerField(default=0)
    clas = models.TextField()
    description = models.TextField()
    contact = models.CharField(max_length=80)
    hours = models.IntegerField(default=0)

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=80)
    description = models.TextField()
    category = models.TextField()
    rating = models.FloatField(default=0)
    g_rating = models.FloatField(default=0)
    # photo

class Review(models.Model):
    restau = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer,on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],)
    like = models.IntegerField(default=0)
