"""miware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from midapp import views as midapp_views


urlpatterns = [
    url(r'^sitedataadd/$', midapp_views.sitedataadd, name='sitedataadd'),
    url(r'^jsonadd/$', midapp_views.jsonadd, name='jsonadd'),
    # url(r'^midware/$', midapp_views.midware, name='midware'),
    url(r'^admin/', admin.site.urls),
]