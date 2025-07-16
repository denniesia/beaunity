from django.contrib import messages
from django.contrib.auth.backends import UserModel
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django_browser_reload.views import events
from markdown_it.rules_core import inline

from beaunity.category.models import Category
from beaunity.comment.forms import CommentCreateForm
from beaunity.common.mixins_class import FilteredContextMixin, FilteredQuerysetMixin

from .forms import EventCreateForm, EventDeleteForm, EventEditForm
from .models import Event


# Create your views here.
class EventsOverviewView(
    LoginRequiredMixin, FilteredContextMixin, FilteredQuerysetMixin, ListView):

    model = Event
    template_name = "event/events-overview.html"
    ordering = ["-start_time"]
    context_object_name = "events"
    paginate_by = 9

    def get_queryset(self):
        return self.get_filtered_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_filtered_context(context, self.model)


class EventDetailsView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = "event"
    template_name = "event/event-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.object
        attendees = event.attendees.all()[:6]
        comments = event.comments.all().order_by("created_at")
        has_joined = event in self.request.user.event_attendees.all()

        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context.update(
            {
                "attendees": attendees,
                "form": CommentCreateForm(),
                "page_obj": page_obj,
                "has_joined": has_joined,
            }
        )

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
            return redirect(request.META.get("HTTP_REFERER") + f"#{self.object.id}")

        return redirect(reverse("event-details", kwargs={"pk": self.object.id}))


class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = "event/event-create.html"
    permission_required = "event.add_event"
    success_url = reverse_lazy("events")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("event-details", kwargs={"pk": self.object.pk})


class EventEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    permission_required = "event.change_event"
    template_name = "event/event-edit.html"

    def get_success_url(self):
        return reverse_lazy("event-details", kwargs={"pk": self.object.pk})


class EventDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = "event/event-delete.html"
    permission_required = "event.delete_event"
    success_url = reverse_lazy("events")

    def get_initial(self):
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(
            {
                "data": self.get_initial(),
            }
        )
        return kwargs


class MyEventsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Event
    context_object_name = "events"
    template_name = "event/my-events.html"
    permission_required = "event.add_event"
    raise_exception = True

    def get_queryset(self):
        self.archived = self.request.GET.get("archived", "false").lower() == "true"
        queryset = Event.objects.filter(created_by=self.request.user)

        if self.archived:
            queryset = queryset.filter(end_time__lt=now())
        else:
            queryset = queryset.filter(end_time__gte=now())

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["archived"] = self.archived
        return context
