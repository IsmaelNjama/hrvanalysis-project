from django.urls import path, include
from . import views
from rest_framework import routers

from .views import SignUpAPIView, LoginAPIView

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)
router.register('subjects', views.SubjectView)
router.register('results', views.ResultView)
router.register('samples', views.SampleView)


urlpatterns = [
    path('signup/',SignUpAPIView.as_view(), name='api-signup'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('', include(router.urls)),
]