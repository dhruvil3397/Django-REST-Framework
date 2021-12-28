from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

# Create router object
router = DefaultRouter()
router1 = DefaultRouter()
# Register router with StudentModelViewSet

router.register('StudentAPI',views.StudentModelViewSet,basename='student')
router1.register('StudentAPI',views.StudentReadOnlyModelViewSet,basename='student')

# Here we don't need to mentioned :- path('studentdetail/<int:pk>',views.StudentRetrieveUpdateDelete.as_view())
    # url here ,because it automatically handle pk value.

urlpatterns = [
    path('router/',include(router.urls)),
    #path('router1/',include(router1.urls)),
]
