from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/',views.studentdetails,name = "student_data"),
    path('studentlist/',views.studentlist),
    
]
