from django.shortcuts import render
from django.views.generic import ListView
from beaunity.category.models import Category
from django.shortcuts import get_object_or_404, redirect
from beaunity.post.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(ListView):
    template_name = 'common/landing_page.html'

    def get_queryset(self):
        return Category.objects.all()

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


