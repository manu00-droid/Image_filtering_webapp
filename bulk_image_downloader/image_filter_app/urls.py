from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('get_images', views.get_images, name='get_images'),
]
