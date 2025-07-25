from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now
from django.views.generic import DetailView, TemplateView

from beaunity import settings
from beaunity.accounts.models import Profile
from beaunity.category.models import Category
from beaunity.challenge.models import Challenge
from beaunity.comment.models import Comment
from beaunity.common.tasks import send_approval_email
from beaunity.event.models import Event
from beaunity.interaction.models import Favourite, Like
from beaunity.main.forms import ContactForm
from beaunity.common.forms import SearchForm
from beaunity.post.models import Post

UserModel = get_user_model()

class LandingPageView(TemplateView):
    template_name = 'main/landing-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()

        current_datetime = now()
        context['events'] = Event.objects.filter(
            end_time__gte=current_datetime
        ).order_by('start_time')[:3]

        context['challenges'] = Challenge.objects.exclude(
            is_approved=False
        ).filter(
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

    return render(request, 'main/about.html', {'form': form})


class SearchView(TemplateView):
    template_name = 'common/search-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SearchForm(self.request.GET)

        if form.is_valid():
            query = form.cleaned_data["query"]
            context['query'] = query
            context['form'] = form
            context['search_mode'] = True

            context['posts'] = Post.objects.filter(
                Q(title__icontains=query)
                    |
                Q(content__icontains=query)
            ).exclude(
                is_approved=False
            )

            context['categories'] = Category.objects.filter(
                Q(title__icontains=query)
                    |
                Q(description__icontains=query)
            )

            context['events'] = Event.objects.filter(
                title__icontains=query
            )

            context['challenges'] = Challenge.objects.filter(
                title__icontains=query
            ).exclude(
                is_approved=False
            )

            context['users'] = UserModel.objects.filter(
                username__icontains=query
            )

        else:
            context['search_mode'] = False
            context['query'] = query
            context['form'] = form

        return context


class DashboardView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'main/dashboard.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.get_object()
        profile = user.profile

        my_events =  Event.objects.filter(
            created_by=user
        )
        fav_events = Event.objects.filter(
            favourites__user=user,
        )
        liked_events = Event.objects.filter(
            likes__user=user
        )
        comments_events = Event.objects.filter(
            comments__created_by=user
        )

        my_posts = Post.objects.filter(
            created_by=user,
            is_approved=True
        ).order_by(
            '-created_at'
        )
        fav_posts = Post.objects.filter(
            favourites__user=user
        )
        liked_posts = Post.objects.filter(
            likes__user=user,
        )
        comments_posts = Post.objects.filter(
           comments__created_by=user,
        )

        my_challenges = Challenge.objects.filter(created_by=user, is_approved=True).order_by('-start_time')
        fav_challenges = Challenge.objects.filter(
            favourites__user=user,
        )
        liked_challenges = Challenge.objects.filter(
            likes__user=user,
        )
        comments_challenges = Challenge.objects.filter(
           comments__created_by=user,
        )

        context.update({
            'fav_events': fav_events,
            'fav_posts': fav_posts,
            'fav_challenges': fav_challenges,
            'my_posts': my_posts,
            'my_events': my_events,
            'my_challenges': my_challenges,
            'joined_events': Event.objects.filter(attendees=user),
            'joined_challenges': Challenge.objects.filter(attendees=user),
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

