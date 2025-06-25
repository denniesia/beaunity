from django.shortcuts import render
from django.views.generic import ListView
from .models import Event
from beaunity.category.models import Category

from django.db.models import Count
from django.utils.timezone import now
# Create your views here.
class EventsOverviewView(ListView):
    template_name = 'event/events-overview.html'
    ordering = ['-start_time']
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.all()
        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')
        archived = self.request.GET.get('archived')

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if sort_by == 'Popularity':
            queryset = queryset.annotate(popularity=Count('events')).order_by('-popularity')
        elif sort_by == 'Online':
            queryset = queryset.filter(is_online=True)
        elif sort_by == 'Public_events':
            queryset = queryset.filter(is_public=True)
        elif sort_by == 'Hosts':
            queryset = queryset.order_by('created_by__username')
        if archived:
            queryset = queryset.filter(end_time__lt=now())

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
