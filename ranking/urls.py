from django.urls import path

from . import views

app_name = 'ranking'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/<str:sort_type>/", views.DetailView.as_view(), name="detail"),
]
