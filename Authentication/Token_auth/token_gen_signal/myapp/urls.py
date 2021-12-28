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
    path('router/',include(router.urls)),
    
]

