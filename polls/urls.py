
from django.contrib import admin
from django.urls import path

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('system', views.system, name='system'),
    path('language', views.language, name='language'),
    path('ide', views.ide, name='ide'),
]
