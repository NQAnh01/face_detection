from django.template import loader
from django.http import HttpResponse
from .forms import *
from django.shortcuts import render
import cv2
from .detect import detected

def index(request):

    if request.method == 'POST':
        name = request.FILES['detect'].name
        form = detectForm(request.POST, request.FILES)
        form.save()
        status = detected(name)
        url_img = '/media/detected/' + name
        if name == '':
            form = detectForm()
            return render(request, 'index.html', {'form' : form})
        return render(request, 'download.html', {'url_img' : url_img})
    else:
        form = detectForm()
        return render(request, 'index.html', {'form' : form})

    

