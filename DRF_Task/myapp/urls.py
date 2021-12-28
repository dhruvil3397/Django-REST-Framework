from django.urls import path
from .import views

urlpatterns = [
    path('userdetail/',views.userdetails),
    path('userdetail/<int:pk>',views.userdetails),   
    path('login/',views.login),
    path('edit/',views.edit),
    path('otpverify/<str:email>', views.otpverify),
    path('changepass/',views.changepassword),
    path('resetpass/',views.resetpassword),
    path('forgotpass/',views.forgotpassword),
    path('verifyforgotpass/',views.verifyforgotpass),
    path('adminRUD/',views.adminRUD),
]
