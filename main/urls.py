from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('data', views.data),
    path('create', views.create)
]