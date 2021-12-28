from django.contrib import admin
from .models import Singer,Song

# Register your models here.
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender']

class SongAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']


admin.site.register(Singer,SingerAdmin)
admin.site.register(Song,SongAdmin)
admin.site.site_header = "Dhruvil Administration"
admin.site.site_title = "Dhruvil|site administration"
admin.site.index_title = "Welcome to Dhruvil Administration"