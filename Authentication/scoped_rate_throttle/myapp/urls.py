from django.urls import path
from .import views

urlpatterns = [
    #path('studentdetail/',views.StudentList.as_view()),
    path('studentdetail/',views.StudentCreate.as_view()),
    #path('studentdetail/<int:pk>',views.StudentUpdate.as_view()),
    #path('studentdetail/<int:pk>',views.StudentRetrieve.as_view()),
    #path('studentdetail/<int:pk>',views.StudentDelete.as_view()), 
    
]
