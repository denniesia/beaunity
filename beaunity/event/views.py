from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event
from beaunity.category.models import Category
from django.db.models import Q
from django.db.models import Count
from django.utils.timezone import now
# Create your views here.
class EventsOverviewView(ListView):
    template_name = 'event/events-overview.html'
    ordering = ['-start_time']
    context_object_name = 'events'

    def get_queryset(self):

        queryset = Event.objects.filter(
            is_archived=False,
        ).order_by('start_time')
        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')
        archived = self.request.GET.get('archived')

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if sort_by == 'Popularity':
            queryset = queryset.annotate(popularity=Count('attendees')).order_by('-popularity')
        elif sort_by == 'Online':
            queryset = queryset.filter(is_online=True)
        elif sort_by == 'Public_events':
            queryset = queryset.filter(is_public=True)
        elif sort_by == 'Hosts':
            queryset = queryset.order_by('created_by__username')
        if archived:
            queryset = queryset.filter(
            is_archived=True,
            ).order_by('start_time')
        print(current_date)
        print(current_datetime)
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cities'] = Event.objects.values_list('city', flat=True).distinct()

        request = self.request
        filter_mode = any([
            request.GET.get('city'),
            request.GET.get('category'),
            request.GET.get('sort_by'),
            request.GET.get('archived')
        ])

        context['filter_mode'] = filter_mode
        return context

class EventDetailsView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event/event-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attendees = self.object.attendees.all().select_related('profile')
        context['attendees'] = attendees
        print(attendees)
        return context

class MyEventsView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/my-events.html'

    def get_queryset(self):
        self.archived = self.request.GET.get('archived', 'false').lower() == 'true'
        queryset = Event.objects.filter(created_by=self.request.user)

        if self.archived:
            queryset = queryset.filter(end_time__lt=now())
        else:
            queryset = queryset.filter(end_time__gte=now())

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archived'] = self.archived  # Pass boolean, not string
        return context