from django.urls import path
from stats import views

app_name = 'stats'

urlpatterns = [
    path('upload/<country>/', views.CSVParser.as_view(), name='upload_stat_world'),
    path('world/', views.WorldTableView.as_view(), name='world_table_data'),
    path('india-stats/', views.IndiaTableView.as_view(), name='india_table_data'),
    path('<stats>/', views.StatListView.as_view(), name='stats')
]
