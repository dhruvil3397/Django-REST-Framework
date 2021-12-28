from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/',views.studentdetail),
    path('studentdetail/<int:pk>',views.studentdetail),

    
]
