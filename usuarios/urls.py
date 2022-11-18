from django.urls import path, include
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('log_user', log_user, name='log_user'),
    path('cad_user', cad_user, name='cad_user' ),
]