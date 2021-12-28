from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/',views.StudentListCreate.as_view()),
    path('studentdetail/<int:pk>',views.StudentRUD.as_view()),
    
    
]
