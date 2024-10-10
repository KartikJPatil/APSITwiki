from django.urls import path

from . import views

urlpatterns = [
    path("wiki/<str:title>", views.entryPage, name="entrypage"),
    path("search", views.search, name="search"),
    path("new", views.createEntry, name="newentry"),
    path("edit", views.editEntry, name="edit"),
    path("random", views.randomPage, name="random"),
    path("Function", views.Function, name="Function"),
    path("", views.index, name="index")
]