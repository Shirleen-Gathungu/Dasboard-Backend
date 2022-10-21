from operator import mod
from pickle import SHORT_BINSTRING
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Artist(models.Model):
    name= models.CharField(max_length=20)
    profile_picture=models.ImageField(default='default.jpg', upload_to='profile_pics')
    album = models.ForeignKey('Album',on_delete=models.CASCADE,related_name='artist_album')


class Album(models.Model):
    songs= models.ForeignKey('Song',on_delete=models.CASCADE,related_name='album_song')

class Song(models.Model):
    title= models.CharField(max_lenght=20)
    artist= models.CharField(max_lenght=20)
    duration= models.TimeField()
    album = models.ForeignKey('Album',on_delete=models.CASCADE,related_name='song_album')

class Playlist(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE,related_name='album_song')
    songs=models.ForeignKey('Songs',on_delete=models.CASCADE,related_name='album_song')
    album=models.ForeignKey(Album,on_delete=models.CASCADE,related_name='album_song')

class User(models.Model):
    name = models.CharField(max_length=20)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,related_name='user_playlist')
   