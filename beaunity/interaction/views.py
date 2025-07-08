from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Like, Favourite
from django.contrib.auth.decorators import login_required
from beaunity.event.models import Event
from beaunity.challenge.models import Challenge

# Create your views here.
@login_required(login_url='login')
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
   return redirect(request.META.get('HTTP_REFERER') + f"#{object_id}")

@login_required(login_url='login')
def favourite_functionality(request, model_name, object_id):
    content_type = get_object_or_404(ContentType, model=model_name)
    model = content_type.model_class()
    obj = get_object_or_404(model, id=object_id)

    favourite, created = Favourite.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=obj.id
    )
    if not created:

        favourite.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def join_functionality(request, model_name, pk):
    user = request.user.profile

    if model_name == 'event':
        obj = get_object_or_404(Event, pk=pk)
        # Join or leave logic — toggle join state
        if user.joined_events.filter(pk=pk).exists():
            user.joined_events.remove(obj)
        else:
            user.joined_events.add(obj)

    elif model_name == 'challenge':
        obj = get_object_or_404(Challenge, pk=pk)
        if user.joined_challenges.filter(pk=pk).exists():
            user.joined_challenges.remove(obj)
        else:
            user.joined_challenges.add(obj)


    return redirect(request.META.get('HTTP_REFERER', '/'))