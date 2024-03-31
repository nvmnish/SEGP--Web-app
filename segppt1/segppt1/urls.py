"""
URL configuration for segppt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from appforsegppt1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.admin_page, name='admin_page'),
    path('options_page', views.options_page, name='options_page'),
    
    path('add_new_image_options', views.add_new_image_options, name='add_new_image_options'),
    path('delete_image_options', views.delete_image_options, name='delete_image_options'),
    path('update_image_options', views.update_image_options, name='update_image_options'),
    path('search_image_options', views.search_image_options, name='search_image_options'),
    
    path('add_WSI', views.add_WSI, name='add_WSI'),
    path('add_IHC', views.add_IHC, name='add_IHC'),
    path('add_tumor_mask', views.add_tumor_mask, name='add_tumor_mask'),
    path('add_HandE', views.add_HandE, name='add_HandE'),
    
    path('delete_WSI', views.delete_WSI, name='delete_WSI'),
    path('delete_IHC', views.delete_IHC, name='delete_IHC'),
]
