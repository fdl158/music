from django.urls import path
from . import views
urlpatterns = [
    # 用户的注册和登录
    path('login.html', views.loginView, name='login'),
    # 用户中心
    path('home/<int:page>.html', views.homeView, name='home'),
    # 退出用户登录
    path('logout.html', views.logoutView, name='logout'),
]