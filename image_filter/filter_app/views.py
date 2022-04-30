from django.shortcuts import render
from django.http import HttpResponse
import zip_creator
import image_downloader


def index(request):
    return render(request,
                  '/home/manav/PycharmProjects/image_filtering_webapp/image_filter/filter_app/Templates/filter_app'
                  '/index.html')


def download(request):
    num_of_images = int(request.POST['num_of_images'])
    keyword = request.POST['keyword']
    print(type(keyword))
    print(type(num_of_images))
    image_downloader.downloader(keyword, num_of_images)
    zip_creator.zipper(keyword)
    return render(request,
                  "/home/manav/PycharmProjects/image_filtering_webapp/image_filter/filter_app/Templates/filter_app"
                  "/download.html",
                  {'keyword': keyword})
