from django.shortcuts import render
from django.http import HttpResponse
from bing_image_downloader import downloader
from datetime import datetime
import os
import shutil
from zipfile import ZipFile
from django.contrib import messages


PARENT_DIR = os.path.join(os.getcwd(), 'downloads')


def home(request):
    return render(request, 'home.html')


def get_images(request):
    print(request)
    keyword = request.GET['image_keyword']
    count = int(request.GET['num_images'])
    path = str(PARENT_DIR) + "/"+str(keyword) + \
        str(datetime.now().strftime("%d-%m-%Y-%H-%M-%S"))
    os.makedirs(path)
    print(path)
    downloader.download(keyword, limit=count, output_dir=path,
                        adult_filter_off=True, force_replace=False, timeout=60)

    zip_path = create_zip(path+"/"+keyword)
    if zip_path is not None:
        return render(request, 'download.html', {'keyword': keyword, 'path': zip_path})
    else:
        messages.error("couldn't create zip file")
        return render(request, 'home.html')


def create_zip(path):
    print("creating zip file at path: ", path)
    with ZipFile(path+'.zip', 'w') as zip_object:
        print(os.listdir(path))
        for filename in os.listdir(path):
            print(filename)
            # f = os.path.join(path, filename)
            if os.path.isfile(filename):
                print(filename)
                zip_object.write(filename=filename)
    if os.path.exists(path):
        # shutil.rmtree(path)
        return path+'.zip'
    else:
        print("Couldn't create zip file")
        return None
