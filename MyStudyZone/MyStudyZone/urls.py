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
from study.views import jquery_util_test_view

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
	path('', default_views.index, name='index'),
	path('', include('study.urls.bootstrap_urls')),
	path('', include('study.urls.layui_urls')),
	path('', include('study.urls.user_urls')),
	path('jquery_util_test', jquery_util_test_view.jquery_util_test, name='jquery_util_test'),
	path('jquery_util_ajx_test', jquery_util_test_view.jquery_util_ajx_test, name='jquery_util_ajx_test'),
	path('jquery_util_ajax_fileupload', jquery_util_test_view.jquery_util_ajax_fileupload,
		 name='jquery_util_ajax_fileupload'),
	path('jquery_util_test_typeaheadjs', jquery_util_test_view.jquery_util_test_typeaheadjs,
		 name='jquery_util_test_typeaheadjs'),
	path('get_ztree_nodes', jquery_util_test_view.get_ztree_nodes, name='get_ztree_nodes'),
	# 另一个app的url
	path('itchat/', include('testApp.urls.itchat_url')),
	# JTable数据表格测试
	path('JTable_test', default_views.JTable_test, name='JTable_test'),
	path('jtable_test_user_available', default_views.jtable_test_user_available, name='jtable_test_user_available'),
	# DataTables测试
	path('jquery_datatables_test', default_views.jquery_datatables_test, name='jquery_datatables_test'),
	path('jquery_datatables_getdata', default_views.jquery_datatables_getdata, name='jquery_datatables_getdata'),

]
