from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,  DetailView, UpdateView, DeleteView
from .models import Event
from beaunity.category.models import Category
from django.db.models import Q
from django.db.models import Count
from django.utils.timezone import now
from .forms import EventCreateForm, EventEditForm, EventDeleteForm
from beaunity.comment.forms import  CommentCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class EventsOverviewView(ListView):
    template_name = 'event/events-overview.html'
    ordering = ['-start_time']
    context_object_name = 'events'

    def get_queryset(self):
        current_datetime = now()
        archived = self.request.GET.get('archived', '').lower() == 'true'

        if archived:
            queryset = Event.objects.filter(end_time__lt=current_datetime)
        else:
            queryset = Event.objects.filter(end_time__gte=current_datetime)

        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if sort_by == 'Popularity':
            queryset = queryset.annotate(popularity=Count('attendees')).order_by('-popularity')
        elif sort_by == 'Online':
            queryset = queryset.filter(is_online=True)
        elif sort_by == 'Public events':
            queryset = queryset.filter(is_public=True)
        elif sort_by == 'Hosts':
            queryset = queryset.order_by('created_by__username')

        if sort_by not in ['Popularity', 'Hosts']:
            queryset = queryset.order_by('start_time')

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

class EventDetailsView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event/event-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attendees = self.object.attendees.select_related('profile')[:6]
        context['attendees'] = attendees
        context['comments'] = self.object.comments.all()

        context['form'] = CommentCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user

            comment.content_type = ContentType.objects.get_for_model(self.model)
            comment.object_id = self.object.id
            comment.save()
            return redirect(request.META.get('HTTP_REFERER') + f"#{self.object.id}")
        return reverse_lazy('event-details', kwargs={'object_id': self.object.id})


class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'event/event-create.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'pk': self.object.pk})


class EventEditView(UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = 'event/event-edit.html'

    def get_success_url(self):
        return reverse_lazy('event-details', kwargs={'pk': self.object.pk})

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/event-delete.html'
    form_class = EventDeleteForm
    success_url = reverse_lazy('events')

    def get_initial(self):
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        context['categories'] = event.categories.all()
        return context


class MyEventsView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/my-events.html'
    permission_required = 'event.change_event'
    raise_exception = True

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


