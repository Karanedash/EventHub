from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("events/", views.event_list, name="event_list"),
]