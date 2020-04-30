from django.urls import path
from stats import views

app_name = 'stats'

urlpatterns = [
    path('upload/<country>', views.CSVParser.as_view(), name='upload_stat_world'),
    path('<stats>/', views.StatListView.as_view(), name='stats')
]
