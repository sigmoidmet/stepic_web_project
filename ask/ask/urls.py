"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import path
from qa.views import test
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',                                              
   url(r'^$', 'test'),                                                              
   url(r'^login/.*$', 'test', name='login'),                                    
   url(r'^signup/.*', 'test', name='signup'),                                   
   url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question'),                 
   url(r'^ask/.*', 'test', name='ask'),                                         
   url(r'^popular/.*', 'test', name='popular'),                                 
   url(r'^new/.*', 'test', name='new'),                                         
)   
