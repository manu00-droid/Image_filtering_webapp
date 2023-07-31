from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.user_login, name='lgoin'),
    path('register/', views.register, name='register'),
    path('new_user/', views.register_new_user, name='register_new_user'),
    path('logout/', views.user_logout, name='user_logout'),
]
