from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=4)
    poster=models.CharField(max_length=100)


class MovieInfo(models.Model):
    m_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=300)


class Users(models.Model):
    u_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100, default="John")
    last_name = models.CharField(max_length=100, default="Doe")
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    age = models.IntegerField()
    age_group = models.CharField(max_length=6)
    occupation = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="USA")


class Ratings(models.Model):
    user = models.ForeignKey(Users)
    movie = models.ForeignKey(MovieInfo)
    rating = models.IntegerField(default=0)


class PredictionModel(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.FloatField()
