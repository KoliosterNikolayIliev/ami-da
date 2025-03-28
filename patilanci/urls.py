"""patilanci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path, include


def render_react(request):
    return render(request, "index.html")


def catch_all(request, path):
    # Redirect to the homepage or any other desired URL
    return redirect('/')


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls', namespace='index')),
                  path('', render_react),
                  path('projects', render_react),
                  path('video-gallery', render_react),
                  path('image-gallery', render_react),
                  path('live', render_react),
                  path('charity', render_react),
                  # re_path(r"^$", render_react),
                  # re_path(r"^(?:.*)/?$", render_react),
                  # re_path(r'^(?P<path>.*)/$', catch_all),

              ]
from django.views.static import serve
urlpatterns += [
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]
