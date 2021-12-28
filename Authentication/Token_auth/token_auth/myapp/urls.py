from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter




# Create router object
router = DefaultRouter()

# Register router with StudentModelViewSet

router.register('StudentAPI',views.StudentModelViewSet,basename='student')


# Here we don't need to mentioned :- path('studentdetail/<int:pk>',views.StudentRetrieveUpdateDelete.as_view())
    # url here ,because it automatically handle pk value.

urlpatterns = [
    path('router/',include(router.urls)), # For Browsable API
    
]

# For Normal GET Request without Authentication:-
    # Write below code in the terminal:
    #  http http://127.0.0.1:8000/myapp/router/StudentAPI/

# For GET Request with Authentication:-
    # Write below code in the terminal
    # http http://127.0.0.1:8000/myapp/router/StudentAPI/ 'Authorization:Token a33a7432820cba68b961c00f218c92cb575a420e'

# For POST Request with Authentication :-
    # Write below code in the terminal
    # http -f POST http://127.0.0.1:8000/myapp/router/StudentAPI/ name=Jay roll=55 city=Ahmedabad 'Authorization:Token a33a7432820cba68b961c00f218c92cb575a420e'


# For PUT Request with Authentication :-
    # Write below code in the terminal
    # http PUT http://127.0.0.1:8000/myapp/router/StudentAPI/4/ name=Jack roll=56 city=Toronto 'Authorization:Token a33a7432820cba68b961c00f218c92cb575a420e'

# For DELETE Request with Authentication :-
    # Write below code in the terminal
    # http DELETE http://127.0.0.1:8000/myapp/router/StudentAPI/4/ 'Authorization:Token a33a7432820cba68b961c00f218c92cb575a420e'

