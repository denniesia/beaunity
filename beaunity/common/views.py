from django.shortcuts import render
from django.views.generic import ListView
from beaunity.category.models import Category
from django.shortcuts import get_object_or_404, redirect
from beaunity.post.models import Post
# Create your views here.
class IndexView(ListView):
    template_name = 'common/landing_page.html'

    def get_queryset(self):
        return Category.objects.all()


#TODO - Challenge and Events logic
def approve_functionality(request, pk: int):

    approved_object = get_object_or_404(Post, pk=pk)

    if request.user.has_perm('post.can_approve_post'):
        approved_object.is_approved = True
        approved_object.save()
        return redirect('post-pending')

    return redirect('post-details', pk=pk)

def not_found_page(request):
    return render(request, 'common/404.html')

