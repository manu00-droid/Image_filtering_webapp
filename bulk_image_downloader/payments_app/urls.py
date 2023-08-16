from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_plans, name='get_plans'),
    path('payment', views.payment, name='payment'),
]
