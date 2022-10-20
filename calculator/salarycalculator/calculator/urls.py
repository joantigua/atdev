from os import name
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('results/', views.results, name ='results'),
]

