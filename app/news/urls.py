from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news import views


router = DefaultRouter()
router.register('who-news', views.WhoNewsViewSet)

app_name = 'news'

urlpatterns = [
    path('', include(router.urls)),
    path('updates/<news>/', views.UpdatesListView.as_view(), name='updates')
]
