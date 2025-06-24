from django.shortcuts import render
from django.views.generic import TemplateView
from beaunity.category.models import Category
from django.shortcuts import get_object_or_404, redirect
from beaunity.post.models import Post
from django.contrib.auth.decorators import login_required
from beaunity.common.forms import SearchForm
from beaunity.post.models import Post
from beaunity.event.models import Event
from beaunity.category.models import Category
from beaunity.accounts.models import AppUser
from django.db.models import Q
# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['events'] = Event.objects.all().order_by('-start_time')
        return context

class SearchView(TemplateView):
    template_name = 'common/search_results.html'

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
            )
            context['categories'] = Category.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
            context['users'] = AppUser.objects.filter(
                username__icontains=query
            )
        else:
            context['search_mode'] = False
            context['query'] = query
            context['form'] = form

        return context

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)


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


