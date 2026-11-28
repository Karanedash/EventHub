from django.utils import timezone
from .forms import RegistrationForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import Event, Registration
from django.contrib import messages
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
    event = get_object_or_404(Event, pk=event_id, is_published=True)
    return render(request, "events/details.html", {"event": event, "form": RegistrationForm()})


def reg(request, event_id):
    event = get_object_or_404(Event, pk=event_id, is_published=True)
    if request.method != "POST":
        return redirect("details", event_id=event.id)

    form = RegistrationForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data["email"].strip().lower()
        if Registration.objects.filter(email=email, event=event).exists():
            form.add_error("email", "Такой email уже записан на мероприятие")
        else:
            registration = form.save(commit=False)
            registration.event = event
            registration.email = email
            registration.status = "new"
            registration.save()
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect("details", event_id=event.id)

    data = {"form": form, "event": event}
    return render(request, "events/details.html", data)