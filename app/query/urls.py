from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('me', views.Covid19QueryView)
router.register('replies', views.Covid19QueryRepliesView)

app_name = 'query'

urlpatterns = [
    path('', include(router.urls)),
]
