from django.urls import path
from .views import *

urlpatterns = [
    path('hv/', homeview),
    path('fv/', formview),
    path('sv/', showview),
    path('sdv/<pk>/', showDetailsview),
    path('uv/<x>/', updateview),
    path('dv/<y>/', deleteview),
]