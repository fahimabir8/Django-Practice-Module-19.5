from django.db import models
from Musician.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=30,unique=True)
    album_release_date = models.DateTimeField(auto_now_add=True)
    musician = models.ForeignKey(Musician,default=None, on_delete=models.CASCADE)
    movie_rating = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    ]
    rating = models.CharField(choices=movie_rating, default=1, max_length=1)
    
    def __str__(self):
        return self.album_name