from django.contrib import admin
from .models import User
from .models import Playlist
from .models import Song
from .models import Album
from .models import Song
from .models import Artist
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ('name','profile_picture',Playlist,)
    search_fields = ('name','profile_picture',Playlist,)
admin.site.register(User,UserAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('user',Song,Album,)
    search_fields = ('user',Song,Album,)
admin.site.register(Playlist,PlaylistAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ('title',Artist,'duration',)
    search_fields = ('title',Artist,'duration',)
admin.site.register(Song,SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','profile_picture',Album,)
    search_fields = ('name','profile_picture',Album,)
admin.site.register(Artist,ArtistAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = (Song,)
    search_fields = (Song,)
admin.site.register(Album,AlbumAdmin)
