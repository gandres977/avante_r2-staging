from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.avanteCoreView, name='avantecore'),
]
