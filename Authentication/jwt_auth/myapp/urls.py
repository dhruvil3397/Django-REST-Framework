from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# Create router object
router = DefaultRouter()

# Register router with StudentModelViewSet

router.register('StudentAPI',views.StudentModelViewSet,basename='student')


# Here we don't need to mentioned :- path('studentdetail/<int:pk>',views.StudentRetrieveUpdateDelete.as_view())
    # url here ,because it automatically handle pk value.

urlpatterns = [
    path('router/',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(), name= 'token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(), name= 'token_verify'),
   
]

# By default - access token validity = 5 minutes and refresh token validy = 1 day
# Get Token:-
    # Write below line in terminal for getting jwt Token : 1.access token 2.refresh token
    # http POST http://127.0.0.1:8000/myapp/gettoken/ username="Dhruvil" password="admin123"


# Verify Token:-
    # Write below line in terminal to verify access token
    # http POST http://127.0.0.1:8000/myapp/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MjM1NjczLCJpYXQiOjE2MzcyMzUzNzMsImp0aSI6IjAyNWRkZjU5Njc1ZDQ3OGE5OWM4YmQ2Mjc3NDczMzExIiwidXNlcl9pZCI6MX0.zFMAarbjLSyoeZo5697oj7tBYCG9RP9_3gtQRYVdagI"

# Refresh Token:-
    # Write below line in terminal to refresh access token
    # http POST http://127.0.0.1:8000/myapp/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzMyMTc3MywiaWF0IjoxNjM3MjM1MzczLCJqdGkiOiJkYTAxMDMwNGNmY2M0OTBhYjI0ZWNjMjU4ZTZlNTFmMSIsInVzZXJfaWQiOjF9.eRwNEEy0znfNK3JrhYzy1ABVmFUhAoSwfQF2vut3qHU"


#------------------------------------------------------------------------------------------
# For Normal GET Request without Authentication:-
    # Write below code in the terminal:
    #  http http://127.0.0.1:8000/myapp/router/StudentAPI/

# For GET Request with Authentication:-
    # Write below code in the terminal
    # http http://127.0.0.1:8000/myapp/router/StudentAPI/ 'Authorization:Bearer a33a7432820cba68b961c00f218c92cb575a420e'

# For POST Request with Authentication :-
    # Write below code in the terminal
    # http -f POST http://127.0.0.1:8000/myapp/router/StudentAPI/ name=Jay roll=12 city=Texas 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MjM5MDU0LCJpYXQiOjE2MzcyMzUzNzMsImp0aSI6ImYyMDU5ZDFhZDVlMTQwMDRhZGEwNTk0NGU3ZTJhMzZkIiwidXNlcl9pZCI6MX0.iTGavqbl0jb9zwjo4ydeTWTatXiLpIEXXP3A5ng1ttU'


# For PUT Request with Authentication :-
    # Write below code in the terminal
    # http PUT http://127.0.0.1:8000/myapp/router/StudentAPI/3/ name=Jack roll=21 city=Texas 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MjM5MDU0LCJpYXQiOjE2MzcyMzUzNzMsImp0aSI6ImYyMDU5ZDFhZDVlMTQwMDRhZGEwNTk0NGU3ZTJhMzZkIiwidXNlcl9pZCI6MX0.iTGavqbl0jb9zwjo4ydeTWTatXiLpIEXXP3A5ng1ttU'

# For DELETE Request with Authentication :-
    # Write below code in the terminal
    # http DELETE http://127.0.0.1:8000/myapp/router/StudentAPI/4/ 'Authorization:Bearer a33a7432820cba68b961c00f218c92cb575a420e'

  