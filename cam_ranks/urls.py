from django.contrib import admin
from django.urls import include, path
from search import views as search_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('search.urls')),
    path('ranking/', include('ranking.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
