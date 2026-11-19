from django.shortcuts import render
from .models import Event
# Create your views here.
def main(request):
    latest_event_list = Event.objects.order_by("-date")[:3]
    context = {"latest_event_list" : latest_event_list}
    return render(request, "events/home.html", context)