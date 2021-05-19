from django.urls import path
from . import views
from apps.landingpage import views

urlpatterns=[
    path('', views.index, name='index'),
    ]