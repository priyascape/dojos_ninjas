from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_dojo', views.submit_dojo),
    path('submit_ninja', views.submit_ninja),
    path('delete', views.delete),
]