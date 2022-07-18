from django.urls import path

from dashboard import admin
from . import views

urlpatterns = [
    path('',  views.index, name= 'dashboard-index'),
    path('csv', views.handle_csv, name='upload_csv'),
]