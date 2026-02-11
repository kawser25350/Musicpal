from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name=models.CharField(max_length=200)
    album_release_date=models.DateTimeField()
    r_choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating=models.IntegerField(choices=r_choices)
    author=models.ForeignKey(Musician,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.album_name}"