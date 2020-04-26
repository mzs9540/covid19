from django.urls import path
from stats import views

urlpatterns = [
    path('upload/', views.CSVParser.as_view(), name='upload_stat_world'),
    path('', views.WorldStatListView.as_view(), name='stats')
]
