from django.contrib import admin
from django.urls import path

from places import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.detail_view, name='detail_view'),
]
