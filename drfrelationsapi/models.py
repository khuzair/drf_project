from platform import release
from pyexpat import model
from django.db import models

SINGING_STYLE = (
    ("HipHop", "hiphop"),
    ("FreeStyle", "free-style"),
    ("RockMusic", "Rock-Music"),
    ("Rap-Music", "rap"),
)


class Singer(models.Model):
    name = models.CharField(max_length=100)
    style = models.CharField(max_length=100, choices=SINGING_STYLE)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.DateField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')

    def __str__(self):
        return self.title
