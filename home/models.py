from django.db import models

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    album_cover = models.ImageField(upload_to='pics', default="")
    fav = models.BooleanField(default=False)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    song_cover = models.ImageField(upload_to='pics', default="")
    song_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=10)
    fav = models.BooleanField(default=False)
    song_file = models.FileField(upload_to='music', default="")

    def __str__(self):
        return self.song_name + '.' + str(self.file_type)
