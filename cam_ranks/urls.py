from django.contrib import admin
from django.urls import include, path
from search import views as search_views

urlpatterns = [
    path('', include('search.urls')),
    path('ranking/', include('ranking.urls')),
    path('admin/', admin.site.urls),
]
