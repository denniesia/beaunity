from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from beaunity.comment.forms import CommentCreateForm
from beaunity.common.mixins import UserIsCreatorMixin
from beaunity.common.filter_mixins import (FilteredContextMixin,
                                           FilteredQuerysetMixin)
from beaunity.common.views import approve_instance, disapprove_instance

from .forms import ChallengeCreateForm, ChallengeDeleteForm, ChallengeEditForm
from .models import Challenge


# Create your views here.
class ChallengeOverviewView(LoginRequiredMixin, FilteredContextMixin, FilteredQuerysetMixin, ListView):
    model = Challenge
    ordering = ["start_time"]
    template_name = "challenge/challenges-overview.html"
    context_object_name = "challenges"
    paginate_by = 5

    def get_queryset(self):
        return self.get_filtered_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_filtered_context(context, self.model)


class ChallengeCreateView(LoginRequiredMixin, CreateView):
    model = Challenge
    template_name = "challenge/challenge-create.html"
    form_class = ChallengeCreateForm

    def form_valid(self, form):
        challenge = form.save(commit=False)

        challenge.created_by = self.request.user

        if self.request.user.has_perm("challenge.can_approve_challenge"):
            challenge.is_approved = True

        challenge.save()
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.has_perm("challenge.can_approve_challenge"):
            return reverse_lazy("challenge-details", kwargs={"pk": self.object.pk})
        return reverse_lazy("challenge-confirmation")


class ChallengeDetailsView(LoginRequiredMixin, DetailView):
    model = Challenge
    template_name = "challenge/challenge-details.html"
    context_object_name = "challenge"

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            "attendees"
        ).select_related(
            "created_by"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = self.get_object()
        attendees = challenge.attendees.all()[:6]
        comments = challenge.comments.all().order_by("created_at")

        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context.update(
            {
                "attendees": attendees,
                "form": CommentCreateForm(),
                "page_obj": page_obj,
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

        return redirect(reverse("challenge-details", kwargs={"pk": self.object.id}))


class ChallengeEditView(UpdateView):
    model = Challenge
    form_class = ChallengeEditForm
    template_name = "challenge/challenge-edit.html"

    def get_success_url(self):
        return reverse_lazy("challenge-details", kwargs={"pk": self.object.pk})


class ChallengeDeleteView(LoginRequiredMixin, UserIsCreatorMixin, DeleteView):
    model = Challenge
    form_class = ChallengeDeleteForm
    template_name = "challenge/challenge-delete.html"
    success_url = reverse_lazy("challenges")

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


class PendingChallengeView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Challenge
    template_name = "challenge/pending-challenges.html"
    permission_required = "challenge.can_approve_challenge"
    paginate_by = 5

    def get_queryset(self):
        return Challenge.objects.filter(is_approved=False).order_by("-created_at")


def approve_challenge(request, pk):
    return approve_instance(
        request=request,
        model_class=Challenge,
        pk=pk,
        content_type="challenge",
        permission_required="challenge.can_approve_challenge",
        redirect_approved="challenge-pending",
        redirect_fallback="challenge-pending",
    )


def disapprove_challenge(request, pk):
    return disapprove_instance(
        request=request,
        model_class=Challenge,
        pk=pk,
        permission_required="challenge.can_approve_challenge",
        redirect_disapproved="challenge-pending",
        redirect_fallback="challenge-pending",
    )


@login_required(login_url="login")
def challenge_confirmation(request):
    return render(request, "challenge/challenge-create-confirmation.html")
