from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Like, Dislike

# Create your views here.

def like_functionality(request, model_name, object_id):
   content_type = get_object_or_404(ContentType, model=model_name)
   model = content_type.model_class()
   obj = get_object_or_404(model, id=object_id)

   like, created = Like.objects.get_or_create(
       user=request.user,
       content_type=content_type,
       object_id=obj.id
   )
   if not created:

       like.delete()
   return redirect(request.META.get('HTTP_REFERER', '/'))

