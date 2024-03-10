from django.urls import path
from . import views

#This is like a controller for PHP because this is Django
#Most of the routes should be put in here and it's all working but make sure that the database is enabled or else it will throw errors when you use 
#python manage.py runserver

#DO NOT TOUCH ANYTHING ELSE BECAUSE IT'S ALREADY CONFIGURED BY DEFAULT#
#Except for urlpatterns we need more routes for this.
urlpatterns = [
    path('', views.index, name="Home App Development Mode"),
    path('test/', views.test, name="test"),
]