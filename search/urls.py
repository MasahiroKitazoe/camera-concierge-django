from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('index/', views.index, name='index')
]
