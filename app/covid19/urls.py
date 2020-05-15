from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/news/', include('news.urls')),
    path('api/stats/', include('stats.urls')),
    path('api/query/', include('query.urls')),
]
