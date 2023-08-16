from django.shortcuts import render
from django.http import HttpResponse


def get_plans(request):
    return render(request, 'plans.html')


def payment(request):
    return render(request, 'payment_index.html')
