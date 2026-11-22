from django.utils import timezone

from django.shortcuts import render
from .models import Event
# Create your views here.
def main(request):
    latest_event_list = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by("date")[:3]
    context = {"latest_event_list" : latest_event_list}
    return render(request, "events/home.html", context)

def event_list(request):
    full_event_list = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by("date")
    context = {"full_event_list": full_event_list}
    return render(request, "events/event_list.html", context)