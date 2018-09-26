"""我的练习 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

from study import default_views

# name 可以用于在 templates, models, views ……中得到对应的网址，
# 相当于“给网址取了个别名”，只要这个别名不变，路径网址名变了也能通过别名获取到
# 在页面中的使用
# 不带参数的：
# {% url 'name' %}
# 带参数的：参数可以是变量名
# {% url 'name' 参数 %}
# 在Ajax中的使用 url: "{% url 'chart3' %}",
urlpatterns = [
    # 路由分发
    # path('', default_views.index, name='index'),  # 主页
    path('', default_views.href, name='href'),
    path('', include('study.urls.bootstrap_urls')),
    path('', include('study.urls.layui_urls')),
    path('', include('study.urls.user_urls')),
]
