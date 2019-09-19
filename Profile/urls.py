from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import login

urlpatterns = [
    path('', views.index, name='index'),
    url('^login/$', login,{'template_name':'Profile/login.html'}),
    path('post/new/', views.post_new, name='post_new'),
    path('user/new/', views.user_new, name='user_new'),
    path('profile/new/', views.profile_new, name='profile_new')
]


