from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('ranking/', include('ranking.urls')),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
]
