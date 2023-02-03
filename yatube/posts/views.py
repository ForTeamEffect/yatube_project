from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Главная су')


def group_posts(request, slug):
    return HttpResponse(f'Главная Groups: {slug}')