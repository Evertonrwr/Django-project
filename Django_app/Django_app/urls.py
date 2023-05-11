"""
URL configuration for Django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('app.html', TemplateView.as_view(template_name='app.html')),
    path('game_over.html', TemplateView.as_view(template_name='game_over.html')),
    path('vitoria.html', TemplateView.as_view(template_name='vitoria.html')),

]
