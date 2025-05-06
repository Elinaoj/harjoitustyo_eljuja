from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [ 
    path('', views.myytavat),
    path('myytavat/', views.myytavat),
    path('posts/', include('posts.urls')),
]