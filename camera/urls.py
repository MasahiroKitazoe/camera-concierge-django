from django.urls import path

from . import views

app_name = 'camera'

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('search/', views.search, name='search'),
    path("camera/<int:camera_id>", views.detail, name="detail")
]
