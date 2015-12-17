"""EduBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.contrib import admin

from kb.apps.views import app_list

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/admin"), name='redirect_to_admin'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^_apps/helloworld/', include('apps.helloworld.urls')),
    url(r'^_apps/news/', include('apps.news.urls')),
    url(r'^_apps/main/', include('apps.main.urls')),
    url(r'^api/', include('kb.urls')),
    url(r'^api_old/', include('services.usermanagement.urls')),
]

