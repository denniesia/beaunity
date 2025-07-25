from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from beaunity.category.models import Category
from beaunity.category.serializers import CategorySerializer

from beaunity.post.models import Post
from beaunity.post.serializers import PostSerializer

from beaunity.challenge.models import Challenge
from beaunity.challenge.serializers import ChallengeSerializer

from beaunity.event.models import Event
from beaunity.event.serializers import EventSerializer

from beaunity.accounts.serializers import UserSerializer


UserModel = get_user_model()

@extend_schema(
    tags=['search'],
    summary="Global Search endpoint",
    description="Search across posts, categories, events, challenges, and users by query string",
    parameters=[
        OpenApiParameter(
            name="q",
            description="Search",
            required=False,
            type=str,
            location=OpenApiParameter.QUERY # /endpoint/?param=value
        )
    ],
)
@api_view(['GET'])
def global_search(request):
    query = request.GET.get('q', '')

    if query:
        posts = Post.objects.filter(
            title__icontains=query
        )
        posts_data = PostSerializer(posts, many=True).data

        categories = Category.objects.filter(
            title__icontains=query
        )
        categories_data = CategorySerializer(categories, many=True).data

        events = Event.objects.filter(
            title__icontains=query
        )
        events_data = EventSerializer(events, many=True).data

        challenges = Challenge.objects.filter(
            title__icontains=query
        )
        challenges_data = ChallengeSerializer(challenges, many=True).data


        users = UserModel.objects.filter(
            username__icontains=query
        )
        users_data = UserSerializer(users, many=True).data

        return Response(
            {
                'posts': posts_data,
                'categories': categories_data,
                'events': events_data,
                'challenges': challenges_data,
                'users': users_data,
            }
        )
    return Response()