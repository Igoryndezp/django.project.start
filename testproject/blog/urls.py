from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('test/',test),
]