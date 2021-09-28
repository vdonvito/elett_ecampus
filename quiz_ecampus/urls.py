"""quiz_ecampus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    #path("delete_all/", views.delete_all, name="delete_all"),
    path("prnt/", views.prnt, name="prnt"),
    path("view_all/", views.view_all, name="view_all"),
    path("start/", views.start, name="start"),
    path("quiz/", views.quiz, name="quiz"),
    path("result/", views.result, name="result"),
    path("ResultError/", views.result_error, name="result_error"),
    path("storico/", views.storico, name="storico"),
]
