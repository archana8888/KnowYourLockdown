"""Know_Your_Lockdown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from quiz import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/',quiz_views.show_quiz, name='quiz'),
    path('',quiz_views.map, name='home'),
    path('chart/',quiz_views.get_chart, name='chart'),
    path('submit/',quiz_views.submit, name='submit'),
    path('getdata/',quiz_views.getdata, name='getdata'),
    path('info/',quiz_views.info,name = 'info'),
    path('map/',quiz_views.map,name = 'map'),
]
