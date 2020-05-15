from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('world/', views.WorldTableView.as_view(), name='world_table_data'),
    path('world-map/', views.WorldMap.as_view(), name='world_map'),
    path('upload/<country>/', views.CSVParser.as_view(), name='upload_stat_world'),
    path('india-stats/', views.IndiaTableView.as_view(), name='india_table_data'),
    path('<stats>/', views.StatListView.as_view(), name='stats'),
]
