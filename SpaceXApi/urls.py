from django.urls import path
from SpaceXApi import views

urlpatterns = [
    path('', views.spaceXApi, name='index'),
]