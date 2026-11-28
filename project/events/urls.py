from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.details, name="details"),
    path("<int:event_id>/reg/", views.reg, name="reg"),
]