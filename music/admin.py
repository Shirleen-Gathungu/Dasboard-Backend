from django.contrib import admin
from .models import User
from .models import Playlist
from .models import Song
from .models import Album
from .models import Song
from .models import Artist
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('name','profile_picture','playlist',)
    search_fields = ('name','profile_picture','playlist',)
admin.site.register(User,UserAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('user','songs','album',)
    search_fields = ('user','songs','album',)
admin.site.register(Playlist,PlaylistAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ('title','artist','duration','album',)
    search_fields = ('title','artist','duration','album',)
admin.site.register(Song,SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','profile_picture','album',)
    search_fields = ('name','profile_picture','album',)
admin.site.register(Artist,ArtistAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('song',)
    search_fields = ('song',)
admin.site.register(Album,AlbumAdmin)
