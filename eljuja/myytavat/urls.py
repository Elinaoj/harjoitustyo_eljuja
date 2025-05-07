from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

app_name = 'myytavat'

urlpatterns = [ 
    path('', views.myytavat),
    path('myytava/', views.myytavat, name="myytava"),
    path('posts/', include('posts.urls')),
]