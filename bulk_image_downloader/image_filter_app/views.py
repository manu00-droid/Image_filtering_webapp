from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def get_images(request):
    print(request)
    keyword = request.GET['image_keyword']
    count = request.GET['num_images']
    print(keyword)
    print(count)
    # res = int(val1) + int(val2)
    return HttpResponse("Hello World")
    # return render(request, 'result.html', {'result': res})
