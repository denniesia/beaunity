from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from beaunity.category.models import Category
from django.shortcuts import get_object_or_404, redirect
from beaunity.post.models import Post
from django.contrib.auth.decorators import login_required
from beaunity.common.forms import SearchForm, ContactForm
from beaunity.post.models import Post
from beaunity.event.models import Event, UserModel
from beaunity.category.models import Category
from beaunity.challenge.models import Challenge

from beaunity.comment.models import Comment

from beaunity.accounts.models import AppUser
from django.db.models import Q
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings
from beaunity.accounts.models import Profile

from beaunity.challenge.models import Challenge
from django.contrib.contenttypes.models import ContentType
from beaunity.interaction.models import Favourite, Like
from django.contrib.auth.mixins import LoginRequiredMixin
from beaunity.common.tasks import send_approval_email
from django.contrib.auth.models import Group
# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/landing-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        current_datetime = now()
        context['events'] = Event.objects.filter(
            end_time__gte=current_datetime
        ).order_by('start_time')[:3]

        context['challenges'] = Challenge.objects.exclude(is_approved=False).filter(
            end_time__gte=current_datetime
        ).order_by('start_time')[:3]
        return context


def about_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            full_message = f"Message from {name} ({email}) on beaunity :\n\n{content}"

            send_mail(
                subject,
                full_message,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return render(request, 'common/email_confirmation.html')
    return render(request, 'common/about.html', {'form': form})



class SearchView(TemplateView):
    template_name = 'common/search-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SearchForm(self.request.GET)
        query = self.request.GET.get('query', '').strip()

        if form.is_valid() and query:
            context['query'] = query
            context['form'] = form
            context['search_mode'] = True

            context['posts'] = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).exclude(is_approved=False)
            context['categories'] = Category.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            context['events'] = Event.objects.filter(
                title__icontains=query
            )
            context['challenge'] = Challenge.objects.filter(
                title__icontains=query
            ).exclude(is_approved=False)
            context['users'] = AppUser.objects.filter(
                username__icontains=query
            )
        else:
            context['search_mode'] = False
            context['query'] = query
            context['form'] = form

        return context

def custom_permission_denied_view(request, exception=None):
    return render(request, "common/403.html", status=403)


UserModel = get_user_model()

class DashboardView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'common/dashboard.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        profile = user.profile

        event_content_type = ContentType.objects.get_for_model(Event)
        fav_events = Event.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=event_content_type,
            ).values_list('object_id', flat=True)
        )
        liked_events = Like.objects.filter(
            user=user,
            content_type=event_content_type,
        )
        comments_events = Comment.objects.filter(
            created_by=user,
            content_type=event_content_type,
        )

        post_content_type = ContentType.objects.get_for_model(Post)
        fav_posts = Post.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=post_content_type,
            ).values_list('object_id', flat=True)
        )
        liked_posts = Like.objects.filter(
            user=user,
            content_type=post_content_type,
        )
        comments_posts = Comment.objects.filter(
            created_by=user,
            content_type=post_content_type,
        )

        challenge_content_type = ContentType.objects.get_for_model(Challenge)
        fav_challenges = Challenge.objects.filter(
            id__in=Favourite.objects.filter(
                user=user,
                content_type=challenge_content_type,
            ).values_list('object_id', flat=True)
        )
        liked_challenges = Like.objects.filter(
            user=user,
            content_type=challenge_content_type,
        )
        comments_challenges = Comment.objects.filter(
            created_by=user,
            content_type=challenge_content_type,
        )

        context.update({
            'fav_events': fav_events,
            'fav_posts': fav_posts,
            'fav_challenges': fav_challenges,
            'my_posts': Post.objects.filter(created_by=user, is_approved=True).order_by('-created_at'),
            'my_events': Event.objects.filter(created_by=user),
            'joined_events': Event.objects.filter(attendees=user),
            'joined_challenges': Challenge.objects.filter(attendees=user),
            'challenges': Challenge.objects.filter(created_by=user, is_approved=True).order_by('-start_time'),
            'likes': Like.objects.filter(user=user),
            'favs': Favourite.objects.filter(user=user),
            'liked_posts': liked_posts.count(),
            'liked_events': liked_events.count(),
            'liked_challenges': liked_challenges.count(),
            'comments': Comment.objects.filter(created_by=user),
            'comments_events': comments_events.count(),
            'comments_challenges': comments_challenges.count(),
            'comments_posts': comments_posts.count(),
        })

        if self.request.user.is_superuser:
            context.update({
                'superusers': UserModel.objects.filter(groups__name='Superuser').count(),
                'moderators': UserModel.objects.filter(groups__name='Moderator').count(),
                'organizers': UserModel.objects.filter(groups__name='Organizer').count(),
                'users': UserModel.objects.count(),
            })

        return context


@login_required
def approve_instance(request, model_class, pk: int, content_type:str, permission_required: str, redirect_approved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.is_approved = True
        instance.save()
        send_approval_email.delay(
            user_id=instance.created_by.id,
            object_type=content_type,
            object_title=instance.title
        )
        return redirect(redirect_approved)

    return redirect(redirect_fallback, pk=pk)


@login_required
def disapprove_instance(request, model_class, pk: int, permission_required: str, redirect_disapproved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.delete()
        return redirect(redirect_disapproved)

    return redirect(redirect_fallback, pk=pk)