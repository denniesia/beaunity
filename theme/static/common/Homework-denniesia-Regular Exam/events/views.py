from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import  EventCreateForm, EventEditForm, EventDeleteForm
from .models import  Event

from common.utils import get_user_obj
# Create your views here.
class EventsView(ListView):
    template_name = 'events/events.html'

    context_object_name = 'events'
    def get_queryset(self):
        return Event.objects.all().order_by('-start_time')


class EventCreateView(CreateView):
    model = Event
    template_name = 'events/create-event.html'
    form_class = EventCreateForm
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.organizer = get_user_obj()
        return super().form_valid(form)

class EventDetailsView(DetailView):
    model = Event
    template_name = 'events/details-event.html'
    context_object_name = 'event'
    pk_url_kwarg = 'event_pk'

class EventEditView(UpdateView):
    model = Event
    template_name = 'events/edit-event.html'
    form_class = EventEditForm
    pk_url_kwarg = 'event_pk'

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'event_pk': self.object.pk})

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/delete-event.html'
    form_class = EventDeleteForm
    pk_url_kwarg = 'event_pk'
    success_url = reverse_lazy('events')


    def get_initial(self):
        return self.object.__dict__








