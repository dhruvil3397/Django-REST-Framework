from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/',views.Studentdetails.as_view()),
    path('studentlist/',views.studentlist),
    
]
