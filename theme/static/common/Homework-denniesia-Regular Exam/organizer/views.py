from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Organizer
from .forms import  OrganizerCreateForm, OrganizerEditForm
from common.utils import get_user_obj
from django.utils import timezone
# Create your views here.
class OrganizerCreateView(CreateView):
    model = Organizer
    form_class = OrganizerCreateForm
    template_name = 'organizer/create-organizer.html'
    success_url = reverse_lazy('events')

class OrganizerDetailsView(DetailView):
    model = Organizer
    template_name = 'organizer/details-organizer.html'
    context_object_name = 'organizer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organizer = get_user_obj()
        events = organizer.events.all().filter(
            start_time__gt=timezone.now(),
        ).order_by('start_time')

        context['events'] = events
        return context

    def get_object(self):
        return get_user_obj()

class OrganizerEditView(UpdateView):
    model = Organizer
    form_class = OrganizerEditForm
    template_name = 'organizer/edit-organizer.html'
    success_url = reverse_lazy('organizer-details')


    def get_object(self):
        return get_user_obj()

class OrganizerDeleteView(DeleteView):
    template_name = 'organizer/delete-organizer.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return get_user_obj()


    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self,form):
        organizer = self.get_object()

        events = organizer.events.filter(
            start_time__gt=timezone.now()
        ).order_by('start_time')

        if events.exists():
            return self.form_invalid(form)

        return super().form_valid(form)