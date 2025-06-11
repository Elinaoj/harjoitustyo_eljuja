from django.urls import path, include
from . import views

app_name = 'artikkelit'

urlpatterns = [
    path('uusi-artikkeli/', views.artikkeli_uusi, name="uusi-artikkeli"),
    path('export-myynti/', views.export_myynnit_to_excel, name='export_myynnit'),
]