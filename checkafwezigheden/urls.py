from django.urls import path
from . import views

app_name = "checkafwezigheden"

urlpatterns = [
     path('', views.index, name='index'),
]