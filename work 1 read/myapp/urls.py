from django.urls import path
from .import views

urlpatterns = [
    path('studentdetail/<int:pk>',views.student_details,name = "student_data"),
    path('studentlist/',views.student_list,name = "student_list"),
]
