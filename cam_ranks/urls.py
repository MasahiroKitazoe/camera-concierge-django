from django.contrib import admin
from django.urls import include, path
from camera import views as search_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('camera.urls')),
    path('ranking/', include('ranking.urls')),
    path('admin/', admin.site.urls),
]
