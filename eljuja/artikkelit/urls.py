from django.urls import path, include
from . import views

app_name = 'artikkelit'

urlpatterns = [
    path('', views.artikkelit_lista, name='lista'),
    path('uusi-artikkeli/', views.artikkeli_uusi, name="uusi-artikkeli"),
]