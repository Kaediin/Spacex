from django.urls import path
from SpaceXApi import views

urlpatterns = [
    path('', views.spaceXApi, name='index'),
    path('sort', views.sortLaunches, name='sort'),
    path('sort_upcoming', views.sortUpcoming, name='sort_upcoming'),
]