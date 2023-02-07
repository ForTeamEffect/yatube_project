from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    html = 'posts/index.html'
    context = {
        'main_name': "Это главная страница проекта Yatube"
    }
    return render(request, html, context)


def index_posts(request):
    return render(request, 'posts/index 2.html')


def groups_info(request):
    html = 'posts/groups_info.html'
    context = {
        'first': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, html, context)


def group_posts(request):
    return render(request, 'posts/group_list.html')


def group_post(request, slug):
    return HttpResponse(f'Главная Groups: {slug}')
