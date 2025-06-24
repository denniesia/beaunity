from django.shortcuts import render
from django.views.generic import ListView
from .models import Event

# Create your views here.
class EventsOverviewView(ListView):
    template_name = 'event/events-overview.html'
    ordering = ['-start_time']
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all()