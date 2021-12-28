from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']


admin.site.register(Student,StudentAdmin)
admin.site.site_header = "Dhruvil Administration"
admin.site.site_title = "Dhruvil|site administration"
admin.site.index_title = "Welcome to Dhruvil Administration"