from django.db import models


class Musician(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.CharField(max_length=11)
    instrument_type=models.CharField()

    def __str__(self):
        return f"{self.first_name}"







