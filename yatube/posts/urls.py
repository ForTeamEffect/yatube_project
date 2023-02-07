from django.urls import path

from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.index,name='just_main'),
    path('posts/', views.index_posts, name='Main_posts'),
    path('group_posts/', views.group_posts,name='posts_of_group'),
    path('groups/', views.groups_info, name='main_groups'),
    path('group/<slug:slug>/', views.group_post,name='post')

]