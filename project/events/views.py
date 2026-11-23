from django.utils import timezone

from django.shortcuts import get_object_or_404, render
from .models import Event
# Create your views here.


def main(request):
    latest_event_list = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by("date")[:3]
    context = {"latest_event_list": latest_event_list}
    return render(request, "events/home.html", context)


def event_list(request):
    full_event_list = Event.objects.filter(is_published=True, date__gte=timezone.now()).order_by("date")
    context = {"full_event_list": full_event_list}
    return render(request, "events/event_list.html", context)


def details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/details.html", {"event": event})