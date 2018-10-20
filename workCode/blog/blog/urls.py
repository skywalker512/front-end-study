"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from blogapp.views import index, tag, detail, index_login, index_register

urlpatterns = [
    path('admin/', admin.site.urls),  # django 自带的url，管理界面
    path('', index, name='index'), # 
    path('tag/<int:tag>', tag, name='tag'),
    path('detail/<int:post>', detail, name='detail'),
    path('page/<int:page>', index, name='page'),
    path('tag/<int:tag>/<int:page>', tag, name='tag_page'),
    path('login', index_login, name='index_login'),
    path('register', index_register, name='index_register'),
]
