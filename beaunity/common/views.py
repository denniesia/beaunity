from django.shortcuts import render
from django.views.generic import TemplateView
from beaunity.category.models import Category
from django.shortcuts import get_object_or_404, redirect
from beaunity.post.models import Post
from django.contrib.auth.decorators import login_required
from beaunity.common.forms import SearchForm, ContactForm
from beaunity.post.models import Post
from beaunity.event.models import Event
from beaunity.category.models import Category
from beaunity.challenge.models import Challenge
from beaunity.event.models import Event
from beaunity.accounts.models import AppUser
from django.db.models import Q
from django.utils.timezone import now
from django.core.mail import send_mail
from django.conf import settings

from beaunity.challenge.models import Challenge

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

        context['challenges'] = Challenge.objects.filter(
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
                settings.EMAIL_HOST_USER,
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


#TODO - Challenge and Events logic
@login_required
def approve_functionality(request, pk: int):

    approved_object = get_object_or_404(Post, pk=pk)

    if request.user.has_perm('post.can_approve_post'):
        approved_object.is_approved = True
        approved_object.save()
        return redirect('post-pending')

    return redirect('post-details', pk=pk)

@login_required
def disapprove_functionality(request, pk: int):
    declined_object = get_object_or_404(Post, pk=pk)
    if request.user.has_perm('post.can_approve_post'):
        declined_object.delete()
        return redirect('post-pending')



