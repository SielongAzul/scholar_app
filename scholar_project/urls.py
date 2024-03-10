
#Note from Azul: Do not create your routes here because the views are mostly on the app folder (scholarweb)
#scholar_project created in startproject command 
#scholarweb created via startapp command

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scholarweb.urls'))
]
