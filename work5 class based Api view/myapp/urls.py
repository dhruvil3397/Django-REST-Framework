from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/',views.studentdetail.as_view()),
    path('studentdetail/<int:pk>',views.studentdetail.as_view()),
    
]
