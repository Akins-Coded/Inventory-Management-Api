from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserViewSet
router = DefaultRouter()

router.register('users', UserViewSet, basename='users')  # Specify the basename for the defined filtered get_query_set

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]

urlpatterns += router.urls