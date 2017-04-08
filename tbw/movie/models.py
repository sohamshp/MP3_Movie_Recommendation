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
    imdb = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.m_id) + " - " + str(self.name) + " (" + str(self.year) + ") <br>" + str(self.genre) + "<br><br>"


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


class Unrated(models.Model):
    user_id = models.IntegerField()
    movie_id = models.IntegerField()


class Ratings2(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.FloatField(default=0)


class UMMat(models.Model):
    userId = models.IntegerField()
    movieId = models.IntegerField()
    rating = models.IntegerField()


class JobAvg(models.Model):
    jobId = models.IntegerField()
    job = models.CharField(max_length=100)
    movieId = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()
    count3 = models.IntegerField()
    count4 = models.IntegerField()
    count5 = models.IntegerField()
    avgRating = models.FloatField()


class AgeAvg(models.Model):
    ageIndex = models.IntegerField()
    ageVal = models.IntegerField()
    ageRange = models.CharField(max_length=10)
    movieId = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()
    count3 = models.IntegerField()
    count4 = models.IntegerField()
    count5 = models.IntegerField()
    avgRating = models.FloatField()


class GenderAvg(models.Model):
    genderIndex = models.IntegerField()
    gender = models.CharField(max_length=1)
    movieId = models.IntegerField()
    count1 = models.IntegerField()
    count2 = models.IntegerField()
    count3 = models.IntegerField()
    count4 = models.IntegerField()
    count5 = models.IntegerField()
    avgRating = models.FloatField()