from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'main/capital.html')

def about(request):

    return render(request, 'main/about.html')

def docker(request):

    return render(request, 'main/docker.html')